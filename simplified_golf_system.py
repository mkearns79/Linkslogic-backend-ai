"""
Simplified Golf Rules System - Version 2 with Enhanced Logging
Updated with better source tracking and no character limits
"""

import time
import logging
import re
import json
from typing import Dict, List, Optional, Any
from datetime import datetime

logger = logging.getLogger(__name__)

class SimplifiedGolfRulesSystem:
    """
    Simplified three-stage routing system with enhanced logging:
    1. Templates for Columbia CC local rules (high confidence only)
    2. Definitions for terminology  
    3. Unified AI for everything else with explicit exception checking
    """
    
    def __init__(self, 
                 templates: Dict,
                 definitions_db: Any,
                 vector_search_engine: Any,
                 openai_client: Any,
                 rules_database: Dict,
                 local_rules: List):
        """
        Initialize with existing components from web_api.py
        """
        self.templates = templates
        self.definitions_db = definitions_db
        self.search_engine = vector_search_engine
        self.client = openai_client
        self.rules_database = rules_database
        self.local_rules = local_rules
        
        # Model selection - UPDATE THIS based on check_openai_models.py results
        self.model = "gpt-4-turbo-preview"
        
        # Related rules mapping for exception handling
        self.RELATED_RULES = {
            '13.1': ['8.1d', '9.3', '9.4'],  # Putting green + conditions altered
            '13.1c': ['8.1d', '9.3'],
            '8.1': ['8.1d', '9.6', '9.3'],   # Conditions + who caused them
            '9.1': ['9.4', '9.5', '9.6'],    # Ball moved + by whom
            '9.3': ['8.1d', '14.2d'],        # Natural forces
            '9.4': ['9.5', '9.6', '13.1d'],  # Accidental movement
            '9.5': ['9.4', '9.6'],           # Deliberate actions
            '9.6': ['8.1d', '9.3'],          # Outside influence
            '11.1': ['11.2', '11.3'],        # Ball in motion interactions
            '11.2': ['11.1', '11.3'],
            '14.2': ['14.2d', '9.3'],        # Lifting/replacing + movement
            '14.2d': ['9.3', '13.1d'],       # Ball moved after replacement
            '16.1': ['16.1f', '8.1'],        # Abnormal conditions
            '17.1': ['17.1d', '17.2'],       # Penalty areas
            '19': ['19.2', '19.3'],          # Unplayable ball
        }
        
        # Source naming for logging consistency
        self.SOURCE_NAMES = {
            'template_high': 'template_high_confidence',
            'template_medium': 'template_medium_confidence', 
            'definitions': 'definitions_database',
            'ai_unified': 'ai_unified_simplified',
            'ai_exception': 'ai_with_exceptions',
            'error': 'error_fallback'
        }
        
    def process_query(self, question: str, verbose: bool = False) -> Dict:
        """
        Main entry point - simplified three-stage routing with comprehensive logging
        """
        start_time = time.time()
        query_id = f"q_{int(time.time()*1000)}"  # Unique query ID for tracking
        
        # Log query start
        self._log_query_start(query_id, question)
        
        # STAGE 1: Check templates (strict matching for Columbia CC rules)
        template_result = self._check_template_strict(question, verbose)
        if template_result and template_result['confidence'] >= 0.3:
            if verbose:
                logger.info(f"✅ [{query_id}] Using template with confidence {template_result['confidence']:.2f}")
            result = self._format_response(template_result, start_time, query_id)
            self._log_query_complete(query_id, question, result)
            return result
        
        # STAGE 2: Check definitions
        if self._is_definition_query(question):
            definition_result = self._get_definition_response(question)
            if definition_result:
                if verbose:
                    logger.info(f"✅ [{query_id}] Using definitions database")
                result = self._format_response(definition_result, start_time, query_id)
                self._log_query_complete(query_id, question, result)
                return result
        
        # STAGE 3: Unified AI with exception handling
        if verbose:
            logger.info(f"🤖 [{query_id}] Using unified AI with exception checking")
        ai_result = self._get_unified_ai_response(question, verbose, query_id)
        result = self._format_response(ai_result, start_time, query_id)
        self._log_query_complete(query_id, question, result)
        return result
    
    def _check_template_strict(self, question: str, verbose: bool = False) -> Optional[Dict]:
        """
        Stricter template matching - only return if we're very confident
        """
        question_lower = question.lower().strip()
        
        # Define strict patterns for each template
        template_patterns = {
            'clear_lost_ball': {
                'required': ['lost', 'ball'],
                'any_of': ['woods', 'rough', 'fescue', 'trees', 'cannot find', "can't find"],
                'min_matches': 2
            },
            'clear_out_of_bounds': {
                'required': ['out of bounds', 'ob'],
                'any_of': ['fence', 'boundary', 'over the'],
                'min_matches': 2  
            },
            'water_hazard_16': {
                'required': ['16'],
                'any_of': ['water', 'penalty area', 'hazard', 'pond', 'sixteenth'],
                'min_matches': 2
            },
            'water_hazard_17': {
                'required': ['17'],
                'any_of': ['water', 'penalty area', 'hazard', 'pond', 'seventeenth'],
                'min_matches': 2
            },
            'turf_nursery': {
                'required': ['turf', 'nursery'],
                'any_of': ['farm', 'grass', 'sod', 'maintenance'],
                'min_matches': 2
            },
            'maintenance_facility': {
                'required': ['maintenance'],
                'any_of': ['facility', 'building', 'shed', 'equipment', 'area'],
                'min_matches': 2
            },
            'aeration_holes': {
                'required': ['aeration'],
                'any_of': ['hole', 'holes', 'punch', 'punched', 'aerify'],
                'min_matches': 2
            },
            'construction_fence_relief': {
                'required': ['fence'],
                'any_of': ['purple line', 'construction', 'mesh', 'relief'],
                'min_matches': 2
            }
        }
        
        best_match = None
        best_confidence = 0.0
        
        for template_name, patterns in template_patterns.items():
            matches = 0
            confidence = 0.0
            
            # Check required patterns
            required_found = 0
            for required in patterns.get('required', []):
                if required in question_lower:
                    required_found += 1
            
            # If not all required patterns found, skip
            if required_found < len(patterns.get('required', [])):
                continue
                
            matches += required_found
            
            # Check any_of patterns
            any_of_found = 0
            for pattern in patterns.get('any_of', []):
                if pattern in question_lower:
                    any_of_found += 1
                    matches += 1
            
            # Calculate confidence
            total_patterns = len(patterns.get('required', [])) + len(patterns.get('any_of', []))
            if total_patterns > 0:
                confidence = matches / total_patterns
            
            # Apply minimum match requirement
            if matches >= patterns.get('min_matches', 2) and confidence > best_confidence:
                best_confidence = confidence
                best_match = template_name
                
        if verbose and best_match:
            logger.info(f"📋 Best template match: {best_match} (confidence: {best_confidence:.2f})")
        
        if best_match and best_confidence >= 0.3:  # Internal threshold
            template = self.templates.get(best_match)
            if template:
                source = 'template_high' if best_confidence >= 0.85 else 'template_medium'
                return {
                    'answer': template.get('quick_response', ''),
                    'source': source,
                    'rule_id': template.get('local_rule'),
                    'confidence': best_confidence,
                    'template_name': best_match,
                    'tokens_used': 0
                }
        
        return None
    
    def _is_definition_query(self, question: str) -> bool:
        """
        Check if this is asking for a definition
        """
        question_lower = question.lower()
        definition_indicators = [
            'what is a', 'what is an', 'what are',
            'what does', 'what do',
            'define', 'definition of',
            'meaning of', 'means',
            'what constitutes', 'explain what'
        ]
        return any(indicator in question_lower for indicator in definition_indicators)
    
    def _get_definition_response(self, question: str) -> Optional[Dict]:
        """
        Get definition from the definitions database
        """
        from golf_definitions_db import search_definitions_by_keyword
        
        # Extract key terms from the question
        question_lower = question.lower()
        
        # Extended list of golf terms to check
        golf_terms = [
            'penalty area', 'bunker', 'putting green', 'teeing area', 
            'general area', 'obstruction', 'loose impediment', 'ground under repair',
            'abnormal course condition', 'temporary water', 'provisional ball',
            'lost ball', 'out of bounds', 'water hazard', 'lateral water hazard',
            'casual water', 'stance', 'stroke', 'ball marker', 'wrong ball',
            'four-ball', 'match play', 'stroke play', 'handicap', 'net score',
            'gross score', 'through the green', 'hazard', 'relief area'
        ]
        
        for term in golf_terms:
            if term in question_lower:
                definitions = search_definitions_by_keyword(term)
                if definitions:
                    definition = definitions[0]
                    answer = f"**{definition['term']}**: {definition['definition']}"
                    if definition.get('examples'):
                        answer += f"\n\n**Examples**: {', '.join(definition['examples'][:3])}"
                    if definition.get('related_rules'):
                        answer += f"\n\n**Related Rules**: {', '.join(definition['related_rules'][:3])}"
                    
                    return {
                        'answer': answer,
                        'source': 'definitions',
                        'confidence': 'high',
                        'definition_id': definition.get('id'),
                        'tokens_used': 0
                    }
        return None
    
    def _get_unified_ai_response(self, question: str, verbose: bool = False, query_id: str = "") -> Dict:
        """
        Unified AI response with explicit exception checking and comprehensive logging
        """
        try:
            # Get relevant rules from vector search
            search_results = self.search_engine.search_with_precedence(
                question, 
                top_n=12,  # Get more rules for better context
                verbose=verbose
            )

            local_rules = [r for r in search_results if r.get('is_local')]
            official_rules = [r for r in search_results if not r.get('is_local')]
            search_results = local_rules[:4] + official_rules[:8]

            if verbose:
                logger.info(f"📊 [{query_id}] Balanced results: {len(local_rules[:4])} local + {len(official_rules[:8])} official")
                logger.info(f"📋 [{query_id}] After balancing: {[r['rule']['id'] for r in search_results]}")
            
            # Check if we found exception-related rules
            has_exception_rules = self._check_for_exception_rules(search_results)
            
            # Build enhanced context with related rules
            context = self._build_enhanced_context(search_results, question)
            
            # Log context stats
            if verbose:
                context_rules = re.findall(r'Rule [\d\.]+[a-z]?', context)
                logger.info(f"📚 [{query_id}] Context includes {len(context_rules)} rules")
                logger.info(f"🔍 [{query_id}] Full context being sent:\n{context[:2000]}")
                if has_exception_rules:
                    logger.info(f"⚠️ [{query_id}] Exception rules detected in context")
            
            # Create the unified prompt with explicit exception handling
            prompt = self._create_unified_prompt(question, context)

            # TEMPROARY - REMOVE AFTER TROUBLESHOOTING Right after line 300 where you create the prompt:
            prompt = self._create_unified_prompt(question, context)

            # TEMPROARY - REMOVE AFTER TROUBLESHOOTING ADD THIS DEBUG LOGGING:
            if verbose:
                logger.info(f"🔍 [{query_id}] CONTEXT BEING SENT TO AI:")
                logger.info(context)
                logger.info(f"📝 [{query_id}] END CONTEXT")
            
            # Get AI response
            response = self.client.chat.completions.create(
                model=self.model,  # Uses the model set in __init__
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=400
            )
            
            # Determine specific source based on what we found
            if has_exception_rules:
                source = 'ai_exception'
            else:
                source = 'ai_unified'
            
            return {
                'answer': response.choices[0].message.content,
                'source': source,
                'confidence': self._assess_confidence(search_results),
                'tokens_used': response.usage.total_tokens if response.usage else 0,
                'rules_used': [r['rule']['id'] for r in search_results],
                'has_exceptions': has_exception_rules,
                'model_used': self.model
            }
            
        except Exception as e:
            logger.error(f"❌ [{query_id}] Unified AI error: {e}")
            return {
                'answer': "I encountered an error processing your question. Please try rephrasing it.",
                'source': 'error',
                'confidence': 'none',
                'tokens_used': 0,
                'error': str(e)
            }
    
    def _check_for_exception_rules(self, search_results: List[Dict]) -> bool:
        """
        Check if any exception-related rules were found
        """
        exception_rule_patterns = ['8.1d', '9.3', '9.4', '9.5', '9.6', '11.', '14.2d']
        
        for result in search_results:
            rule_id = result['rule']['id']
            for pattern in exception_rule_patterns:
                if pattern in rule_id:
                    return True
        return False
    
    def _build_enhanced_context(self, search_results: List[Dict], question: str) -> str:
        """
        Build context with primary rules and related exception rules
        """
        context_parts = []
        included_rules = set()
        
        # First, add primary search results
        for i, result in enumerate(search_results):
            rule = result['rule']
            rule_id = rule['id']
            included_rules.add(rule_id)
            
            is_local = result.get('is_local', False)
            
            if is_local:
                context_part = f"COLUMBIA CC LOCAL RULE {rule_id}: {rule['title']}\n"
            else:
                context_part = f"Rule {rule_id}: {rule['title']}\n"
            
            # Include full rule text (no truncation for better accuracy)
            context_part += f"{rule.get('text', '')}\n"
            
            # Add conditions if available - EXCEPTIONS FIRST
            if 'conditions' in rule:
                # Separate exceptions from other conditions
                exceptions = []
                other_conditions = []
                
                for condition in rule['conditions'][:5]:
                    situation = condition.get('situation', '')
                    if 'exception' in situation.lower():
                        exceptions.append(condition)
                    else:
                        other_conditions.append(condition)
                
                # Show exceptions FIRST and prominently
                if exceptions:
                    context_part += "\n⚠️ EXCEPTIONS:\n"
                    for exc in exceptions:
                        context_part += f"  • {exc.get('explanation', '')}\n"
                        # Add examples if available
                        if 'examples' in exc:
                            for ex in exc['examples'][:2]:
                                context_part += f"    Example: {ex}\n"
                
                # Then show other conditions
                if other_conditions:
                    context_part += "\nConditions and Applications:\n"
                    for condition in other_conditions:
                        context_part += f"- {condition.get('situation', '')}: {condition.get('explanation', '')}\n"
            
            context_parts.append(context_part)
        
        # Now add related exception rules
        related_rules_to_add = set()
        for result in search_results:
            rule_id = result['rule']['id']
            base_rule = rule_id.split('.')[0] if '.' in rule_id else rule_id
            
            # Check for related rules
            for pattern, related_list in self.RELATED_RULES.items():
                if base_rule.startswith(pattern.split('.')[0]):
                    related_rules_to_add.update(related_list)
        
        # Remove already included rules
        related_rules_to_add -= included_rules
        
        # Fetch and add related rules
        if related_rules_to_add:
            context_parts.append("\n--- RELATED EXCEPTION RULES ---")
            for rule_id in list(related_rules_to_add)[:4]:  # Include up to 4 related rules
                rule = self._get_rule_by_id(rule_id)
                if rule:
                    # Include full text for exception rules (they're critical)
                    context_parts.append(f"\nRule {rule_id}: {rule.get('title', '')}\n{rule.get('text', '')}")
        
        return "\n".join(context_parts)
    
    def _get_rule_by_id(self, rule_id: str) -> Optional[Dict]:
        """
        Get a rule by its ID from the database
        """
        # Check local rules first
        for rule in self.local_rules:
            if rule.get('id') == rule_id:
                return rule
        
        # Check official rules
        if rule_id in self.rules_database:
            return self.rules_database[rule_id]
        
        return None
    
    def _create_unified_prompt(self, question: str, context: str) -> str:
        """
        Create the unified prompt with explicit exception handling instructions
        """
        prompt = f"""You are an expert golf rules official at Columbia Country Club with complete knowledge of both USGA Rules and Columbia's local rules.

QUESTION: {question}

RELEVANT RULES CONTEXT:
{context}

CRITICAL INSTRUCTIONS FOR ACCURATE RULINGS:

1. IDENTIFY THE PRIMARY RULE that applies to this situation

2. CHECK FOR EXCEPTIONS - This is absolutely critical! Consider:
   - WHO caused the condition:
     * If another player/person caused it → Check Rule 8.1d (may restore conditions)
     * If animal/natural forces caused it → Check Rules 9.3, 9.6
     * If player accidentally caused it → Check Rule 9.4
   
   - WHEN it happened:
     * After ball came to rest → Different rules may apply (8.1d, 9.3)
     * During the stroke → Rule 9.1b
     * While ball in motion → Rules 11.1-11.3
     * After marking and lifting → Rule 14.2d
   
   - WHERE on the course:
     * Putting green → Special rules under Rule 13
     * Penalty area → Rule 17 procedures
     * Bunker → Rule 12 specific rules
     * Teeing area → Rule 6 applies
   
   - INTENT (accidental vs. deliberate):
     * Accidental movement → Often no penalty or different procedure
     * Deliberate actions → Usually penalties apply

   - EXCEPTIONS WITHIN RULES:
     * Many rules have exceptions listed within them - check carefully!
     * Look for conditions labeled "Exception:", "Allowed:", or "Does not apply when:" clauses
     * Read ALL conditions carefully before concluding something is not allowed

3. CHECK COLUMBIA CC LOCAL RULES:
   - If a Columbia local rule applies to this specific situation, it takes precedence
   - Columbia rules are marked as "CCC-" in the context

4. PROVIDE YOUR ANSWER:
   - State the applicable rule(s) clearly with rule numbers
   - Mention ANY exceptions or special cases that apply
   - Specify the correct procedure step by step
   - State any penalties (or explicitly note if there's no penalty)
   - If an exception changes the ruling, explain why

RESPONSE FORMAT:
- Start with the direct answer/ruling first (1-2 sentences)
- Then provide the explanation with rule citations
- Keep total response concise: 150-250 words
- Don't explore rules that don't apply to this situation
- Set max_tokens to 400 in the API call

Start your response appropriately:
- "According to Columbia's local rules..." (if using local rule)
- "According to the Rules of Golf, Rule X.X..." (if using official rule)
        
Example of complete answer:
"According to The Rules of Golf, Rule 13.1c, you generally cannot repair damage on the fringe. However, Rule 8.1d provides an exception: since another player caused the damage after your ball came to rest, you ARE allowed to restore the conditions to what they were. You may repair the pitch mark without penalty."

Now provide your complete ruling:"""
        
        return prompt
    
    def _assess_confidence(self, search_results: List[Dict]) -> str:
        """
        Assess confidence based on search result quality
        """
        if not search_results:
            return 'low'
        
        best_score = search_results[0].get('best_similarity', 0) if search_results else 0
        
        # Check if we have local rules in results
        has_local = any(r.get('is_local', False) for r in search_results[:3])
        
        if has_local and best_score > 0.6:
            return 'high'  # High confidence when local rules match
        elif best_score > 0.7:
            return 'high'
        elif best_score > 0.5:
            return 'medium'
        else:
            return 'low'
    
    def _format_response(self, result: Dict, start_time: float, query_id: str = "") -> Dict:
        """
        Format the response with timing information and proper source naming
        """
        result['response_time'] = round(time.time() - start_time, 2)
        result['query_id'] = query_id
        
        # Normalize source name for consistency
        if result['source'] in self.SOURCE_NAMES:
            result['source'] = self.SOURCE_NAMES[result['source']]
        
        return result
    
    def _log_query_start(self, query_id: str, question: str):
        """
        Log the start of a query
        """
        logger.info(f"🏌️ [{query_id}] Query started: {question[:100]}...")
    
    def _log_query_complete(self, query_id: str, question: str, result: Dict):
        """
        Comprehensive logging for dashboard - no character limits
        """
        try:
            # Build comprehensive log entry
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "query_id": query_id,
                "question": question,  # Full question, no truncation
                "answer": result.get('answer', ''),  # Full answer, no truncation
                "source": result.get('source', 'unknown'),
                "rule_type": self._determine_rule_type(result),
                "confidence": result.get('confidence', 'unknown'),
                "tokens_used": result.get('tokens_used', 0),
                "estimated_cost": self._calculate_cost(result.get('tokens_used', 0)),
                "response_time": result.get('response_time', 0),
                "success": result.get('source') != 'error',
                "template_name": result.get('template_name', ''),
                "rules_used": result.get('rules_used', []),
                "has_exceptions": result.get('has_exceptions', False),
                "model_used": result.get('model_used', ''),
                "definition_id": result.get('definition_id', ''),
                "rule_id": result.get('rule_id', '')
            }
            
            # Log to Cloud Logging with GOLF_QUERY prefix for dashboard
            logger.info(f"GOLF_QUERY: {json.dumps(log_entry)}")
            
            # Additional detailed logging for debugging
            if result.get('source') == 'error':
                logger.error(f"❌ [{query_id}] Query failed: {result.get('error', 'Unknown error')}")
            else:
                logger.info(f"✅ [{query_id}] Query completed: {result['source']} in {result['response_time']}s")
                
        except Exception as e:
            logger.error(f"Logging error for query {query_id}: {e}")
    
    def _determine_rule_type(self, result: Dict) -> str:
        """
        Determine if the rule is local or official based on the response
        """
        answer = result.get('answer', '')
        rule_id = result.get('rule_id', '')
        rules_used = result.get('rules_used', [])
        
        if any('CCC-' in r for r in rules_used):
            return 'local'
        elif 'CCC-' in rule_id or 'Columbia' in answer[:200]:
            return 'local'
        elif result.get('source') == 'definitions_database':
            return 'definition'
        else:
            return 'official'
    
    def _calculate_cost(self, tokens: int) -> float:
        """
        Calculate estimated cost based on model and tokens
        """
        # Pricing per 1K tokens (you can update these based on current pricing)
        pricing = {
            "gpt-4-turbo-preview": 0.01,
            "gpt-4-0125-preview": 0.01,
            "gpt-4": 0.03,
            "gpt-3.5-turbo": 0.001
        }
        
        cost_per_1k = pricing.get(self.model, 0.01)
        return round((tokens / 1000) * cost_per_1k, 4)


# Integration function for web_api.py
def create_simplified_system(templates, definitions_db, search_engine, client, rules_db, local_rules):
    """
    Factory function to create the simplified system with existing components
    """
    return SimplifiedGolfRulesSystem(
        templates=templates,
        definitions_db=definitions_db,
        vector_search_engine=search_engine,
        openai_client=client,
        rules_database=rules_db,
        local_rules=local_rules
    )
