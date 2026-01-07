from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import time
import os
import re
import math
from datetime import datetime
from datetime import timedelta
import logging
from openai import OpenAI
from dotenv import load_dotenv
from simplified_golf_system import SimplifiedGolfRulesSystem, create_simplified_system


# Import your existing comprehensive databases
from golf_rules_data import RULES_DATABASE
from columbia_cc_local_rules_db import COLUMBIA_CC_LOCAL_RULES
from golf_definitions_db import (
    GOLF_DEFINITIONS_DATABASE, 
    search_definitions_by_keyword,
    get_definition_by_id,
    get_definitions_by_category,
    COMMON_DEFINITION_LOOKUPS
)

from simplified_golf_system import SimplifiedGolfRulesSystem, create_simplified_system

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Global variables for system status
ai_system_available = False
ai_error_message = ""
USE_SIMPLIFIED_SYSTEM = True  # Set to True to test
simplified_system = None

# RESTORED: Your Complete Template System (from your original system)
COMMON_QUERY_TEMPLATES = {
    "clear_lost_ball": {
        "keywords": ["lost my ball in the woods", "lost my ball in the rough", "can't find my ball in the woods", "lost ball in trees", "lost ball in the fescue", "ball is lost in", "cannot find my ball"],
        "local_rule": "CCC-1",
        "quick_response": """At Columbia Country Club, you have TWO options for lost balls:

OPTION 1 - Columbia CC Special Relief (2 penalty strokes):
Instead of going back to where you last played, you can:
- Estimate where your ball was lost
- Find the nearest fairway point to that spot  
- Drop anywhere between two imaginary lines from the hole through each point
- Stay within two club-lengths of those lines
- Must not be closer to the hole than where ball was lost

OPTION 2 - Standard Rule (1 penalty stroke):
Return to where you last played and hit again (stroke and distance).

Most golfers prefer the Columbia CC option since you don't have to walk back."""
    },

    "clear_out_of_bounds": {
        "keywords": ["out of bounds", "over the fence", "ob", "ball is OB", "ball went OB"],
        "local_rule": "CCC-1",
        "quick_response": """At Columbia, you have TWO options for out-of-bounds balls:

OPTION 1 - Columbia CC Special Relief (2 penalty strokes):
Instead of going back to where you last played, you can:
• Estimate where your ball crossed out of bounds or was lost
• Find the nearest fairway point to that spot
• Drop anywhere between two imaginary lines: one from the hole through where your ball was lost, and one from the hole through the nearest fairway point
• Stay within two club-lengths of those lines
• Must not be closer to the hole than where ball was lost

OPTION 2 - Standard Rule (1 penalty stroke):
Return to where you last played and hit again (stroke and distance).

Exception: player gets FREE RELIEF from a ball hit into the maintenance area to the left of #10, whether the ball is found or not."""
    },
    
    "water_hazard_16": {
        "keywords": ["water on 16", "water on #16", "penalty area on #16", "water on hole 16", "hit it in the water on the 16th", "water hazard on 16"],
        "local_rule": "CCC-2",
        "quick_response": """On the 16th hole at Columbia CC, your options under Rule 17.1 depend on where the ball entered the water:

If your ball went into the water/penalty area on the south side of the footbridge marked by yellow stakes:
• Stroke-and-Distance Relief (rehit from tee) (1 penalty stroke)
• Back-on-the-Line Relief (1 penalty stroke), OR
• Use the special DROPPING ZONE near the 16th green (1 penalty stroke)

If your ball went into the water/penalty area on the north side of the footbridge marked by red stakes, you have an additional relief option to drop within two club lengths from the point where the original ball is estimated to have crossed into the red penalty area, no closer to the hole (1 penalty stroke)."""
    },
    
    "water_hazard_17": {
        "keywords": ["water on #17", "water on 17", "ball in water on hole 17", "water on seventeen", "17th hole water", "pond on hole seventeen", "17th water", "drop zone on seventeen"],
        "local_rule": "CCC-2", 
        "quick_response": """On the 17th hole at Columbia CC:

If your ball goes in the POND (west of the footbridge):
• Standard relief under Rule 17.1 (1 penalty stroke), OR  
• Use the special DROPPING ZONE near the 17th green (1 penalty stroke)
If your ball is in other penalty areas on 17th, including on the cart bridge:
• Standard relief under Rule 17.1 only
The dropping zone is only available for the main pond area, not other penalty areas on the hole."""
    },

    "turf_nursery": {
        "keywords": ["turf nursery", "turf farm", "fairway farm", "nursery area", "ball in nursery", "tahoma farm", "nursery near maintenance", "grass farm", "farm near the shack", "nursery near the shack", "sod farm", "sod nursery"],
        "local_rule": "CCC-8",
        "quick_response": """According to Columbia Country Club's local rules, the turf nursery adjacent to the maintenance area is a No Play Zone.

MANDATORY FREE RELIEF required:
- You CANNOT play the ball as it lies
- You MUST take free relief under Rule 16.1f
- Drop at nearest point of complete relief from the nursery area
- Within one club-length, not nearer hole
- No penalty stroke

This is different from regular ground under repair - relief is mandatory, not optional."""
    },
     
    "maintenance_facility": {
        "keywords": ["Maintenance facility on #10", "ball near maintenance building on hole 10", "road left of 10", "maintenance road", "paved area left of 10", "maintenance", "building", "facility", "shed", "equipment", "roof"],
        "local_rule": "CCC-7",
        "quick_response": """Maintenance facility at Columbia CC (near holes 9 & 10):

FREE RELIEF available from:
• All maintenance buildings
• Storage tanks and sheds  
• Paved and gravel areas
• Retention ponds
• Equipment
The entire maintenance complex is treated as one large immovable obstruction. Drop within one club-length of your nearest point of complete relief, no closer to the hole."""
    },
    
     "OB_lines": {
        "keywords": ["touching the out-of-bounds line", "on the out of bounds line", "touching the white line", "on the white line", "painted boundary line", "on the painted OB line", "touching the white paint", "on the line of white stakes"],
        "official_definition": "Out of Bounds",
        "quick_response": """According to the Rules of Golf, when out-of-bounds is defined by a painted line on the ground, the boundary edge is the course-side edge of the line, and the line itself is out of bounds.

When stakes are used to define or show the boundary edge, they are boundary objects, which are treated as immovable even if they are movable or any part of them is movable."""
    },
    
    "aeration_holes": {
        "keywords": ["aeration", "hole in green", "aerify", "punched green"],
        "local_rule": "CCC-11",
        "quick_response": """Aeration holes at Columbia CC:

FREE RELIEF available when:
• Ball is IN an aeration hole
• Ball TOUCHES an aeration hole  
• Aeration hole interferes with your swing
NO RELIEF when:
• Aeration hole only affects your stance
• On putting green: only affects your line of putt
Relief: Drop/place within one club-length of nearest point of relief. If you get relief and the ball rolls into another aeration hole, you get relief again."""
    },

    "construction_fence_relief": {
        "keywords": ["mesh fence relief", "against purple line fence", "against construction fence", "construction fence interfering with swing", "construction fence relief", "purple line fence relief"],
        "local_rule": "CCC-6",
        "quick_response": """According to Columbia Country Club's local rules, the fence around the Purple Line construction area (including mesh/green fencing) is considered a boundary fence.

NO FREE RELIEF is available from this fence, or any fence at Columbia.

Your options:
- Play the ball as it lies if possible
- Declare the ball unplayable under Rule 19 (1 penalty stroke)
  - Drop within two club-lengths, not nearer hole
  - Drop on line from hole through ball, going back as far as desired
  - Return to previous spot where you played

The construction fence is treated as a boundary, not a regular obstruction."""
    },

    "green_stakes_cart_path": {
    "keywords": [
        "green stakes behind 14", "green stakes behind 17", "green stakes behind fourteenth", "green stakes behind seventeenth",
        "cart path behind 14th green", "cart path behind 17th green", "path behind fourteenth green", "path behind seventeenth green", 
        "cart path green stakes", "path marked with green stakes", "integral object cart path",
        "no relief cart path", "cart path behind green", "path behind 14", "path behind 17",
        "green stakes cart path", "stakes behind green", "marked cart path", "Path behind #14 & #17 green"
    ],
    "local_rule": "CCC-4",
    "quick_response": """According to Columbia Country Club's local rules, certain cart paths are designated as INTEGRAL OBJECTS from which NO FREE RELIEF is available:

AFFECTED AREAS:
• Cart path sections behind 14th green marked by green stakes
• Cart path sections behind 17th green marked by green stakes  
• Unpaved road behind 12th green
NO FREE RELIEF AVAILABLE - Your options:
• Play the ball as it lies if possible
• Declare the ball unplayable under Rule 19 (1 penalty stroke)
    - Drop within two club-lengths, not nearer hole
    - Drop on line from hole through ball, going back as far as desired
    - Return to previous spot where you played
Note: All other cart paths on the course DO provide free relief under Rule 16.1 - only these specifically marked areas are integral objects."""
    },

    "purple_line_boundary": {
    "keywords": [
        "purple line", "purple line out of bounds", "purple line boundary", "ball crossed purple line", "ball over purple line", "ball over the train tracks",
        "purple line construction", "construction boundary", "ball in tunnel", "ball past purple line",
        "purple line area", "construction area boundary", "ball beyond purple line", "crossed construction line",
        "purple boundary line", "construction zone boundary", "ball in construction area",
        "over the purple line", "past the purple line", "through purple line", "across purple line", "across the train tracks"
    ],
    "local_rule": "CCC-6",
    "quick_response": """According to Columbia Country Club's local rules, the Purple Line construction fence is a BOUNDARY, and any ball that crosses this boundary is OUT OF BOUNDS.

IMPORTANT BOUNDARY RULE:
• NO RELIEF for balls near or against Purple Line boundary fence
• Any ball that crosses the Purple Line boundary is OUT OF BOUNDS
• This applies EVEN IF the ball comes to rest in a seemingly playable position
• This includes balls that end up on the other side of the boundary
• This includes balls that come to rest inside tunnels or other areas beyond the line
OUT OF BOUNDS RELIEF OPTIONS:
You have TWO options under Columbia CC's local rules:

OPTION 1 - Columbia CC Special Relief (2 penalty strokes):
• Estimate where your ball crossed the Purple Line boundary
• Find the nearest fairway point to that crossing point
• Drop within two club-lengths of the line between the hole and those reference points
• Must not be closer to the hole than where ball crossed boundary
OPTION 2 - Standard Rule (1 penalty stroke):
• Return to where you last played and hit again (stroke and distance)
Remember: The Purple Line boundary fence (including any mesh) provides NO FREE RELIEF - it is a boundary, not an obstruction."""
    }
}

