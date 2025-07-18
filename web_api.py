from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import time
import os
import re
import math
from datetime import datetime
import logging
from openai import OpenAI
from dotenv import load_dotenv

# Import your existing comprehensive databases
from golf_rules_data import RULES_DATABASE
from columbia_cc_local_rules_db import COLUMBIA_CC_LOCAL_RULES

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

# RESTORED: Your Complete Template System (from your original system)
COMMON_QUERY_TEMPLATES = {
    "clear_lost_ball": {
        "keywords": ["lost my ball in the woods", "lost my ball in the rough", "can't find my ball in the woods", "lost ball in trees", "lost ball in the fescue"],
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
        "keywords": ["out of bounds", "over the fence", "ob"],
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
        "quick_response": """On the 16th hole at Columbia CC, you have EXTRA relief options:

If your ball goes in the water/penalty area:
• Standard relief under Rule 17.1 (1 penalty stroke), OR
• Use the special DROPPING ZONE near the 16th green (1 penalty stroke)

The dropping zone is often the better choice as it gives you a good angle to the pin without having to go way back or play from a difficult angle."""
    },
    
    "water_hazard_17": {
        "keywords": ["water on seventeen", "water on 17", "17th hole water", "pond on hole seventeen", "17th water", "drop zone on seventeen"],
        "local_rule": "CCC-2", 
        "quick_response": """On the 17th hole at Columbia CC:

If your ball goes in the POND (west of the footbridge):
• Standard relief under Rule 17.1 (1 penalty stroke), OR  
• Use the special DROPPING ZONE near the 17th green (1 penalty stroke)

If your ball is in other penalty areas on 17th, including on the cart bridge:
• Standard relief under Rule 17.1 only

The dropping zone is only available for the main pond area, not other water hazards on the hole."""
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
        "keywords": ["maintenance", "building", "facility", "shed", "equipment", "roof"],
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
        "green stakes cart path", "stakes behind green", "marked cart path"
    ],
    "local_rule": "CCC-4",
    "quick_response": """According to Columbia Country Club's local rules, certain cart paths are designated as INTEGRAL OBJECTS from which NO FREE RELIEF is available:

AFFECTED AREAS:
• Cart path sections behind 14th green marked by green stakes
• Cart path sections behind 17th green marked by green stakes  
• Unpaved road behind 12th green

NO FREE RELIEF AVAILABLE - Your options:
- Play the ball as it lies if possible
- Declare the ball unplayable under Rule 19 (1 penalty stroke)
  - Drop within two club-lengths, not nearer hole
  - Drop on line from hole through ball, going back as far as desired
  - Return to previous spot where you played

Note: All other cart paths on the course DO provide free relief under Rule 16.1 - only these specifically marked areas are integral objects."""
    },

    "purple_line_boundary": {
    "keywords": [
        "purple line out of bounds", "purple line boundary", "ball crossed purple line", "ball over purple line", "ball over the train tracks",
        "purple line construction", "construction boundary", "ball in tunnel", "ball past purple line",
        "purple line area", "construction area boundary", "ball beyond purple line", "crossed construction line",
        "purple boundary line", "construction zone boundary", "ball in construction area",
        "over the purple line", "past the purple line", "through purple line", "across purple line", "across the train tracks"
    ],
    "local_rule": "CCC-6",
    "quick_response": """According to Columbia Country Club's local rules, the Purple Line construction fence is a BOUNDARY, and any ball that crosses this boundary is OUT OF BOUNDS.

IMPORTANT BOUNDARY RULE:
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
        
        # Only process first 50 official rules to prevent API overload
        # You can increase this gradually
        for rule in RULES_DATABASE[:50]:
            processed_rules.append({
                'id': rule['id'],
                'title': rule['title'],
                'text': rule['text'],
                'keywords': rule.get('keywords', []),
                'is_local': False,
                'priority': 2,
                'search_text': f"{rule['title']} {rule['text']} {' '.join(rule.get('keywords', []))}"
            })
            
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
            
            return results[:top_n]
            
        except Exception as e:
            logger.error(f"Search error: {e}")
            return []

def check_common_query(question):
    """RESTORED: Your original template checking function."""
    question_lower = question.lower()
    
    for template_name, template_data in COMMON_QUERY_TEMPLATES.items():
        for keyword_phrase in template_data["keywords"]:
            if keyword_phrase in question_lower:
                return template_data
    
    return None

def classify_intent_minimal(question):
    """Lightweight intent classification - ~$0.005 per query"""
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{
                "role": "user", 
                "content": f"""Golf question type?
A) Ball location/position (where is ball, can I play it, is it in bounds)
B) Relief options/procedures (what are my options, how do I get relief)
C) Other

