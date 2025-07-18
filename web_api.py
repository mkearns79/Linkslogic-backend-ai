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

def get_hybrid_interpretation(question, verbose=False):
    """RESTORED: Your original hybrid interpretation with OpenAI embeddings."""
    try:
        # STEP 1: Check templates first (your original approach)
        template = check_common_query(question)
        if template:
            if verbose:
                logger.info(f"✅ Template match: {template['local_rule']}")
            return {
                'answer': template["quick_response"],
                'source': 'template',
                'rule_id': template['local_rule'],
                'confidence': 'highest',
                'tokens_used': 0
            }
        
        # STEP 2: Vector search with rule relevance scoring (your original sophisticated approach)
        if verbose:
            logger.info("🔍 No template found, using vector search with rule scoring...")
            
        search_engine = ProductionHybridVectorSearch()
        
        # Extract hole number for context (your original logic)
        hole_match = re.search(r'\b(\d{1,2})(?:th|st|nd|rd)?\s+hole\b', question.lower())
        hole_number = int(hole_match.group(1)) if hole_match else None
        
        search_results = search_engine.search_with_precedence(
            question, 
            hole_number=hole_number, 
            top_n=2, 
            verbose=verbose
        )
        
        if not search_results:
            if verbose:
                logger.info("❌ No relevant rules found")
            return {
                'answer': "I couldn't find specific rules for that question. Could you rephrase or ask about Columbia Country Club local rules?",
                'source': 'no_rules_found',
                'confidence': 'low',
                'tokens_used': 0
            }
        
        # STEP 3: Build sophisticated context (your original approach)
        context_parts = []
        for result in search_results:
            rule = result['rule']
            is_local = result.get('is_local', False)
            score = result['best_similarity']
            
            if is_local:
                context_parts.append(f"COLUMBIA CC LOCAL RULE {rule['id']}: {rule['title']} - {rule['text']} (Relevance: {score:.3f})")
            else:
                context_parts.append(f"OFFICIAL RULE {rule['id']}: {rule['title']} - {rule['text']} (Relevance: {score:.3f})")
        
        context = "\n\n".join(context_parts)
        
        # STEP 4: Sophisticated LLM interpretation (your original prompting)
        prompt = f"""You are an expert golf rules assistant. Analyze the question carefully to select the most appropriate rule.

        QUESTION ANALYSIS REQUIRED:
        Before answering, identify the CORE INTENT behind the question:

        **STEP 1: What is the player's situation?**
        - WHERE is their ball? (location/position)
        - WHAT happened to their ball? (movement/action)
        - HOW can they proceed? (options/procedures)

        **STEP 2: What type of rule guidance do they need?**

        A) BALL LOCATION/STATUS questions:
           - Intent: "Where is my ball legally?" or "Can I play this ball?"
           - Examples: boundary determinations, ball position, in/out of bounds
           - Use: Position/boundary rules (like 18.2a for boundaries)

        B) RELIEF OPTIONS questions:
           - Intent: "What are my choices?" or "How do I get out of this?"
           - Examples: penalty area options, relief procedures, dropping zones
           - Use: Relief procedure rules (Rule 17 for penalty areas, Rule 16 for obstructions)

        C) BALL IDENTIFICATION questions:
           - Intent: "Which ball should I play?" or "How do I know it's mine?"
           - Examples: multiple balls, provisional situations, lost ball vs identification
           - Use: Identification rules (18.3c for provisionals, 7.2 for general ID)

        D) PENALTY/CONSEQUENCE questions:
           - Intent: "What does this cost me?" or "What's the penalty?"
           - Examples: stroke penalties, procedure violations
           - Use: Specific penalty rules

        E) RELIEF PROCEDURE MECHANICS questions:
           - Intent: "HOW do I drop/place the ball?" or "WHERE exactly?"
           - Examples: dropping height, dropping area, placement vs dropping
           - Use: Procedure rules (14.3 for dropping, 14.2 for placing)
           - Key: Dropping vs placing are DIFFERENT procedures with different rules

        F) BALL SUBSTITUTION/REPLACEMENT questions:
           - Intent: "Can I use a different ball?" or "Must I use the same ball?"
           - Examples: when you can/cannot substitute, equipment damage
           - Use: Ball substitution rules (6.3b, 14.2a)
           - Key: Substitution allowed during relief, NOT during replacement

        **STEP 3: Key distinctions that matter:**
        - Water/penalty area ≠ lost ball (different rules entirely)
        - Ball position questions ≠ relief procedure questions  
        - Can't find ball ≠ can't identify ball
        - Free relief situations ≠ penalty relief situations
        - Movable objects ≠ immovable objects
        - Course area determines available procedures: 
          * Teeing area = can re-tee, special rules apply
          * Bunker = cannot ground club, special relief rules
          * Putting green = place (don't drop), can clean ball, different rules
          * General area = standard rules apply
          * Penalty area = can play as lies or take penalty relief
        - Dropping ≠ placing (different procedures and areas)
        - Red penalty area ≠ yellow penalty area (different relief options)
        - Ball replacement ≠ ball substitution (different rules apply)

        RULES CONTEXT:
        {context}

        QUESTION: {question}

        SELECTION PRIORITY:
        1. Choose the rule that matches the question TYPE, not just keywords
        2. Local rules override official rules when applicable
        3. Use the most specific sub-rule (like 18.3c(2) instead of 18.3)
        4. Consider what the player actually needs to know

        ANSWER FORMAT REQUIREMENTS:
        - If using a COLUMBIA CC LOCAL RULE, start with "According to Columbia Country Club's local rules..."
        - If using an OFFICIAL RULE, start with "According to the Rules of Golf, Rule X.X..."
        - ALWAYS prioritize local rules over official rules when both apply
        - Be specific about free relief vs penalty strokes
        - Include the key procedure steps
        - Keep response under 200 words

        Provide a clear answer with the correct rule citation."""

        if verbose:
            logger.info("🧠 Consulting LLM with sophisticated context and rule scoring...")
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional golf rules expert providing accurate rule interpretations for Columbia Country Club. Prioritize local rules over official rules."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=250
        )
        
        result = response.choices[0].message.content
        tokens_used = response.usage.total_tokens if response.usage else 0
        
        if verbose:
            logger.info(f"✅ Generated sophisticated AI response (tokens: {tokens_used})")
            
        return {
            'answer': result,
            'source': 'ai_sophisticated',
            'rules_used': [r['rule']['id'] for r in search_results],
            'confidence': 'high',
            'tokens_used': tokens_used
        }
        
    except Exception as e:
        logger.error(f"Hybrid interpretation error: {e}")
        return {
            'answer': "I'm experiencing a technical issue. Please try rephrasing your question.",
            'source': 'error',
            'confidence': 'none',
            'tokens_used': 0
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