class ProductionHybridVectorSearch:
    """FIXED: Production hybrid search with proper caching to prevent API loops."""
    
    def __init__(self):
        self.embeddings_cache = {}
        self.rule_embeddings_cache = {}  # Separate cache for rule embeddings
        self.local_rules = self._process_local_rules()
        self.official_rules = self._process_official_rules()
        self._precompute_rule_embeddings()  # Pre-compute on startup
        
    def _process_local_rules(self):
        """Process Columbia CC local rules for search."""
        processed_rules = []
        
        for rule in COLUMBIA_CC_LOCAL_RULES['local_rules']:
            processed_rules.append({
                'id': rule['id'],
                'title': rule['title'],
                'text': rule['text'],
                'keywords': rule.get('keywords', []),
                'is_local': True,
                'priority': 1,
                'search_text': f"{rule['title']} {rule['text']} {' '.join(rule.get('keywords', []))}"
            })
            
        return processed_rules
    
    def _process_official_rules(self):
        """Process official rules from your comprehensive database."""
        processed_rules = []
    
        # CRITICAL FIX: Include ALL rules or at least the most important ones
        # Priority rules that should definitely be included
        priority_rule_ids = [
            "15.2", "15.2a", "15.2a(2)", "15.2a(3)", "15.2b",  # Movable obstructions
            "16.1", "16.1a", "16.1b",  # Abnormal course conditions
            "8.1a", "8.1b", "8.1c", "8.1d",  # Playing course as found
            "17.1", "17.1a", "17.1b", "17.1c", "17.1d",  # Penalty areas
            "9.4", "9.4a", "9.4b",  # Ball moved
            "7.4",  # Ball moved during search
            "14.2", "14.2b", "14.2e",  # Replacing ball procedures
        ]
    
        # First, add priority rules
        added_ids = set()
        for rule in RULES_DATABASE:
            if rule['id'] in priority_rule_ids:
                processed_rules.append({
                    'id': rule['id'],
                    'title': rule['title'],
                    'text': rule['text'],
                    'keywords': rule.get('keywords', []),
                    'is_local': False,
                    'priority': 2,
                    'search_text': f"{rule['title']} {rule['text']} {' '.join(rule.get('keywords', []))}"
                })
                added_ids.add(rule['id'])
    
        # Then add remaining rules up to a reasonable limit (e.g., 100 total)
        remaining_count = 0
        max_additional = 100 - len(processed_rules)
    
        for rule in RULES_DATABASE:
            if rule['id'] not in added_ids and remaining_count < max_additional:
                processed_rules.append({
                    'id': rule['id'],
                    'title': rule['title'],
                    'text': rule['text'],
                    'keywords': rule.get('keywords', []),
                    'is_local': False,
                    'priority': 2,
                    'search_text': f"{rule['title']} {rule['text']} {' '.join(rule.get('keywords', []))}"
                })
                remaining_count += 1
    
        logger.info(f"📚 Processed {len(processed_rules)} official rules for embedding")
        return processed_rules
    
    def _precompute_rule_embeddings(self):
        """Pre-compute embeddings for all rules to avoid repeated API calls."""
        logger.info("🔄 Pre-computing rule embeddings (one-time startup cost)...")
        
        all_rules = self.local_rules + self.official_rules
        rule_texts = [rule['search_text'][:500] for rule in all_rules]  # Limit text length
        
        try:
            # Get embeddings for all rules in one API call
            embeddings = self.get_embeddings_batch(rule_texts)
            
            if embeddings:
                for i, rule in enumerate(all_rules):
                    self.rule_embeddings_cache[rule['id']] = embeddings[i]
                
                logger.info(f"✅ Pre-computed embeddings for {len(all_rules)} rules")
            else:
                logger.error("❌ Failed to pre-compute rule embeddings")
                
        except Exception as e:
            logger.error(f"❌ Error pre-computing embeddings: {e}")
    
    def get_embeddings_batch(self, texts, max_batch_size=100):
        """Get embeddings for multiple texts in batches."""
        try:
            if not texts:
                return []
            
            all_embeddings = []
            
            # Process in batches to avoid API limits
            for i in range(0, len(texts), max_batch_size):
                batch = texts[i:i + max_batch_size]
                
                response = client.embeddings.create(
                    model="text-embedding-3-small",
                    input=batch
                )
                
                batch_embeddings = [d.embedding for d in response.data]
                all_embeddings.extend(batch_embeddings)
                
                logger.info(f"📊 Processed embedding batch {i//max_batch_size + 1}")
            
            return all_embeddings
            
        except Exception as e:
            logger.error(f"Batch embedding error: {e}")
            return None
    
    def get_embeddings(self, text):
        """Get embeddings for a single text with caching."""
        try:
            # Check cache first
            cache_key = str(hash(text))
            if cache_key in self.embeddings_cache:
                return [self.embeddings_cache[cache_key]]
            
            response = client.embeddings.create(
                model="text-embedding-3-small",
                input=[text]
            )
            
            embedding = response.data[0].embedding
            self.embeddings_cache[cache_key] = embedding
            return [embedding]
            
        except Exception as e:
            logger.error(f"Single embedding error: {e}")
            return None
    
    def cosine_similarity(self, a, b):
        """Calculate cosine similarity between two vectors."""
        import math
        dot_product = sum(x * y for x, y in zip(a, b))
        magnitude_a = math.sqrt(sum(x * x for x in a))
        magnitude_b = math.sqrt(sum(x * x for x in b))
        return dot_product / (magnitude_a * magnitude_b) if magnitude_a * magnitude_b > 0 else 0
    
    def search_with_precedence(self, query, hole_number=None, top_n=3, verbose=False):
        """FIXED: Search with precedence using pre-computed embeddings."""
        try:
            if verbose:
                logger.info(f"🔍 Searching with precedence for: {query}")
                
            # Get query embedding (only 1 API call per query now)
            query_embedding = self.get_embeddings(query)
            if not query_embedding:
                return []
            
            query_vector = query_embedding[0]
            results = []
            
            # Use pre-computed rule embeddings (no API calls in loop)
            all_rules = self.local_rules + self.official_rules
            
            for rule in all_rules:
                rule_id = rule['id']
                
                # Use pre-computed embedding
                if rule_id in self.rule_embeddings_cache:
                    rule_embedding = self.rule_embeddings_cache[rule_id]
                    similarity = self.cosine_similarity(query_vector, rule_embedding)
                    
                    results.append({
                        'rule': {
                            'id': rule['id'],
                            'title': rule['title'],
                            'text': rule['text']
                        },
                        'best_similarity': similarity,
                        'is_local': rule['is_local'],
                        'priority': rule['priority'],
                        'rule_type': 'local' if rule['is_local'] else 'official'
                    })
            
            # Sort by local rules first, then similarity
            def sort_key(result):
                base_score = result['best_similarity']
                if result['is_local']:
                    return base_score * 1.5  # 50% boost for local rules
                return base_score
            
            results.sort(key=sort_key, reverse=True)
            
            if verbose:
                logger.info(f"✅ Found {len(results)} total rules, returning top {top_n}")
                for i, result in enumerate(results[:top_n]):
                    rule_type = "LOCAL" if result['is_local'] else "OFFICIAL"
                    logger.info(f"  {i+1}. {rule_type} - {result['rule']['id']}: {result['best_similarity']:.3f}")
            
            # Purple line boost
            if 'purple line' in query.lower():
                for result in results:
                    if result.get('rule', {}).get('id') == 'CCC-6':
                        result['best_similarity'] *= 3.0
                        break
                # Re-sort after boosting
                results.sort(key=sort_key, reverse=True)
                
                if verbose:
                    logger.info("🎯 Applied purple line boost to CCC-6")

            return results[:top_n]
            
        except Exception as e:
            logger.error(f"Search error: {e}")
            return []