Question: {question}
Answer:"""
            }],
            temperature=0.1,
            max_tokens=10
        )
        
        result = response.choices[0].message.content.strip()
        if result.startswith('A'):
            return 'position'
        elif result.startswith('B'):
            return 'relief'
        else:
            return 'other'
            
    except Exception as e:
        logger.error(f"Intent classification error: {e}")
        return 'other'  # Fallback to current system

def get_position_focused_response(question, verbose=False):
    """Focused AI for position/boundary questions with local rules context"""
    try:
        # Get local rules context
        search_engine = ClubSpecificVectorSearch(club_id='columbia_cc')
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
        
        # Build context including local rules
        context_parts = []
        for result in search_results[:3]:
            rule = result['rule']
            is_local = result.get('is_local', False)
            if is_local:
                context_parts.append(f"COLUMBIA CC LOCAL RULE {rule['id']}: {rule['title']} - {rule['text'][:150]}...")
            else:
                context_parts.append(f"Official Rule {rule['id']}: {rule['title'][:80]}...")
        
        context = "\n".join(context_parts) if context_parts else "General golf rules apply."

        prompt = f"""Golf rules expert: Determine ball position/status at Columbia Country Club.

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
If official rule, start with "According to the Rules of Golf, Rule X.X..."
Max 85 words."""

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=125
        )
        
        return {
            'answer': response.choices[0].message.content,
            'source': 'ai_position',
            'confidence': 'high',
            'tokens_used': response.usage.total_tokens if response.usage else 0
        }
        
    except Exception as e:
        logger.error(f"Position response error: {e}")
        return get_fallback_response()

def get_relief_focused_response(question, verbose=False):
    """Focused AI for relief/procedure questions with enhanced local rules context"""
    try:
        # Get local rules context with more results for comprehensive relief options
        search_engine = ProductionHybridVectorSearch()
        search_results = search_engine.search_with_precedence(question, top_n=3, verbose=verbose)
        
        # ENHANCED DEBUG LOGGING (same as position function)
        if verbose:
            logger.info(f"🔍 Relief search results for '{question}':")
            for i, result in enumerate(search_results):
                rule_id = result['rule']['id']
                title = result['rule']['title']
                is_local = result.get('is_local', False)
                score = result.get('best_similarity', 0)
                logger.info(f"  {i+1}. {'LOCAL' if is_local else 'OFFICIAL'} - {rule_id}: {title} (score: {score:.3f})")
        
        # Build enhanced context with more local rule detail
        context_parts = []
        for result in search_results[:3]:  # Use top 3 instead of 2
            rule = result['rule']
            is_local = result.get('is_local', False)
            if is_local:
                # More detailed local rule context (increased from 60 to 200 chars)
                context_parts.append(f"COLUMBIA CC LOCAL RULE {rule['id']}: {rule['title']} - {rule['text'][:200]}...")
            else:
                context_parts.append(f"Official Rule {rule['id']}: {rule['title'][:80]}...")
        
        context = "\n".join(context_parts) if context_parts else "No specific local rules found."
        
        prompt = f"""Golf rules expert: Provide relief options/procedures at Columbia Country Club.

Question: {question}

Relevant Rules:
{context}

Focus on: 
- Columbia CC local relief options (special procedures, dropping zones, free vs penalty relief)
- Local rule exceptions (integral objects, no-relief areas, boundary definitions)
- Relief procedures (where to drop, how many penalty strokes, measurement procedures)
- Local vs official relief options (always prioritize local when available)
- Hole-specific relief (dropping zones, special areas, course-specific rules)
- Equipment/obstruction relief (cart paths, maintenance areas, construction fences, construction zones)

Key distinctions:
- Local relief options override official rules when applicable
- Free relief vs penalty relief situations
- Dropping vs placing procedures
- Course area-specific relief rules

If COLUMBIA CC LOCAL RULE applies, start with "According to Columbia's local rules..."
If official rule, start with "According to the Rules of Golf, Rule X.X..."
Max 85 words."""

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=125
        )
        
        return {
            'answer': response.choices[0].message.content,
            'source': 'ai_relief',
            'confidence': 'high',
            'tokens_used': response.usage.total_tokens if response.usage else 0
        }
        
    except Exception as e:
        logger.error(f"Relief response error: {e}")
        return get_fallback_response()

def get_general_focused_response(question, verbose=False):
    """General AI for unclear intent - uses simplified enhanced prompt"""
    try:
        # Get context from vector search (keep current top 2)
        search_engine = ProductionHybridVectorSearch()
        search_results = search_engine.search_with_precedence(question, top_n=2, verbose=verbose)
        
        # Build context (slight enhancement - 100 chars vs 60)
        context_parts = []
        for result in search_results[:2]:
            rule = result['rule']
            is_local = result.get('is_local', False)
            if is_local:
                context_parts.append(f"COLUMBIA CC LOCAL RULE {rule['id']}: {rule['title']} - {rule['text'][:100]}...")
            else:
                context_parts.append(f"Official Rule {rule['id']}: {rule['title'][:80]}...")
        
        context = "\n".join(context_parts) if context_parts else "General golf rules apply."
        
        prompt = f"""Golf rules expert: Answer golf question at Columbia Country Club.

