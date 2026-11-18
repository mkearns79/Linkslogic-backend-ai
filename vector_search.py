"""
LLM-optimized semantic search for golf rules with hybrid AI systems.

REFACTORED: February 17, 2026
- Removed ClubSpecificVectorSearch (dead code in production)
- Removed stale standalone apply_columbia_boosting() (production version lives in web_api.py)
- Removed test_local_rules() auto-running debug code
- Kept RulesVectorSearch base class with universal golf boosting logic
- Kept helper functions: extract_hole_number_simple, detect_wrong_ball_scenario

NOTE: This module requires sentence-transformers and sklearn, which are NOT in the
production container. It is used only by golf_rules_hybrid.py for local development/testing.
Production uses ProductionHybridVectorSearch in web_api.py (OpenAI embeddings API).

If you need Columbia CC-specific boosting in production, use apply_columbia_boosting() in web_api.py.
If you need universal golf boosting (wrong ball, provisional ball, bounce-back) in production,
port apply_universal_golf_boosting() from RulesVectorSearch to web_api.py.
"""
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os
import warnings
warnings.filterwarnings('ignore')
import logging
logger = logging.getLogger(__name__)

# Import our rules database
from golf_rules_data import RULES_DATABASE
from columbia_cc_local_rules_db import COLUMBIA_CC_LOCAL_RULES

import re

def extract_hole_number_simple(query: str):
    """Simple hole number extraction."""
    patterns = [
        r'\b(\d{1,2})(?:th|st|nd|rd)?\s+(?:hole|green)\b',
        r'\bhole\s+(\d{1,2})\b',
        r'\b(\d{1,2})(?:th|st|nd|rd)\b'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, query.lower())
        if match:
            hole_num = int(match.group(1))
            if 1 <= hole_num <= 18:
                return hole_num
    return None

def detect_wrong_ball_scenario(query_lower):
    """
    Detect if query describes a wrong ball scenario with comprehensive pattern matching.
    Returns True if this appears to be about someone playing the wrong ball.
    """
    
    # Define comprehensive patterns for wrong ball scenarios
    wrong_ball_patterns = [
        # Direct wrong ball references
        'wrong ball', 'played wrong ball', 'hit wrong ball',
        
        # Someone else played my ball
        'opponent hit my ball', 'opponent played my ball',
        'someone hit my ball', 'someone played my ball', 'someone else hit my ball',
        'another player hit my ball', 'another player played my ball',
        'other player hit my ball', 'other player played my ball',
        
        # My ball was played by others
        'my ball was hit', 'my ball was played', 'my ball got hit',
        'they hit my ball', 'they played my ball',
        
        # Playing someone else's ball  
        'hit someone else ball', 'played someone else ball',
        'hit another player ball', 'played another player ball',
        'hit opponent ball', 'played opponent ball',
        
        # Confusion scenarios
        'hit their ball by mistake', 'played their ball by mistake',
        'accidentally hit their ball', 'accidentally played their ball',
        'mixed up balls', 'confused balls', 'switched balls'
    ]
    
    # Check for any matching patterns
    for pattern in wrong_ball_patterns:
        if pattern in query_lower:
            return True
    
    # Additional logic: Check for combination patterns
    # "hit" or "played" + possessive pronouns + "ball"
    hit_played_terms = ['hit', 'played', 'struck', 'took']
    possessive_terms = ['my ball', 'his ball', 'her ball', 'their ball', 'opponent ball']
    other_person_terms = ['opponent', 'someone', 'another player', 'other player', 'they', 'he', 'she']
    
    has_action = any(term in query_lower for term in hit_played_terms)
    has_possessive = any(term in query_lower for term in possessive_terms)
    has_other_person = any(term in query_lower for term in other_person_terms)
    
    # If we have action + possessive + other person, likely wrong ball scenario
    if has_action and has_possessive and has_other_person:
        return True
    
    return False


# NOTE: Standalone apply_columbia_boosting() was removed in refactor (Feb 2026).
# The production version lives in web_api.py -> apply_columbia_boosting()
# and is called from ProductionHybridVectorSearch.search_with_precedence().