def build_enhanced_rule_context(search_results, max_rules=3):
    """
    Build COMPLETE context including full rule text and ALL conditions.
    This ensures the AI has complete information about when rules apply.
    """
    context_parts = []
    
    for i, result in enumerate(search_results[:max_rules]):
        rule = result['rule']
        is_local = result.get('is_local', False)
        
        # Start with rule identification
        if is_local:
            context_part = f"COLUMBIA CC LOCAL RULE - {rule['title']}\n"
        else:
            context_part = f"Official Rule {rule['id']}: {rule['title']}\n"
        
        # CRITICAL FIX: Include COMPLETE rule text, not truncated
        rule_text = rule.get('text', '')
        context_part += f"Full Text: {rule_text}\n"
        
        # CRITICAL: Add ALL conditions that specify when rule applies and exceptions
        if 'conditions' in rule and rule['conditions']:
            context_part += "\nIMPORTANT CONDITIONS AND APPLICATIONS:\n"
            for j, condition in enumerate(rule['conditions']):
                situation = condition.get('situation', '')
                explanation = condition.get('explanation', '')
                examples = condition.get('examples', [])
                
                context_part += f"\n{j+1}. {situation}\n"
                context_part += f"   Explanation: {explanation}\n"
                if examples:
                    context_part += f"   Examples: {', '.join(examples[:5])}\n"
        
        # Add any enhanced context if it exists
        if 'enhanced_context' in rule:
            context_part += f"\nAdditional Context: {rule['enhanced_context']}\n"
        
        context_parts.append(context_part)
    
    return "\n" + "="*50 + "\n".join(context_parts)


def detect_definition_query(query):
    """Detect if query is asking for a golf definition."""
    query_lower = query.lower().strip()
    
    # Direct definition queries
    definition_patterns = [
        r'what is (?:a |an |the )?(.+?)(?:\?|$)',
        r'define (?:a |an |the )?(.+?)(?:\?|$)', 
        r'definition of (?:a |an |the )?(.+?)(?:\?|$)',
        r'what does (.+?) mean(?:\?|$)',
        r'meaning of (.+?)(?:\?|$)',
        r'(.+?) definition(?:\?|$)',
        r'tell me about (?:a |an |the )?(.+?)(?:\?|$)'
    ]
    
    import re
    for pattern in definition_patterns:
        match = re.search(pattern, query_lower)
        if match:
            term = match.group(1).strip()
            # Check common lookups first
            if term in COMMON_DEFINITION_LOOKUPS:
                return COMMON_DEFINITION_LOOKUPS[term]
            
            # Search by keywords
            results = search_definitions_by_keyword([term])
            if results and results[0]['relevance_score'] >= 2:
                return results[0]['definition']['id']
    
    return None

def create_definition_response(definition_id, query):
    """Create a formatted response for a definition query."""
    definition = get_definition_by_id(definition_id)
    if not definition:
        return None
    
    response = f"""**{definition['term']}**

{definition['definition']}

**Examples:**
{chr(10).join([f'• {example}' for example in definition['examples'][:4]])}

**Related Rules:** {', '.join(definition['related_rules'])}"""
    
    return {
        'success': True,
        'answer': response,
        'question': query,
        'source': 'definitions_database',
        'definition_id': definition_id,
        'rule_type': 'definition',
        'confidence': 'high'
    }

def enhance_ai_prompt_with_definitions(prompt, query):
    """
    Option 1: Include potentially relevant definitions and let AI choose.
    For stake queries, includes both movable obstruction and penalty area definitions.
    """
    try:
        logger.info(f"🔍 DEBUG: enhance_ai_prompt_with_definitions called for query: {query}")
        
        query_lower = query.lower()
        definitions_to_add = []
        
        # Check if stakes are mentioned
        stake_mentioned = any(term in query_lower for term in ['stake', 'stakes', 'red', 'yellow'])
        
        if stake_mentioned:
            # Add BOTH definitions and let the AI figure out which is relevant
            movable_def = get_definition_by_id('MOVABLE_OBSTRUCTION')
            penalty_def = get_definition_by_id('PENALTY_AREA')
            
            if movable_def:
                definitions_to_add.append(movable_def)
            if penalty_def:
                definitions_to_add.append(penalty_def)
        
        # Also check for other specific terms
        query_words = query_lower.split()
        for word in query_words:
            if word in COMMON_DEFINITION_LOOKUPS and word not in ['stake', 'stakes', 'red', 'yellow']:
                def_id = COMMON_DEFINITION_LOOKUPS[word]
                definition = get_definition_by_id(def_id)
                if definition and definition not in definitions_to_add:
                    definitions_to_add.append(definition)
        
        # Add definitions to prompt if any were found
        if definitions_to_add:
            definitions_context = "\n\nPOTENTIALLY RELEVANT DEFINITIONS:\n"
            for definition in definitions_to_add[:3]:  # Limit to 3 definitions max
                definitions_context += f"\n{definition['term']}: {definition['definition']}\n"
                if 'related_rules' in definition and definition['related_rules']:
                    definitions_context += f"Related Rules: {', '.join(definition['related_rules'])}\n"
            
            definitions_context += "\nNote: Apply only the definitions relevant to the specific question being asked.\n"
            return prompt + definitions_context
        
        return prompt
        
    except Exception as e:
        logger.error(f"❌ DEBUG: Definition enhancement failed with error: {e}")
        import traceback
        logger.error(f"❌ DEBUG: Traceback: {traceback.format_exc()}")
        return prompt

def check_common_query(question):
    """RESTORED: Your original template checking function."""
    question_lower = question.lower()
    
    for template_name, template_data in COMMON_QUERY_TEMPLATES.items():
        for keyword_phrase in template_data["keywords"]:
            if keyword_phrase.lower() in question_lower:
                return template_data
    
    return None

def classify_intent_enhanced(question):
    """
    Enhanced intent classification that better identifies complex queries.
    """
    try:
        classification_prompt = f"""Classify this golf rules question into the most specific category:

Question: {question}

Categories:
A) Relief procedures - How to take relief, drop procedures, relief options
B) Obstruction/condition interference - When relief is available from obstructions or abnormal conditions
C) Ball position/status - Where the ball is, which area, in/out of bounds
D) Penalty situations - Penalty strokes, breaches, wrong ball
E) Definitions - What is a term, terminology questions
F) Procedures - How to proceed, order of play, marking
G) Equipment - Clubs, balls, devices
H) General/Other - Doesn't fit above categories

Answer with letter only:"""

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": classification_prompt}],
            temperature=0.1,
            max_tokens=5
        )
        
        result = response.choices[0].message.content.strip().upper()
        
        # Map to intent categories
        intent_map = {
            'A': 'relief',
            'B': 'obstruction',
            'C': 'position',
            'D': 'penalty',
            'E': 'definition',
            'F': 'procedure',
            'G': 'equipment'
        }
        
        return intent_map.get(result[0], 'general')
            
    except Exception as e:
        logger.error(f"Enhanced intent classification error: {e}")
        return 'general'