Question: {question}

Relevant Rules:
{context}

Determine if this is about: ball position, relief procedures, equipment, or rule clarification.
Focus on: Local rule priority, Columbia-specific procedures, official rule application.

If COLUMBIA CC LOCAL RULE applies, start with "According to Columbia's local rules..."
If official rule, start with "According to the Rules of Golf, Rule X.X..."
Max 85 words."""

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=125
        )
        
        return {
            'answer': response.choices[0].message.content,
            'source': 'ai_general',
            'confidence': 'medium',
            'tokens_used': response.usage.total_tokens if response.usage else 0
        }
        
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

def get_hybrid_interpretation(question, verbose=False):
    """Two-stage approach: Intent classification + focused AI"""
    try:
        start_time = time.time()
        
        # STEP 1: Lightweight intent classification (always runs)
        intent = classify_intent_minimal(question)
        if verbose:
            logger.info(f"🎯 Intent classified as: {intent}")
        
        # STEP 2: Route based on intent
        if intent == 'position':
            # Position questions: Skip templates, go straight to focused AI
            result = get_position_focused_response(question, verbose)
            
        elif intent == 'relief':
            # Relief questions: Check templates first, then AI if needed
            template = check_common_query(question)
            if template:
                if verbose:
                    logger.info(f"✅ Template match: {template['local_rule']}")
                result = {
                    'answer': template["quick_response"],
                    'source': 'template',
                    'rule_id': template['local_rule'],
                    'confidence': 'highest',
                    'tokens_used': 0
                }
            else:
                result = get_relief_focused_response(question, verbose)
                
        else:  # 'other'
            # Unclear intent: Fall back to current system
            template = check_common_query(question)
            if template:
                if verbose:
                    logger.info(f"✅ Template match for unclear intent: {template['local_rule']}")
                result = {
                    'answer': template["quick_response"],
                    'source': 'template',
                    'rule_id': template['local_rule'],
                    'confidence': 'highest',
                    'tokens_used': 0
                }
            else:
                result = get_general_focused_response(question, verbose)
        
        # Add timing and intent info to result
        response_time = round(time.time() - start_time, 2)
        result['response_time'] = response_time
        result['intent_detected'] = intent
        
        # Enhanced logging for cost tracking
        if verbose:
            logger.info(f"✅ Response completed: Intent={intent}, Source={result['source']}, Tokens={result.get('tokens_used', 0)}, Time={response_time}s")
        
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

def initialize_ai_system():
    """Initialize the production hybrid system."""
    global ai_system_available, ai_error_message
    
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
        
        if ai_system_available:
            try:
                # Use restored sophisticated hybrid system
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

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check showing production hybrid system status."""
    local_rules_count = len(COLUMBIA_CC_LOCAL_RULES.get('local_rules', []))
    official_rules_count = len(RULES_DATABASE)
    
    return jsonify({
        'status': 'healthy',
        'service': 'production_hybrid_golf_rules',
        'timestamp': datetime.now().isoformat(),
        'version': '6.0.0-production-hybrid',
        'ai_available': ai_system_available,
        'approach': 'templates_first_then_ai_with_rule_scoring',
        'deployment_optimized': True,
        'system_info': {
            'templates_loaded': len(COMMON_QUERY_TEMPLATES),
            'local_rules_loaded': local_rules_count,
            'official_rules_loaded': official_rules_count,
            'total_rules': local_rules_count + official_rules_count
        },
        'features': {
            'template_matching': True,
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
                'id': 'maintenance_template',
                'text': 'Ball near maintenance building on hole 10',
                'category': 'local_rules',
                'icon': '🏗️',
                'expected_source': 'template',
                'expected_rule': 'CCC-7'
            },
            {
                'id': 'embedded_ball_ai',
                'text': 'My ball is embedded in the fairway',
                'category': 'official_rules',
                'icon': '⛳',
                'expected_source': 'ai_sophisticated',
                'expected_rule': '16.3'
            },
            {
                'id': 'water_17_template',
                'text': 'Ball in water on hole 17',
                'category': 'local_rules',
                'icon': '💧',
                'expected_source': 'template',
                'expected_rule': 'CCC-2'
            },
            {
                'id': 'unplayable_ball_ai',
                'text': 'I want to declare my ball unplayable',
                'category': 'official_rules',
                'icon': '🚫',
                'expected_source': 'ai_sophisticated',
                'expected_rule': '19.2'
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