class RulesVectorSearch:
    """Original search class - keep all existing functionality"""
    
    def __init__(self, model_name='all-MiniLM-L6-v2', cache_dir='./embeddings_cache'):
        """
        Initialize the LLM-optimized semantic search engine.
        
        Args:
            model_name: Sentence transformer model to use
            cache_dir: Directory to cache embeddings
        """
        self.model_name = model_name
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        
        try:
            print(f"Loading semantic model: {model_name}")
            print("Optimized for LLM integration")
            
            # Load the sentence transformer model
            self.model = SentenceTransformer(model_name)
            
            # Prepare documents and embeddings
            self.rules = RULES_DATABASE
            self.documents = []
            self.rule_ids = []
            self.document_metadata = []
            
            self._prepare_documents()
            self._load_or_compute_embeddings()
            
            print(f"âœ… Search engine ready with {len(self.documents)} documents")
            
        except Exception as e:
            print(f"Error initializing semantic search: {str(e)}")
            raise
    
    def _prepare_documents(self):
        """Prepare documents optimized for LLM consumption."""
        for rule in self.rules:
            # Create main rule document with LLM-friendly structure
            main_doc = f"Golf Rule {rule['id']}: {rule['title']}. {rule['text']}"
            
            # Add keywords for better matching
            if rule.get('keywords'):
                main_doc += f" Keywords: {', '.join(rule['keywords'])}"
            
            self.documents.append(main_doc)
            self.rule_ids.append(rule['id'])
            self.document_metadata.append({
                'type': 'main_rule',
                'rule_id': rule['id'],
                'title': rule['title'],
                'condition_index': None,
                'full_rule_data': rule  # Store full rule for LLM context
            })
            
            # Create condition documents with enhanced context
            if 'conditions' in rule:
                for idx, condition in enumerate(rule['conditions']):
                    situation = condition.get('situation', '')
                    explanation = condition.get('explanation', '')
                    
                    # Enhanced condition document with rule context
                    condition_doc = (f"Golf Rule {rule['id']} ({rule['title']}) - "
                                   f"Situation: {situation}. "
                                   f"Rule: {explanation}")
                    
                    # Add examples in LLM-friendly format
                    if 'examples' in condition and condition['examples']:
                        examples_text = ', '.join(condition['examples'])
                        condition_doc += f" Examples: {examples_text}"
                    
                    self.documents.append(condition_doc)
                    self.rule_ids.append(rule['id'])
                    self.document_metadata.append({
                        'type': 'condition',
                        'rule_id': rule['id'],
                        'title': rule['title'],
                        'condition_index': idx,
                        'situation': situation,
                        'condition_data': condition,
                        'parent_rule_data': rule  # Full parent rule for context
                    })
    
    def _load_or_compute_embeddings(self):
        """Load cached embeddings or compute them."""
        cache_file = os.path.join(self.cache_dir, f"golf_rules_llm_{self.model_name.replace('/', '_')}.pkl")
        
        # Try to load cached embeddings
        if os.path.exists(cache_file):
            try:
                print("Loading cached embeddings...")
                with open(cache_file, 'rb') as f:
                    cache_data = pickle.load(f)
                    
                if (cache_data.get('model_name') == self.model_name and 
                    len(cache_data.get('embeddings', [])) == len(self.documents)):
                    self.document_embeddings = cache_data['embeddings']
                    print("âœ… Cached embeddings loaded successfully!")
                    return
                else:
                    print("Cache invalid, recomputing embeddings...")
            except Exception as e:
                print(f"Error loading cache: {e}, recomputing embeddings...")
        
        # Compute embeddings
        print(f"Computing embeddings for {len(self.documents)} documents...")
        
        self.document_embeddings = self.model.encode(
            self.documents,
            convert_to_numpy=True,
            show_progress_bar=True,
            batch_size=32
        )
        
        # Cache the embeddings
        try:
            cache_data = {
                'model_name': self.model_name,
                'embeddings': self.document_embeddings,
                'document_count': len(self.documents)
            }
            with open(cache_file, 'wb') as f:
                pickle.dump(cache_data, f)
            print(f"âœ… Embeddings cached to {cache_file}")
        except Exception as e:
            print(f"Warning: Could not cache embeddings: {e}")
    
    def search(self, query, top_n=3):
        """
        Standard search maintaining backward compatibility.
        
        Args:
            query: Search query string
            top_n: Number of results to return
            
        Returns:
            List of search results with rules and similarity scores
        """
        return self._search_internal(query, top_n, optimize_for_llm=False)
    
    def search_for_llm(self, query, top_n=5, include_context=True, similarity_threshold=0.15):
        """
        LLM-optimized search with enhanced context and formatting.
        
        Args:
            query: Search query string
            top_n: Number of results to return (recommend 3-5 for LLMs)
            include_context: Whether to include additional context for LLM
            similarity_threshold: Minimum similarity to include result
            
        Returns:
            Enhanced search results optimized for LLM consumption
        """
        return self._search_internal(
            query, 
            top_n, 
            optimize_for_llm=True, 
            include_context=include_context,
            similarity_threshold=similarity_threshold
        )
    
    def _search_internal(self, query, top_n, optimize_for_llm=False, include_context=True, similarity_threshold=0.1):
        """Internal search method with LLM optimization options."""
        try:
            # Encode the query
            query_embedding = self.model.encode([query], convert_to_numpy=True)
            
            # Calculate similarities
            similarities = cosine_similarity(query_embedding, self.document_embeddings)[0]
            
            # Get top matches (get more initially to group by rule)
            top_indices = np.argsort(similarities)[-top_n*3:][::-1]
            
            # Group results by rule to avoid duplicates
            rule_results = {}
            
            for idx in top_indices:
                if similarities[idx] < similarity_threshold:
                    continue
                    
                metadata = self.document_metadata[idx]
                rule_id = metadata['rule_id']
                
                if rule_id not in rule_results:
                    rule_results[rule_id] = {
                        'rule': metadata.get('full_rule_data') or metadata.get('parent_rule_data'),
                        'similarity': similarities[idx],
                        'best_match_type': metadata['type'],
                        'best_condition': None,
                        'all_matches': [],
                        'llm_context': {}  # Additional context for LLM
                    }
                else:
                    # Update if this match is better
                    if similarities[idx] > rule_results[rule_id]['similarity']:
                        rule_results[rule_id]['similarity'] = similarities[idx]
                        rule_results[rule_id]['best_match_type'] = metadata['type']
                
                # Store match details
                match_info = {
                    'similarity': similarities[idx],
                    'type': metadata['type'],
                    'metadata': metadata,
                    'matched_text': self.documents[idx]  # Include the actual matched text
                }
                
                rule_results[rule_id]['all_matches'].append(match_info)
                
                # Track best condition match with enhanced data
                if metadata['type'] == 'condition':
                    if (not rule_results[rule_id]['best_condition'] or 
                        similarities[idx] > rule_results[rule_id]['best_condition']['similarity']):
                        
                        rule_results[rule_id]['best_condition'] = {
                            'similarity': similarities[idx],
                            'condition_data': metadata.get('condition_data'),
                            'situation': metadata.get('situation', ''),
                            'matched_text': self.documents[idx]
                        }
                
                # Add LLM-specific context
                if optimize_for_llm:
                    rule_results[rule_id]['llm_context'] = {
                        'query_relevance': similarities[idx],
                        'match_explanation': self._generate_match_explanation(query, metadata, similarities[idx]),
                        'key_concepts': self._extract_key_concepts(metadata),
                        'related_rules': self._find_related_rules(rule_id)
                    }
            
            # Sort by similarity and return top N
            sorted_results = sorted(
                rule_results.values(),
                key=lambda x: x['similarity'],
                reverse=True
            )[:top_n]
            
            # Format results
            formatted_results = []
            for result in sorted_results:
                formatted_result = {
                    'rule': result['rule'],
                    'similarity': result['similarity'],
                    'best_match_type': result['best_match_type'],
                    'best_condition': result['best_condition']
                }
                
                # Add LLM-specific enhancements
                if optimize_for_llm:
                    formatted_result.update({
                        'llm_context': result['llm_context'],
                        'all_matches': result['all_matches'],
                        'context_for_llm': self._format_context_for_llm(result),
                        'confidence_score': self._calculate_confidence(result)
                    })
                
                formatted_results.append(formatted_result)
            
            return formatted_results
            
        except Exception as e:
            print(f"Error during search: {str(e)}")
            return []
    
    def _generate_match_explanation(self, query, metadata, similarity):
        """Generate explanation of why this rule matched the query."""
        if metadata['type'] == 'condition':
            return f"Query matched specific condition: {metadata.get('situation', 'N/A')}"
        else:
            return f"Query matched main rule about {metadata.get('title', 'N/A')}"
    
    def _extract_key_concepts(self, metadata):
        """Extract key concepts from the matched rule for LLM context."""
        concepts = []
        
        if metadata['type'] == 'condition' and metadata.get('condition_data'):
            cond = metadata['condition_data']
            if 'examples' in cond:
                concepts.extend(cond['examples'][:3])  # Limit to top 3 examples
        
        rule_data = metadata.get('full_rule_data') or metadata.get('parent_rule_data')
        if rule_data and 'keywords' in rule_data:
            concepts.extend(rule_data['keywords'][:5])  # Limit to top 5 keywords
            
        return list(set(concepts))  # Remove duplicates
    
    def _find_related_rules(self, rule_id):
        """Find rules related to the matched rule for additional LLM context."""
        # Simple related rule detection based on rule numbering
        related = []
        
        base_rule = rule_id.split('.')[0]  # e.g., "4.1" -> "4"
        
        for rule in self.rules:
            other_id = rule['id']
            other_base = other_id.split('.')[0]
            
            # Same base rule but different sub-rule
            if other_base == base_rule and other_id != rule_id:
                related.append({
                    'id': other_id,
                    'title': rule['title']
                })
                
            if len(related) >= 3:  # Limit to 3 related rules
                break
                
        return related
    
    def _format_context_for_llm(self, result):
        """Format rule context in a way that's optimal for LLM consumption."""
        rule = result['rule']
        context = {
            'rule_summary': f"Rule {rule['id']}: {rule['title']}",
            'main_text': rule['text'],
            'relevant_condition': None
        }
        
        if result['best_condition'] and result['best_condition']['condition_data']:
            cond = result['best_condition']['condition_data']
            context['relevant_condition'] = {
                'situation': cond.get('situation', ''),
                'explanation': cond.get('explanation', ''),
                'examples': cond.get('examples', [])[:3]  # Limit examples
            }
        
        return context
    
    def _calculate_confidence(self, result):
        """Calculate confidence score for LLM to understand result quality."""
        base_score = result['similarity']
        
        # Boost confidence for condition matches (more specific)
        if result['best_match_type'] == 'condition':
            base_score *= 1.1
            
        # Boost confidence for high similarity
        if base_score > 0.7:
            confidence = 'high'
        elif base_score > 0.4:
            confidence = 'medium'
        else:
            confidence = 'low'
            
        return {
            'score': base_score,
            'level': confidence,
            'reasoning': f"Based on {result['best_match_type']} match with {base_score:.3f} similarity"
        }

    def get_llm_prompt_context(self, query, search_results):
        """
        Generate formatted context specifically for LLM prompts.
        
        Args:
            query: Original user query
            search_results: Results from search_for_llm()
            
        Returns:
            Formatted string ready to include in LLM prompt
        """
        if not search_results:
            return "No relevant golf rules found for this query."
        
        context_parts = [
            f"Based on the query '{query}', here are the most relevant golf rules:\n"
        ]
        
        for i, result in enumerate(search_results, 1):
            rule = result['rule']
            confidence = result.get('confidence_score', {})
            
            context_parts.append(f"{i}. RULE {rule['id']}: {rule['title']}")
            context_parts.append(f"   Confidence: {confidence.get('level', 'unknown').upper()}")
            context_parts.append(f"   Text: {rule['text']}")
            
            # Add specific condition if highly relevant
            if (result.get('best_condition') and 
                result['best_condition']['similarity'] > 0.5):
                
                cond = result['best_condition']['condition_data']
                if cond:
                    context_parts.append(f"   Most Relevant Situation: {cond.get('situation', '')}")
                    context_parts.append(f"   Rule Details: {cond.get('explanation', '')}")
                    
                    if cond.get('examples'):
                        examples = ', '.join(cond['examples'][:2])
                        context_parts.append(f"   Examples: {examples}")
            
            context_parts.append("")  # Empty line between rules
        
        return "\n".join(context_parts)

    def get_relevant_conditions(self, rule, query, max_conditions=2):
        """Get the most relevant conditions for a rule based on the query."""
        if 'conditions' not in rule or not rule['conditions']:
            return []
    
        # Score conditions by relevance to query
        condition_scores = []
        query_words = set(query.lower().split())
    
        for cond in rule['conditions']:
            # Combine situation and explanation for scoring
            condition_text = (cond.get('situation', '') + ' ' + cond.get('explanation', '')).lower()
            condition_words = set(condition_text.split())
        
            # Calculate word overlap score
            overlap = len(query_words.intersection(condition_words))
        
            # Boost score for exact phrase matches
            phrase_bonus = 0
            for word in query_words:
                if len(word) > 3 and word in condition_text:
                    phrase_bonus += 1
        
            total_score = overlap + phrase_bonus
            condition_scores.append((total_score, cond))
    
        # Return top N most relevant conditions with score > 0
        condition_scores.sort(reverse=True, key=lambda x: x[0])
        return [cond for score, cond in condition_scores[:max_conditions] if score > 0]

    def compress_rule_for_llm(self, rule, query, max_text_length=200):
        """Create a compressed version of the rule optimized for LLM token efficiency."""
        compressed = f"Rule {rule['id']}: {rule['title']}\n"
    
        # Truncate main rule text
        rule_text = rule.get('text', '')
        if len(rule_text) > max_text_length:
            compressed += f"{rule_text[:max_text_length]}...\n"
        else:
            compressed += f"{rule_text}\n"
    
        # Add only the most relevant conditions
        relevant_conditions = self.get_relevant_conditions(rule, query, max_conditions=2)
    
        if relevant_conditions:
            compressed += "Key situations:\n"
            for cond in relevant_conditions:
                situation = cond.get('situation', '')[:80]  # Limit situation length
                explanation = cond.get('explanation', '')[:120]  # Limit explanation length
            
                # Add ellipsis if truncated
                if len(cond.get('situation', '')) > 80:
                    situation += "..."
                if len(cond.get('explanation', '')) > 120:
                    explanation += "..."
                
                compressed += f"- {situation}: {explanation}\n"
    
        return compressed

    def get_compressed_context_for_llm(self, search_results, query):
        """Generate compressed context from search results for LLM."""
        if not search_results:
            return "No relevant rules found."
    
        context_parts = []
    
        for i, result in enumerate(search_results, 1):
            rule = result['rule']
            similarity = result.get('similarity', 0)
        
            # Only include rules with decent similarity
            if similarity < 0.2:
                continue
            
            compressed_rule = self.compress_rule_for_llm(rule, query)
        
            # Add confidence indicator
            confidence = "High" if similarity > 0.7 else "Medium" if similarity > 0.4 else "Low"
            context_parts.append(f"[{confidence} confidence]\n{compressed_rule}")
        
            # Limit to prevent token explosion
            if len('\n'.join(context_parts)) > 1000:  # Stop before hitting ~1000 chars
                break
    
        return '\n'.join(context_parts)

    def apply_universal_golf_boosting(self, rule_results, query, verbose=False):
        """
        Universal golf rule boosting for scenarios that apply to all golf courses.
        This handles generic golf rule conflicts that aren't course-specific.
        """
        query_lower = query.lower()
        
        # PROVISIONAL BALL IDENTIFICATION SCENARIO BOOSTING (NEW)
        provisional_keywords = ['provisional', 'provisional ball']
        identification_keywords = [
            'cannot distinguish', 'cannot tell which', 'cannot identify which',
            'which is which', 'both balls', 'found both', 'same area',
            'look identical', 'both found', 'distinguish between'
        ]
    
        has_provisional = any(keyword in query_lower for keyword in provisional_keywords)
        has_identification_issue = any(keyword in query_lower for keyword in identification_keywords)
        
        if has_provisional and has_identification_issue:
            if verbose:
                print("ðŸŽ¯ Universal Golf: Detected provisional ball identification scenario")
            
            # Boost Rule 18.3c(2) and related provisional rules
            for rule_id in rule_results:
                rule_text = rule_results[rule_id]['rule'].get('text', '').lower()
                rule_title = rule_results[rule_id]['rule'].get('title', '').lower()
                rule_conditions = rule_results[rule_id]['rule'].get('conditions', [])
                
                # Check if this rule addresses provisional ball identification
                rule_addresses_identification = False
                
                # Direct rule ID matches
                if '18.3c(2)' in rule_id or '18.3c' in rule_id or '18.3' in rule_id:
                    if 'provisional' in rule_text:
                        rule_addresses_identification = True
                
                # Check rule text for provisional identification content
                if 'provisional' in rule_text and any(keyword in rule_text for keyword in identification_keywords):
                    rule_addresses_identification = True
                
                # Check conditions for specific provisional identification scenarios
                if isinstance(rule_conditions, list):
                    for condition in rule_conditions:
                        if isinstance(condition, dict):
                            condition_text = str(condition.get('explanation', '')).lower()
                            condition_examples = condition.get('examples', [])
                            
                            # Look for provisional identification in conditions
                            if ('provisional' in condition_text and 
                                any(keyword in condition_text for keyword in identification_keywords)):
                                rule_addresses_identification = True
                                break
                            
                            # Check examples
                            if isinstance(condition_examples, list):
                                examples_text = ' '.join(str(ex).lower() for ex in condition_examples)
                                if ('provisional' in examples_text and 
                                    any(keyword in examples_text for keyword in identification_keywords)):
                                    rule_addresses_identification = True
                                    break
                
                if rule_addresses_identification:
                    old_score = rule_results[rule_id]['best_similarity']
                    rule_results[rule_id]['best_similarity'] *= 8.0  # Strong boost
                    
                    if verbose:
                        new_score = rule_results[rule_id]['best_similarity']
                        print(f"   ðŸŽ¯ {rule_id}: {old_score:.3f} â†’ {new_score:.3f} (8.0x boost - provisional ID rule)")
            
            # De-boost rules that don't address this specific scenario
            irrelevant_rule_types = ['lost ball', 'out of bounds', 'penalty area', 'unplayable']
            for rule_id in rule_results:
                rule_text = rule_results[rule_id]['rule'].get('text', '').lower()
                rule_title = rule_results[rule_id]['rule'].get('title', '').lower()
                
                # Check if rule is about irrelevant scenarios
                if any(irrelevant in rule_text or irrelevant in rule_title for irrelevant in irrelevant_rule_types):
                    if 'provisional' not in rule_text:  # Don't de-boost provisional-related rules
                        old_score = rule_results[rule_id]['best_similarity']
                        rule_results[rule_id]['best_similarity'] *= 0.3
                        
                        if verbose:
                            new_score = rule_results[rule_id]['best_similarity']
                            print(f"   ðŸ”» {rule_id}: {old_score:.3f} â†’ {new_score:.3f} (0.3x de-boost - irrelevant context)")

        # WRONG BALL SCENARIO BOOSTING (universal across all courses)
        if detect_wrong_ball_scenario(query_lower):
            if verbose:
                print("ðŸŽ¯ Universal Golf: Detected wrong ball scenario")
            
            # Boost rules about playing wrong ball (Rule 6.3c and similar)
            wrong_ball_rule_indicators = [
                'wrong ball', 'playing wrong ball', '6.3c', 'rule 6.3',
                'substitute ball', 'correct ball'
            ]
            
            for rule_id in rule_results:
                rule_text = rule_results[rule_id]['rule'].get('text', '').lower()
                rule_title = rule_results[rule_id]['rule'].get('title', '').lower()
                
                # Check if this rule is about wrong ball scenarios
                if any(indicator in rule_text or indicator in rule_title 
                       for indicator in wrong_ball_rule_indicators):
                    old_score = rule_results[rule_id]['best_similarity']
                    rule_results[rule_id]['best_similarity'] *= 5.0
                    
                    if verbose:
                        new_score = rule_results[rule_id]['best_similarity']
                        print(f"   ðŸŽ¯ {rule_id}: {old_score:.3f} â†’ {new_score:.3f} (5.0x boost - wrong ball rule)")
            
            # De-boost ball in motion rules (common wrong match)
            ball_in_motion_indicators = [
                'ball in motion', 'moving ball', 'accidentally deflects', 
                'accidentally moves', 'deflected', 'stopped'
            ]
            
            for rule_id in rule_results:
                rule_text = rule_results[rule_id]['rule'].get('text', '').lower()
                rule_title = rule_results[rule_id]['rule'].get('title', '').lower()
                
                # Check if this rule is about ball in motion (wrong context for wrong ball)
                if any(indicator in rule_text or indicator in rule_title 
                       for indicator in ball_in_motion_indicators):
                    old_score = rule_results[rule_id]['best_similarity']
                    rule_results[rule_id]['best_similarity'] *= 0.3
                    
                    if verbose:
                        new_score = rule_results[rule_id]['best_similarity']
                        print(f"   ðŸ”» {rule_id}: {old_score:.3f} â†’ {new_score:.3f} (0.3x de-boost - ball in motion conflict)")
        
        # BALL BOUNCED BACK IN BOUNDS SCENARIO BOOSTING
        out_of_bounds_keywords = ['out of bounds', 'ob', 'out-of-bounds']
        bounce_back_keywords = [
            'bounced back', 'bounce back', 'bounced back in', 'hit tree and bounced',
            'hit and bounced', 'deflected back', 'came back in', 'ricocheted back',
            'caromed back', 'rebounded', 'kicked back'
        ]
        in_bounds_keywords = ['in bounds', 'back in bounds', 'back in', 'back onto course']
        
        has_out_of_bounds = any(keyword in query_lower for keyword in out_of_bounds_keywords)
        has_bounce_back = any(keyword in query_lower for keyword in bounce_back_keywords)
        has_in_bounds = any(keyword in query_lower for keyword in in_bounds_keywords)
        
        if has_out_of_bounds and (has_bounce_back or has_in_bounds):
            if verbose:
                print("ðŸŽ¯ Universal Golf: Detected ball bounced back in bounds scenario")
            
            # This is about ball position, not OB relief - boost official boundary rules
            for rule_id in rule_results:
                rule_text = rule_results[rule_id]['rule'].get('text', '').lower()
                rule_title = rule_results[rule_id]['rule'].get('title', '').lower()
                
                # Boost official rules about ball position/boundary definitions
                if ('18.2' in rule_id and 'boundary' in rule_text) or 'boundary' in rule_title:
                    old_score = rule_results[rule_id]['best_similarity']
                    rule_results[rule_id]['best_similarity'] *= 6.0
                    
                    if verbose:
                        new_score = rule_results[rule_id]['best_similarity']
                        print(f"   ðŸŽ¯ {rule_id}: {old_score:.3f} â†’ {new_score:.3f} (6.0x boost - boundary definition rule)")
            
            # De-boost local rules about OB relief (this isn't about relief procedures)
            for rule_id in rule_results:
                rule_data = rule_results[rule_id]['rule']
                is_local = rule_results[rule_id].get('is_local', False)
                
                if is_local and 'out of bounds' in rule_data.get('text', '').lower():
                    # Check if it's about relief procedures rather than boundary definition
                    if any(relief_word in rule_data.get('text', '').lower() 
                           for relief_word in ['relief', 'drop', 'penalty stroke', 'options']):
                        old_score = rule_results[rule_id]['best_similarity']
                        rule_results[rule_id]['best_similarity'] *= 0.2
                        
                        if verbose:
                            new_score = rule_results[rule_id]['best_similarity']
                            print(f"   ðŸ”» {rule_id}: {old_score:.3f} â†’ {new_score:.3f} (0.2x de-boost - OB relief not applicable)")
        
        return rule_results


# NOTE: ClubSpecificVectorSearch was removed in refactor (Feb 2026).
# It was dead code — never instantiated in production (web_api.py uses
# ProductionHybridVectorSearch with OpenAI embeddings instead).
# Its Columbia CC boosting logic was stale; the production version is
# apply_columbia_boosting() in web_api.py.
#
# If you need local development search with sentence-transformers,
# use RulesVectorSearch directly with apply_universal_golf_boosting().
#
# The old golf_rules_hybrid.py also imported ClubSpecificVectorSearch;
# that file is legacy code superseded by simplified_golf_system.py.


# Backward compatibility
if __name__ == "__main__":
    pass