def get_position_focused_response(question, verbose=False):
    """Focused AI for position/boundary questions with local rules context"""
    try:
        # Get local rules context
        search_engine = ProductionHybridVectorSearch()
        search_results = search_engine.search_with_precedence(question, top_n=3, verbose=verbose)
        
        # TEMPORARY DEBUG LOGGING
        if verbose:
            logger.info(f"🔍 Position search results for '{question}':")
            for i, result in enumerate(search_results):
                rule_id = result['rule']['id']
                title = result['rule']['title']
                is_local = result.get('is_local', False)
                score = result.get('best_similarity', 0)
                logger.info(f"  {i+1}. {'LOCAL' if is_local else 'OFFICIAL'} - {rule_id}: {title} (score: {score:.3f})")
        
        context = build_enhanced_rule_context(search_results, max_rules=3)

        base_prompt = f"""Golf rules expert: Determine ball position/status at Columbia Country Club. Be aware that many ball position/status situations are not Columbia-specific, and for these the official golf rules are the more suitable source for the response. Do not reference Columbia local rules unless the local rules apply to the user's specific question.

Question: {question}

Relevant Rules:
{context}

Focus on: 
- Local boundary definitions (purple line, train tracks, construction areas, out of bounds markers)
- Ball location determination (in bounds vs out of bounds, penalty area vs general area)
- Course area identification (teeing area, bunker, penalty area, putting green, general area)
- Local obstruction rules (cart paths as integral objects vs immovable obstructions)
- Ball identification issues (which ball is mine, provisional vs original)
- Playability status (can I play this ball, is it the right ball)
- Movement and position after deflection (bounced back, kicked back, ricocheted)
- Columbia-specific areas (maintenance zones, construction boundaries, integral cart paths)

Key distinctions:
- Ball position ≠ relief procedures (focus on WHERE not HOW to get relief)
- Different course areas have different rules
- Local boundaries may differ from standard golf boundaries

If COLUMBIA CC LOCAL RULE applies, start with "According to Columbia's local rules..."
If an official rule applies, start with "According to the Rules of Golf, Rule X.X..."
"""

        enhanced_prompt = enhance_ai_prompt_with_definitions(base_prompt, question)

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": enhanced_prompt}],
            temperature=0.1,
            max_tokens=300
        )
        
        result = {
            'answer': response.choices[0].message.content,
            'source': 'ai_position',
            'confidence': 'high',
            'tokens_used': response.usage.total_tokens if response.usage else 0
        }

        # Log token usage
        logger.info(f"📊 General response tokens used: {result['tokens_used']}")

        return result
        
    except Exception as e:
        logger.error(f"Position response error: {e}")
        return get_fallback_response()

def get_relief_focused_response(question, verbose=False):
    """Focused AI for relief/procedure questions - COMPLETE ANSWERS"""
    try:
        search_engine = ProductionHybridVectorSearch()
        search_results = search_engine.search_with_precedence(question, top_n=4, verbose=verbose)
        
        if verbose:
            logger.info(f"🔍 Relief search results for '{question}':")
            for i, result in enumerate(search_results):
                rule_id = result['rule']['id']
                title = result['rule']['title']
                is_local = result.get('is_local', False)
                score = result.get('best_similarity', 0)
                logger.info(f"  {i+1}. {'LOCAL' if is_local else 'OFFICIAL'} - {rule_id}: {title} (score: {score:.3f})")
        
        context = build_enhanced_rule_context(search_results, max_rules=3)
        
        # REMOVED word limit - allow complete answers
        base_prompt = f"""You are a golf rules expert at Columbia Country Club. Provide a COMPLETE and ACCURATE answer about relief options. Do not reference Columbia Local Rules unless the local rule applies to the user's specific question.

Question: {question}

Relevant Rules Context:
{context}

CRITICAL INSTRUCTIONS:
1. Provide a COMPLETE answer - do not truncate or summarize important details, but be as consise as possible to provide a complete answer
2. Include ALL conditions that must be met for relief to be available
3. Specify what types of interference qualify (e.g., swing, stance, line of play)
4. Mention ANY exceptions or situations where relief is NOT available
5. Be clear about whether there is free relief or if a penalty applies
5. If discussing movable obstructions, clearly state they can be removed without penalty
6. If discussing immovable obstructions, explain the relief procedure
7. Distinguish between movable and immovable obstructions if relevant

Start your response with either:
- "According to Columbia's local rules..." (if using local rule)
- "According to the Rules of Golf, Rule X.X..." (if using official rule)

Provide the complete procedure including:
- Whether there is a penalty or free relief
- Where and how to take relief
- Any specific requirements or limitations"""

        enhanced_prompt = enhance_ai_prompt_with_definitions(base_prompt, question)

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": enhanced_prompt}],
            temperature=0.1,
            max_tokens=300  # Increased from 125 to allow complete answers
        )
        
        result = {
            'answer': response.choices[0].message.content,
            'source': 'ai_relief',
            'confidence': 'high',
            'tokens_used': response.usage.total_tokens if response.usage else 0
        }
        
        # Log token usage
        logger.info(f"📊 General response tokens used: {result['tokens_used']}")

        return result

    except Exception as e:
        logger.error(f"Relief response error: {e}")
        return get_fallback_response()

def get_penalty_focused_response(question, verbose=False):
    """Focused AI for penalty situations - COMPLETE ANSWERS"""
    try:
        search_engine = ProductionHybridVectorSearch()
        search_results = search_engine.search_with_precedence(question, top_n=3, verbose=verbose)
        
        if verbose:
            logger.info(f"🔍 Penalty search results for '{question}':")
            for i, result in enumerate(search_results):
                rule_id = result['rule']['id']
                title = result['rule']['title']
                is_local = result.get('is_local', False)
                score = result.get('best_similarity', 0)
                logger.info(f"  {i+1}. {'LOCAL' if is_local else 'OFFICIAL'} - {rule_id}: {title} (score: {score:.3f})")
        
        context = build_enhanced_rule_context(search_results, max_rules=3)
        
        base_prompt = f"""You are a golf rules expert at Columbia Country Club. Provide a COMPLETE answer about penalties and breaches. Do not reference Columbia's local rules unless the local rule applies to the user's specific question.

Question: {question}

Relevant Rules Context:
{context}

CRITICAL INSTRUCTIONS:
1. Provide a COMPLETE answer with all details
2. Clearly state whether there is a penalty or not
3. If there is a penalty, specify exactly what it is (one stroke, two strokes, loss of hole, disqualification)
4. Explain ALL conditions that affect whether a penalty applies
5. Include any exceptions where the penalty does NOT apply
6. Describe the complete procedure to continue play after the breach

Start your response appropriately:
- "According to Columbia's local rules..." (if using local rule)
- "According to the Rules of Golf, Rule X.X..." (if using official rule)"""

        # Apply definition enhancement (Option 1)
        enhanced_prompt = enhance_ai_prompt_with_definitions(base_prompt, question)

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": enhanced_prompt}],
            temperature=0.1,
            max_tokens=300  # Increased to allow complete answers
        )
        
        result = {
            'answer': response.choices[0].message.content,
            'source': 'ai_penalty',
            'confidence': 'high',
            'tokens_used': response.usage.total_tokens if response.usage else 0
        }
        
        # Log token usage
        logger.info(f"📊 Penalty response tokens used: {result['tokens_used']}")
        
        return result
        
    except Exception as e:
        logger.error(f"Penalty response error: {e}")
        return get_fallback_response()


def get_procedure_focused_response(question, verbose=False):
    """Focused AI for procedure questions - COMPLETE ANSWERS"""
    try:
        search_engine = ProductionHybridVectorSearch()
        search_results = search_engine.search_with_precedence(question, top_n=3, verbose=verbose)
        
        if verbose:
            logger.info(f"🔍 Procedure search results for '{question}':")
            for i, result in enumerate(search_results):
                rule_id = result['rule']['id']
                title = result['rule']['title']
                is_local = result.get('is_local', False)
                score = result.get('best_similarity', 0)
                logger.info(f"  {i+1}. {'LOCAL' if is_local else 'OFFICIAL'} - {rule_id}: {title} (score: {score:.3f})")
        
        context = build_enhanced_rule_context(search_results, max_rules=3)
        
        base_prompt = f"""You are a golf rules expert at Columbia Country Club. Provide a COMPLETE answer about golf procedures. Do not mention Columbia's Local Rules unless a local rule applies to the user's specific question.

Question: {question}

Relevant Rules Context:
{context}

CRITICAL INSTRUCTIONS:
1. Provide a COMPLETE step-by-step procedure
2. Number each step clearly for easy following
3. Include ALL requirements and conditions for each step
4. Specify any penalties for incorrect procedures
5. Mention any exceptions or special situations
6. Be thorough - do not skip steps or details

Start your response appropriately:
- "According to Columbia's local rules..." (if using local rule)
- "According to the Rules of Golf, Rule X.X..." (if using official rule)

Format the procedure clearly with numbered steps when applicable."""

        # Apply definition enhancement (Option 1)
        enhanced_prompt = enhance_ai_prompt_with_definitions(base_prompt, question)

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": enhanced_prompt}],
            temperature=0.1,
            max_tokens=300  # Increased to allow complete answers
        )
        
        result = {
            'answer': response.choices[0].message.content,
            'source': 'ai_procedure',
            'confidence': 'high',
            'tokens_used': response.usage.total_tokens if response.usage else 0
        }
        
        # Log token usage
        logger.info(f"📊 Procedure response tokens used: {result['tokens_used']}")
        
        return result
        
    except Exception as e:
        logger.error(f"Procedure response error: {e}")
        return get_fallback_response()

def get_general_focused_response(question, verbose=False):
    """General AI for unclear intent - COMPLETE ANSWERS"""
    try:
        search_engine = ProductionHybridVectorSearch()
        search_results = search_engine.search_with_precedence(question, top_n=3, verbose=verbose)
        
        context = build_enhanced_rule_context(search_results, max_rules=3)
        
        # REMOVED word limit
        base_prompt = f"""You are a golf rules expert at Columbia Country Club. Provide a COMPLETE answer to this golf rules question. Do not mention Columbia's Local Rules unless a local rule applies to the user's specific question.

Question: {question}

Relevant Rules Context:
{context}

CRITICAL INSTRUCTIONS:
1. Provide a COMPLETE answer with all necessary details
2. Include all relevant conditions, exceptions, and procedures
3. Be specific and accurate - do not omit important information
4. If the rule has specific requirements or limitations, include them all

Start your response appropriately:
- "According to Columbia's local rules..." (if using local rule)
- "According to the Rules of Golf, Rule X.X..." (if using official rule)

Ensure your answer is complete and would allow a golfer to proceed correctly."""

        enhanced_prompt = enhance_ai_prompt_with_definitions(base_prompt, question)

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": enhanced_prompt}],
            temperature=0.1,
            max_tokens=300  # Increased to allow complete answers
        )
        
        result = {
            'answer': response.choices[0].message.content,
            'source': 'ai_general',
            'confidence': 'medium',
            'tokens_used': response.usage.total_tokens if response.usage else 0
        }

        # Log token usage
        logger.info(f"📊 General response tokens used: {result['tokens_used']}")
        
        return result
        
    except Exception as e:
        logger.error(f"General response error: {e}")
        return get_fallback_response()

def get_fallback_response():
    """Fallback response when AI fails"""
    return {
        'answer': "I'm having trouble processing that question. Please try rephrasing or contact support.",
        'source': 'fallback',
        'confidence': 'low',
        'tokens_used': 0
    }

def calculate_template_confidence(question, template_data):
    """
    Hybrid approach: Positive signals for base match, with disqualifiers.
    Only matches when clearly asking about a Columbia-specific scenario.
    """
    question_lower = question.lower().strip()
    confidence = 0.0
    matched_keyword = None
    
    # STEP 1: Extract key concepts and check for critical concept matches
    concepts = extract_key_concepts(question_lower)
    
    # Get template name for critical concept checking
    template_name = None
    for name, data in COMMON_QUERY_TEMPLATES.items():
        if data == template_data:
            template_name = name
            break
    
    # If critical concepts match, start with base confidence
    if template_name and check_critical_concepts(concepts, template_name):
        confidence = 0.55  # Base confidence for critical concept
        matched_keyword = "critical_concepts"

    # STEP 2: Check each keyword for positive signals
    for keyword_phrase in template_data.get("keywords", []):
        keyword_lower = keyword_phrase.lower()
        
        # Skip if keyword not in question at all
        if keyword_lower not in question_lower:
            continue
            
        # For very short keywords (ob, cc), verify word boundaries
        if len(keyword_lower) <= 3:
            import re
            pattern = r'\b' + re.escape(keyword_lower) + r'\b'
            if not re.search(pattern, question_lower):
                continue  # Skip "ob" inside "obstruction"
        
        # STRONG POSITIVE SIGNALS (high confidence)
        strong_signals = [
            keyword_lower == question_lower,  # Exact match
            question_lower.startswith(keyword_lower),  # Starts with keyword
            question_lower.endswith(keyword_lower),  # Ends with keyword
            f"rule for {keyword_lower}" in question_lower,  # "what is the rule for X"
            f"rule about {keyword_lower}" in question_lower,  # "rule about X"
            f"rule if {keyword_lower}" in question_lower,  # "what's the rule if X"
            f"relief from {keyword_lower}" in question_lower,  # "relief from X"
            f"relief for {keyword_lower}" in question_lower,  # "relief for X"
            f"procedure for {keyword_lower}" in question_lower,  # "procedure for X"
            len(keyword_lower) / len(question_lower) > 0.7,  # Keyword is 70%+ of question
        ]
        
        # MODERATE POSITIVE SIGNALS (medium confidence)
        moderate_signals = [
            len(keyword_lower) / len(question_lower) > 0.4,  # Keyword is 40%+ of question
            question_lower.startswith("what") and keyword_lower in question_lower[:50],  # What + keyword early
            question_lower.startswith("how") and keyword_lower in question_lower[:50],  # How + keyword early
            question_lower.startswith("where") and keyword_lower in question_lower[:50],  # Where + keyword early
            f"hit {keyword_lower}" in question_lower,  # "ball hit purple line"
            f"went {keyword_lower}" in question_lower,  # "ball went out of bounds"
            f"into {keyword_lower}" in question_lower,  # "into maintenance facility"
            f"near {keyword_lower}" in question_lower,  # "near purple line"
        ]
        
        # Check for Columbia-specific partial matches (for things like "lost ball")
        columbia_partial_matches = {
            'lost ball': ['lost', 'ball'],
            'cart path': ['cart', 'path'],
            'green stakes': ['green', 'stakes'],
            'purple line': ['purple', 'line'],
            'maintenance': ['maintenance'],
            'water': ['water', 'hazard'],
        }
        
        partial_match = False
        for phrase, required_words in columbia_partial_matches.items():
            if all(word in keyword_lower for word in required_words):
                if all(word in question_lower for word in required_words):
                    # Check if this is asking about the rule/procedure
                    if any(asking_word in question_lower for asking_word in 
                           ['rule', 'relief', 'procedure', 'what', 'how', 'where']):
                        partial_match = True
                        break
        
        # Assign confidence based on signals
        if any(strong_signals):
            confidence = 0.8
            matched_keyword = keyword_phrase
            break
        elif any(moderate_signals):
            confidence = 0.6
            matched_keyword = keyword_phrase
            break
        elif partial_match:
            confidence = 0.5
            matched_keyword = keyword_phrase
            # Don't break - keep looking for better matches
    
    # EARLY EXIT: No match found
    if confidence == 0:
        return 0.0
    
    # DISQUALIFIERS - Complex scenarios that should go to AI
    disqualifiers = [
        # Multi-step scenarios
        'and then' in question_lower,
        'after that' in question_lower,
        'which caused' in question_lower,
        'resulted in' in question_lower,
        'subsequently' in question_lower,
        
        # Ball in motion scenarios
        'in motion' in question_lower,
        'moving ball' in question_lower,
        'while it was still' in question_lower,
        'accidentally hit' in question_lower,
        'accidentally deflected' in question_lower,
        
        # Multi-player interactions
        ('my opponent' in question_lower or 'another player' in question_lower) and 
        any(action in question_lower for action in ['hit', 'played', 'moved', 'touched']),
        
        # Complex rules scenarios
        'what happens if' in question_lower and len(question_lower.split()) > 15,
        'is it legal' in question_lower and 'then' in question_lower,
        
        # Query is too long (likely a complex scenario)
        len(question_lower.split()) > 25,
        
        # Multiple golf actions (complex scenario)
        sum(1 for action in ['hit', 'chipped', 'putted', 'drove', 'played', 'dropped', 'placed', 'lifted'] 
            if action in question_lower) > 2,
    ]
    
    if any(disqualifiers):
        return 0.0  # Disqualified - this is a complex rules scenario
    
    # TEMPLATE-SPECIFIC ADJUSTMENTS
    template_name = template_data.get('template_name', template_data.get('local_rule', ''))
    
    # For LOST BALL template - avoid penalty area confusion
    if 'lost_ball' in template_name.lower() or template_data.get('local_rule') == 'CCC-1':
        if any(indicator in question_lower for indicator in 
               ['red stake', 'yellow stake', 'penalty area', 'water hazard', 'water', 'pond', 'creek']):
            return 0.0  # This is a penalty area, not a lost ball scenario
    
    # For OUT OF BOUNDS template - avoid penalty area confusion  
    if 'out_of_bounds' in template_name.lower():
        if any(indicator in question_lower for indicator in ['red stake', 'yellow stake', 'penalty area']):
            return 0.0  # This is a penalty area, not OB
        
        # Boost for white stakes (indicate OB)
        if 'white stake' in question_lower:
            confidence = min(1.0, confidence * 1.3)
    
    # FINAL ADJUSTMENTS
    
    # Boost for explicit Columbia context
    if any(term in question_lower for term in ['columbia', 'cc', 'our course', 'here at']):
        confidence = min(1.0, confidence * 1.2)
    
    # Penalty for explicit general/USGA context
    if any(term in question_lower for term in ['usga', 'official rule', 'rules of golf']):
        confidence *= 0.3
    
    return confidence

def extract_key_concepts(text):
    """
    Extract important concepts from text for matching.
    Returns a set of key terms.
    """
    # Remove common words and extract key concepts
    stop_words = {'the', 'a', 'an', 'is', 'my', 'in', 'on', 'at', 'to', 'for', 
                  'of', 'with', 'what', 'if', 'do', 'i', 'how', 'can', 'get',
                  'from', 'when', 'where', 'rule', 'rules', 'happens'}
    
    # Special handling for compound concepts
    text = text.replace('out of bounds', 'out_of_bounds')
    text = text.replace('lost ball', 'lost_ball')
    text = text.replace('cart path', 'cart_path')
    text = text.replace('green stakes', 'green_stakes')
    text = text.replace('maintenance facility', 'maintenance_facility')
    text = text.replace('purple line', 'purple_line')
    text = text.replace('water hazard', 'water_hazard')
    
    # Extract words
    words = text.lower().split()
    
    # Keep important words and numbers
    concepts = set()
    for word in words:
        # Keep numbers (hole numbers)
        if any(char.isdigit() for char in word):
            # Extract just the number
            import re
            numbers = re.findall(r'\d+', word)
            concepts.update(numbers)
        # Keep non-stop words
        elif word not in stop_words and len(word) > 2:
            concepts.add(word)
    
    return concepts


def check_critical_concepts(matching_concepts, template_name):
    """
    Check if the matching concepts include critical identifiers for this template.
    """
    critical_concepts = {
        'clear_lost_ball': {'lost_ball', 'lost', 'ball', 'woods', 'rough', 'fescue'},
        'clear_out_of_bounds': {'out_of_bounds', 'bounds', 'fence', 'ob'},
        'water_hazard_16': {'water', '16', 'water_hazard', 'hazard'},
        'water_hazard_17': {'water', '17', 'water_hazard', 'hazard'},
        'green_stakes_cart_path': {'green_stakes', 'cart_path', '14', '17', 'path', 'behind'},
        'maintenance_facility': {'maintenance', 'maintenance_facility', 'facility'},
        'purple_line_boundary': {'purple_line', 'purple', 'line', 'boundary'},
    }
    
    # Define minimum required matches for each template
    minimum_required = {
        'clear_lost_ball': 2,  # Need at least 2 concepts (e.g., 'lost' + 'ball')
        'clear_out_of_bounds': 2,  # Need at least 2 concepts
        'water_hazard_16': 2,  # Need 'water' + '16'
        'water_hazard_17': 2,  # Need 'water' + '17'
        'green_stakes_cart_path': 3,  # Need at least 3 concepts (e.g., 'cart_path' + '14' + 'behind')
        'maintenance_facility': 1,  # 'maintenance' alone is specific enough
        'purple_line_boundary': 2,  # Need at least 2 concepts

    }

    template_critical = critical_concepts.get(template_name, set())
    min_required = minimum_required.get(template_name, 2) # Default to 2

    # Count how many critical concepts match
    matched_count = len(matching_concepts.intersection(template_critical))
    
    # Return True only if we meet the minimum threshold
    return matched_count >= min_required    

def check_common_query_with_confidence(question, confidence_threshold=0.6):
    """
    Check templates with confidence scoring.
    Uses same approach as vector search: calculate similarity, apply threshold.
    """
    best_match = None
    best_confidence = 0.0
    
    # Debug output
    debug_matches = []
    
    for template_name, template_data in COMMON_QUERY_TEMPLATES.items():
        confidence = calculate_template_confidence(question, template_data)
        
        debug_matches.append((template_name, confidence))
        
        if confidence > best_confidence:
            best_confidence = confidence
            best_match = {
                'template_name': template_name,
                'template_data': template_data,
                'confidence': confidence
            }
    
    # Debug print (like your verbose mode in vector search)
    print(f"\n🔍 Template matching for: '{question[:40]}...'")
    for name, conf in sorted(debug_matches, key=lambda x: x[1], reverse=True)[:3]:
        status = "✅" if conf >= confidence_threshold else "  "
        print(f"  {status} {name}: {conf:.3f}")
    
    # Apply threshold (like similarity < 0.1 skip in vector search)
    if best_match and best_confidence >= confidence_threshold:
        template_data = best_match['template_data'].copy()
        template_data['match_confidence'] = best_confidence
        template_data['template_name'] = best_match['template_name']
        
        # Classify confidence level (like your vector search)
        if best_confidence > 0.7:
            template_data['confidence_level'] = 'high'
        elif best_confidence > 0.4:
            template_data['confidence_level'] = 'medium'
        else:
            template_data['confidence_level'] = 'low'
            
        return template_data
    
    return None

def get_hybrid_interpretation(question, verbose=False):
    """
    ENHANCED: Two-stage approach with confidence-based routing
    """
    try:
        start_time = time.time()
        
        # STEP 1: Check templates with confidence scoring
        # Use lower threshold for initial check, will validate further
        template = check_common_query_with_confidence(question, confidence_threshold=0.5)
        
        if template:
            confidence = template.get('match_confidence', 0)
            
            if verbose:
                template_name = template.get('template_name', 'unknown')
                rule_id = template.get('local_rule', 'unknown')
                logger.info(f"📊 Template match: {template_name} (Rule {rule_id}) with confidence {confidence:.3f}")
            
            # High confidence: Use template immediately
            if confidence >= 0.75:
                if verbose:
                    logger.info(f"✅ High confidence ({confidence:.3f}) - using template")
                
                result = {
                    'answer': template["quick_response"],
                    'source': 'template',
                    'rule_id': template.get('local_rule'),
                    'confidence': 'high',
                    'confidence_score': confidence,
                    'tokens_used': 0
                }
                result['response_time'] = round(time.time() - start_time, 2)
                return result
            
            # Medium confidence: Use template but note uncertainty
            elif confidence >= 0.5:
                if verbose:
                    logger.info(f"⚠️ Medium confidence ({confidence:.3f}) - using template with note")
                
                # Add a note about confidence
                modified_answer = template["quick_response"]
                if confidence < 0.65:
                    modified_answer += "\n\n*Note: If this doesn't address your specific situation, please ask for more details.*"
                
                result = {
                    'answer': modified_answer,
                    'source': 'template_medium_confidence',
                    'rule_id': template.get('local_rule'),
                    'confidence': 'medium',
                    'confidence_score': confidence,
                    'tokens_used': 0
                }
                result['response_time'] = round(time.time() - start_time, 2)
                return result
            
            # Low confidence: Fall through to AI
            else:
                if verbose:
                    logger.info(f"❌ Low confidence ({confidence:.3f}) - routing to AI")
        
        # STEP 2: No good template match, classify intent for AI routing
        intent = classify_intent_enhanced(question)
        if verbose:
            logger.info(f"🎯 Intent classified as: {intent}")
        
        # STEP 3: Route to appropriate AI handler
        if intent == 'position':
            result = get_position_focused_response(question, verbose)
        elif intent == 'relief':
            result = get_relief_focused_response(question, verbose)
        elif intent == 'penalty':
            result = get_penalty_focused_response(question, verbose)
        elif intent == 'procedure':
            result = get_procedure_focused_response(question, verbose)
        else:
            result = get_general_focused_response(question, verbose)
        
        # Add timing and intent info
        response_time = round(time.time() - start_time, 2)
        result['response_time'] = response_time
        result['intent_detected'] = intent
        
        if verbose:
            logger.info(f"✅ AI response completed in {response_time}s")
        
        return result
                
    except Exception as e:
        logger.error(f"Hybrid interpretation error: {e}")
        return {
            'answer': "I'm experiencing a technical issue. Please try rephrasing your question.",
            'source': 'error',
            'confidence': 'none',
            'tokens_used': 0,
            'intent_detected': 'error'
        }

def enhance_ai_prompt_with_completeness_check(base_prompt, question, rule_type="general"):
    """
    Add completeness requirements to any AI prompt.
    This ensures responses include conditions and limitations.
    """
    completeness_instructions = """

ACCURACY REQUIREMENTS:
- Include ALL qualifying conditions (when the rule applies)
- Include ALL exceptions (when the rule does NOT apply)
- For relief questions: specify what types of interference qualify
- For position questions: specify all relevant boundaries and areas
- Never provide partial information that could mislead

If the rule has specific conditions for applicability, you MUST mention them.
Example: "Relief is available ONLY when [condition 1] AND [condition 2]"
"""
    
    # Add specific checks based on question type
    if "relief" in question.lower() or "obstruction" in question.lower():
        completeness_instructions += """
For relief from obstructions/conditions:
- Specify if interference must be with swing, stance, or line of play
- Note if different rules apply on putting green vs general area
- Include any "clearly unreasonable" exceptions
"""
    
    return base_prompt + completeness_instructions

def validate_response_completeness(response_text, question):
    """
    Quick validation to ensure response includes necessary components.
    Returns True if response appears complete, False if missing key elements.
    """
    response_lower = response_text.lower()
    question_lower = question.lower()
    
    # Check for rule citation
    has_rule_citation = ("rule" in response_lower and 
                        any(char.isdigit() for char in response_text))
    
    # Check for conditions/limitations based on question type
    if "relief" in question_lower or "obstruction" in question_lower:
        # Should mention when relief is available
        has_conditions = any(phrase in response_lower for phrase in [
            "only if", "only when", "must", "interference", 
            "not available", "except", "unless"
        ])
        return has_rule_citation and has_conditions
    
    return has_rule_citation

def initialize_ai_system():
    """Initialize the production hybrid system."""
    global ai_system_available, ai_error_message, simplified_system
    
    try:
        logger.info("🤖 Initializing production hybrid AI system...")
        
        # Test OpenAI connection
        test_response = client.embeddings.create(
            model="text-embedding-3-small",
            input=["test"]
        )
        
        if test_response:
            ai_system_available = True
            logger.info("✅ Production hybrid system ready - Templates + AI with Rule Scoring")
            try:
                simplified_system = create_simplified_system(
                    templates=COMMON_QUERY_TEMPLATES,
                    definitions_db=GOLF_DEFINITIONS_DATABASE,
                    search_engine=ProductionHybridVectorSearch(),
                    client=client,
                    rules_db=RULES_DATABASE,
                    local_rules=COLUMBIA_CC_LOCAL_RULES
                )
                logger.info("✅ Simplified system ready")
            except Exception as e:
                logger.error(f"⚠️ Simplified system init failed: {e}")
            return True
        else:
            raise Exception("OpenAI API test failed")
            
    except Exception as e:
        ai_system_available = False
        ai_error_message = f"AI initialization error: {str(e)}"
        logger.error(f"❌ AI initialization failed: {str(e)}")
        return False

@app.route('/api/ask', methods=['POST'])
def ask_question():
    """RESTORED: Your original sophisticated API endpoint."""
    try:
        data = request.json
        question = data.get('question', '').strip()
        
        if not question:
            return jsonify({
                'success': False,
                'error': 'Question is required'
            }), 400
        
        logger.info(f"🔍 Question: {question}")
        start_time = time.time()

        definition_id = detect_definition_query(question)
        if definition_id:
            logger.info(f"📖 Definition query detected: {definition_id}")
            response_data = create_definition_response(definition_id, question)
            if response_data:
                response_time = round(time.time() - start_time, 2)
                
                # Add standard response metadata
                response_data['response_time'] = response_time
                response_data['club_id'] = 'columbia_cc'
                response_data['ai_system'] = 'definitions_database'
                response_data['timestamp'] = datetime.now().isoformat()
                response_data['tokens_used'] = 0  # Definitions are free
                response_data['estimated_cost'] = 0.0
                response_data['intent_detected'] = 'definition'
                
                # ADD COMPREHENSIVE LOGGING (same format as other sources)
                try:
                    comprehensive_log = {
                        "timestamp": datetime.now().isoformat(),
                        "question": question,
                        "answer": response_data.get('answer', ''),
                        "source": 'definitions_database',
                        "rule_type": 'definition',
                        "confidence": response_data.get('confidence', 'high'),
                        "tokens_used": 0,
                        "estimated_cost": 0.0,
                        "response_time": response_time,
                        "intent_detected": 'definition',
                        "success": True,
                        "definition_id": definition_id  # Additional metadata for definitions
                    }
                    
                    # Log to Cloud Logging (persists forever) - SAME FORMAT AS OTHER SOURCES
                    logger.info(f"GOLF_QUERY: {json.dumps(comprehensive_log)}")
                    
                except Exception as e:
                    logger.error(f"Dashboard logging error for definitions: {e}")
                
                logger.info(f"✅ Definition response in {response_time}s")
                return jsonify(response_data)
            
        if ai_system_available:
            try:
                # Use restored sophisticated hybrid system
                if USE_SIMPLIFIED_SYSTEM and simplified_system:
                    logger.info("🆕 Using SIMPLIFIED system")
                    result = simplified_system.process_query(question, verbose=True)
                else:
                    logger.info("📦 Using ORIGINAL hybrid system")
                    result = get_hybrid_interpretation(question, verbose=True)
                response_time = round(time.time() - start_time, 2)
                
                # Determine rule type from response
                rule_type = 'local' if 'Columbia' in result['answer'] else 'official'
                
                response_data = {
                    'success': True,
                    'answer': result['answer'],
                    'question': question,
                    'club_id': 'columbia_cc',
                    'rule_type': rule_type,
                    'source': result['source'],
                    'confidence': result['confidence'],
                    'response_time': response_time,
                    'ai_system': 'production_hybrid',
                    'tokens_used': result.get('tokens_used', 0),
                    'estimated_cost': round(result.get('tokens_used', 0) * 0.00001, 4),
                    'intent_detected': result.get('intent_detected', 'unknown'),
                    'timestamp': datetime.now().isoformat()
                }
                
                if 'rules_used' in result:
                    response_data['rules_used'] = result['rules_used']
                if 'rule_id' in result:
                    response_data['rule_id'] = result['rule_id']
                
                logger.info(f"✅ Production hybrid response ({result['source']}) in {response_time}s")
                try:
                    comprehensive_log = {
                        "timestamp": datetime.now().isoformat(),
                        "question": question,
                        "answer": response_data.get('answer', ''),
                        "source": response_data.get('source', ''),
                        "rule_type": response_data.get('rule_type', ''),
                        "confidence": response_data.get('confidence', ''),
                        "tokens_used": response_data.get('tokens_used', 0),
                        "estimated_cost": response_data.get('estimated_cost', 0),
                        "response_time": response_data.get('response_time', 0),
                        "intent_detected": response_data.get('intent_detected', ''),
                        "success": response_data.get('success', False)
                    }
                    
                except Exception as e:
                    logger.error(f"Dashboard logging error: {e}")

                return jsonify(response_data)
                
            except Exception as e:
                logger.error(f"⚠️ Hybrid system error: {str(e)}")
                # Fall through to fallback
        
        # Fallback if AI unavailable
        fallback_answer = "AI system temporarily unavailable. Please try again or contact support."
        response_time = round(time.time() - start_time, 2)
        
        response_data = {
            'success': True,
            'answer': fallback_answer,
            'question': question,
            'club_id': 'columbia_cc',
            'rule_type': 'general',
            'source': 'fallback',
            'confidence': 'low',
            'response_time': response_time,
            'ai_system': 'fallback',
            'timestamp': datetime.now().isoformat()
        }
        
        logger.info(f"✅ Fallback response in {response_time}s") 
        
        return jsonify(response_data)
        
    except Exception as e:
        logger.error(f"❌ API Error: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Failed to process question: {str(e)}',
            'timestamp': datetime.now().isoformat()
        }), 500

@app.route('/api/definitions', methods=['GET'])
def get_definitions():
    """Get golf definitions - can search or get by category."""
    try:
        search_term = request.args.get('search', '').strip()
        category = request.args.get('category', '').strip()
        definition_id = request.args.get('id', '').strip()
        
        if definition_id:
            definition = get_definition_by_id(definition_id)
            if definition:
                return jsonify({
                    'success': True,
                    'definitions': [definition],
                    'total': 1
                })
            else:
                return jsonify({'success': False, 'error': 'Definition not found'}), 404
        
        elif search_term:
            results = search_definitions_by_keyword([search_term])
            definitions = [result['definition'] for result in results[:10]]
            
            return jsonify({
                'success': True,
                'definitions': definitions,
                'total': len(definitions),
                'search_term': search_term
            })
        
        elif category:
            definitions = get_definitions_by_category(category)
            return jsonify({
                'success': True,
                'definitions': definitions,
                'total': len(definitions),
                'category': category
            })
        
        else:
            return jsonify({
                'success': True,
                'definitions': GOLF_DEFINITIONS_DATABASE,
                'total': len(GOLF_DEFINITIONS_DATABASE)
            })
    
    except Exception as e:
        logger.error(f"❌ Definitions API Error: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Failed to get definitions: {str(e)}'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check showing production hybrid system status."""
    local_rules_count = len(COLUMBIA_CC_LOCAL_RULES.get('local_rules', []))
    official_rules_count = len(RULES_DATABASE)
    definitions_count = len(GOLF_DEFINITIONS_DATABASE)
    
    return jsonify({
        'status': 'healthy',
        'service': 'production_hybrid_golf_rules',
        'timestamp': datetime.now().isoformat(),
        'version': '6.1.0-production-hybrid',
        'ai_available': ai_system_available,
        'approach': 'templates_first_then_ai_with_rule_scoring',
        'deployment_optimized': True,
        'system_info': {
            'templates_loaded': len(COMMON_QUERY_TEMPLATES),
            'local_rules_loaded': local_rules_count,
            'official_rules_loaded': official_rules_count,
            'definitions_loaded': definitions_count,
            'total_rules': local_rules_count + official_rules_count
        },
        'features': {
            'template_matching': True,
            'definitions_database': True,
            'vector_search': ai_system_available,
            'rule_precedence': True,
            'local_rule_priority': True,
            'sophisticated_context': True
        }
    })

@app.route('/api/quick-questions', methods=['GET'])
def get_quick_questions():
    """Test questions covering the full system capability."""
    return jsonify({
        'success': True,
        'questions': [
            {
                'id': 'maintenance_facility',
                'text': 'Maintenance facility on #10',
                'category': 'local_rules',
                'icon': '🏗️',
                'expected_source': 'template'
            },
            {
                'id': 'purple_line_boundary',
                'text': 'Purple Line',
                'category': 'local_rules',
                'icon': '🚆',
                'expected_source': 'template'
            },
            {
                'id': 'water_hazard_17',
                'text': 'Water on #17',
                'category': 'local_rules',
                'icon': '💧',
                'expected_source': 'template'
            },
            {
                'id': 'green_stakes_cart_path',
                'text': 'Path behind #14 & #17 green',
                'category': 'local_rules',
                'icon': '🚫',
                'expected_source': 'template'
            }
        ],
        'ai_available': ai_system_available,
        'system_capabilities': {
            'handles_templates': True,
            'handles_ai_queries': ai_system_available,
            'rule_precedence': True,
            'comprehensive_database': True
        }
    })

@app.route('/api/admin/queries', methods=['GET'])
def view_all_queries():
    """Dashboard reading from Cloud Logging."""
    try:
        from google.cloud import logging as cloud_logging
        
        # Initialize Cloud Logging client
        logging_client = cloud_logging.Client()
        
        # Query for our golf queries from the last 7 days
        filter_str = '''
        resource.type="cloud_run_revision"
        textPayload:"GOLF_QUERY:"
        timestamp >= "{}T00:00:00Z"
        '''.format((datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d'))
        
        all_queries = []
        
        # Fetch logs
        for entry in logging_client.list_entries(filter_=filter_str, max_results=500):
            try:
                # Extract the JSON from the log message
                log_text = entry.payload
                if "GOLF_QUERY:" in log_text:
                    json_part = log_text.split("GOLF_QUERY:", 1)[1].strip()
                    query_data = json.loads(json_part)
                    all_queries.append(query_data)
            except:
                continue
        
        # Sort by timestamp (newest first)
        all_queries.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        
        # UPDATED SUMMARY WITH DEFINITIONS DATABASE TRACKING
        template_count = len([q for q in all_queries if 'template' in q.get('source', '')])
        ai_count = len([q for q in all_queries if 'ai' in q.get('source', '')])
        definitions_count = len([q for q in all_queries if q.get('source', '') == 'definitions_database'])

        # Create HTML dashboard with enhanced summary
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Golf Rules Query Dashboard (Cloud Logging)</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
                .question {{ max-width: 300px; word-wrap: break-word; }}
                .answer {{ max-width: 400px; word-wrap: break-word; }}
                .template {{ background-color: #e8f5e8; }}
                .ai {{ background-color: #e8f0ff; }}
                .definitions {{ background-color: #fff5e6; }}
                .error {{ background-color: #ffe8e8; }}
                .summary {{ background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
            </style>
        </head>
        <body>
            <h1>🌏️ Golf Rules Query Dashboard (Persistent)</h1>
            
            <div class="summary">
                <h3>Summary (Last 7 Days)</h3>
                <p><strong>Total Queries:</strong> {len(all_queries)}</p>
                <p><strong>Template Responses:</strong> {template_count}</p>
                <p><strong>Definitions Database:</strong> {definitions_count} ✨ NEW</p>
                <p><strong>AI Responses:</strong> {ai_count}</p>
                <p><strong>Total Cost:</strong> ${sum([q.get('estimated_cost', 0) for q in all_queries]):.4f}</p>
                <p><strong>Data Source:</strong> Cloud Logging (Persistent)</p>
            </div>
            
            <table>
                <tr>
                    <th>Time</th>
                    <th>Question</th>
                    <th>Answer</th>
                    <th>Source</th>
                    <th>Rule</th>
                    <th>Tokens</th>
                    <th>Cost</th>
                    <th>Time (s)</th>
                </tr>
        """
        
        # Add rows for each query with definitions database color coding
        for query in all_queries[:100]:  # Limit to 100 for performance
            timestamp = query.get('timestamp', 'N/A')[:16]
            question = query.get('question', 'N/A')[:100]
            answer = query.get('answer', 'N/A')[:450]
            source = query.get('source', 'unknown')
            rule_type = query.get('rule_type', 'N/A')
            tokens = query.get('tokens_used', 0)
            cost = query.get('estimated_cost', 0)
            response_time = query.get('response_time', 0)
            
            # Color code by source - ADDED DEFINITIONS DATABASE
            row_class = ""
            if 'template' in source:
                row_class = "template"
            elif source == 'definitions_database':
                row_class = "definitions"
            elif 'ai' in source:
                row_class = "ai"
            elif 'error' in source or 'fallback' in source:
                row_class = "error"
            
            html += f"""
                <tr class="{row_class}">
                    <td>{timestamp}</td>
                    <td class="question">{question}</td>
                    <td class="answer">{answer}</td>
                    <td>{source}</td>
                    <td>{rule_type}</td>
                    <td>{tokens}</td>
                    <td>${cost:.4f}</td>
                    <td>{response_time:.1f}</td>
                </tr>
            """
        
        html += """
            </table>
            
            <div style="margin-top: 20px; font-size: 12px; color: #666;">
                <p><strong>Color coding:</strong></p>
                <p><span style="background-color: #e8f5e8; padding: 2px 6px;">Green</span> = Template (Free)</p>
                <p><span style="background-color: #fff5e6; padding: 2px 6px;">Orange</span> = Definitions Database (Free) ✨ NEW</p>
                <p><span style="background-color: #e8f0ff; padding: 2px 6px;">Blue</span> = AI Response (Costs tokens)</p>
                <p><span style="background-color: #ffe8e8; padding: 2px 6px;">Red</span> = Error/Fallback</p>
                <p><strong>Data persists across container restarts!</strong></p>
            </div>
            
            <script>
                // Auto-refresh every 60 seconds
                setTimeout(() => location.reload(), 60000);
            </script>
        </body>
        </html>
        """
        
        return html
        
    except Exception as e:
        return f"""
        <html>
        <body>
            <h1>Dashboard Error</h1>
            <p>Error loading from Cloud Logging: {str(e)}</p>
            <p>Falling back to file-based logs...</p>
        </body>
        </html>
        """
        
        return html
        
    except Exception as e:
        return f"""
        <html>
        <body>
            <h1>Dashboard Error</h1>
            <p>Error loading from Cloud Logging: {str(e)}</p>
            <p>Falling back to file-based logs...</p>
        </body>
        </html>
        """

# Initialize the production hybrid system
logger.info("🚀 Starting Production Hybrid Golf Rules System...")
logger.info("📊 System includes:")
logger.info(f"  • {len(COMMON_QUERY_TEMPLATES)} comprehensive templates")
logger.info(f"  • {len(COLUMBIA_CC_LOCAL_RULES.get('local_rules', []))} Columbia CC local rules")  
logger.info(f"  • {len(RULES_DATABASE)} official golf rules")

ai_initialized = initialize_ai_system()

if ai_initialized: 
    logger.info("🎯 Production Hybrid System Ready - Templates + AI + Rule Scoring + Local Precedence!")
else:
    logger.warning("⚠️ Running in template-only mode")

        
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False, host='0.0.0.0', port=port)

# Add this at the bottom of web_api.py temporarily
#if __name__ == "__main__":
    #test_template_confidence()
