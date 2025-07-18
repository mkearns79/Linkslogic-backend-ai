"""Production Golf Rules Assistant combining vector search with LLM interpretation."""
import os
import time
import json
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv
from vector_search import ClubSpecificVectorSearch

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

    "clear out_of_bounds": {
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

Exception: player gets FREE RELIEF from a ball hit into the maintenace area to the left of #10, whether the ball is found or not. The player is entitled to a free drop at the nearest point of full relief (in most cases, just to the right of the paved driveway lining the maintenance area"""
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

If your ball is in other penalty areas on 17th:
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
    }  
}

# Suppress tokenizer warnings for production
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize vector search
search_engine = ClubSpecificVectorSearch(club_id='columbia_cc')

def log_usage(tokens_used, cost, question_preview):
    """Simple usage logging for production monitoring."""
    try:
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "tokens": tokens_used,
            "cost": round(cost, 4),
            "question_preview": question_preview[:50] + "..." if len(question_preview) > 50 else question_preview
        }
        
        # Append to usage log file
        with open("usage_log.json", "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except:
        pass  # Don't let logging errors break the main function

def get_hybrid_interpretation(question, verbose=False, use_compression=True):
    """Get a golf rule interpretation using the hybrid approach."""
    try:
        # Step 1: Find relevant rules using vector search
        if verbose:
            print("\n🔍 Performing vector search...")
            search_start = time.time()
            
        import re
        hole_match = re.search(r'\b(\d{1,2})(?:th|st|nd|rd)?\s+hole\b', question.lower())
        hole_number = int(hole_match.group(1)) if hole_match else None

        search_results = search_engine.search_with_precedence(question, hole_number=hole_number, top_n=2)

        if verbose:
            search_end = time.time()
            search_time = round(search_end - search_start, 2)
            print(f"✓ Vector search completed in {search_time} seconds")
        
        # Check if we found any relevant rules
        if not search_results:
            if verbose:
                print("❌ No relevant rules found. Using LLM without rule context.")
            
            # Use LLM without specific rule context
            prompt = f"""You are an expert golf rules official. Interpret the following situation 
according to the official USGA/R&A Rules of Golf (2023 edition).

Since I couldn't find specific rules that match this query, please provide your best 
understanding of the applicable rules. If this is a specialized or uncommon situation,
please indicate that and suggest where the player might look for more definitive guidance.

Situation: {question}

Be concise but thorough. If the situation is ambiguous, explain what additional 
information would help clarify the ruling.
"""
            
            if verbose:
                print("\n🧠 Consulting LLM (without specific rule context)...")
                llm_start = time.time()
                
            # Send request to OpenAI API
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert golf rules official providing accurate rule interpretations."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=150
            )
            
            result = response.choices[0].message.content
            
            if verbose:
                llm_end = time.time()
                llm_time = round(llm_end - llm_start, 2)
                print(f"✓ LLM response received in {llm_time} seconds")
                print(f"📊 Tokens used: {response.usage.total_tokens}")
                print("💡 Source: LLM knowledge only (no specific rules matched)")
            
            # Log usage
            if response.usage:
                total_cost = (response.usage.prompt_tokens * 0.01 + response.usage.completion_tokens * 0.03) / 1000
                log_usage(response.usage.total_tokens, total_cost, question)
            
            return result
        
        # Step 2: Build context - COMPRESSED vs DETAILED
        if use_compression:
            if verbose:
                print("\n📋 Building compressed context...")
            relevant_rules_text = search_engine.get_compressed_context_for_llm(search_results, question)
            prompt_type = "compressed"
        else:
            if verbose:
                print("\n📋 Building detailed context...")
            relevant_rules_text = _build_detailed_context(search_results, verbose)
            prompt_type = "detailed"
        
        # Step 3: Create optimized prompt
        if use_compression:
            prompt = f"""Golf rules context:
{relevant_rules_text}

Question: {question}

Provide:
1. Direct answer
2. Applicable rule number  
3. Key procedure (if relief/penalty involved)

Keep response under 150 words unless situation requires detailed steps."""
        else:
            # Original detailed prompt
            prompt = f"""You are an expert golf rules official. Interpret the following situation 
according to the official USGA/R&A Rules of Golf (2023 edition).

Based on these relevant rules:

{relevant_rules_text}

For your response:
First, if possible, provide a concise answer to the question. Sometimes the user will ask "what do I do if... [then explains a situation]?" For the concise answer to this type of question, either explain the only rule-based solution, or explain that the user has options, if multiple solutions exist.  Then, if applicable,:
1. Identify the applicable rule number
2. Explain the relevant part of the rule
3. Provide a clear procedure for the golfer to follow
4. Include any free relief or penalty options

Situation: {question}

Be concise but thorough. If the situation is ambiguous, explain what additional 
information would help clarify the ruling.
"""

        if verbose:
            print(f"\n🧠 Consulting LLM ({prompt_type} context)...")
            print(f"📏 Prompt length: {len(prompt)} characters")
            llm_start = time.time()
        
        # Send request with token limiting
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert golf rules official providing accurate rule interpretations."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=200 if use_compression else None
        )
        
        result = response.choices[0].message.content
        
        if verbose:
            llm_end = time.time()
            llm_time = round(llm_end - llm_start, 2)
            print(f"✓ LLM response received in {llm_time} seconds")
            print(f"📊 Tokens used: {response.usage.total_tokens}")
            print(f"💡 Source: Vector search + LLM interpretation ({prompt_type})")
        
        # Log usage
        if response.usage:
            total_cost = (response.usage.prompt_tokens * 0.01 + response.usage.completion_tokens * 0.03) / 1000
            log_usage(response.usage.total_tokens, total_cost, question)
        
        return result
    
    except Exception as e:
        if verbose:
            print(f"\nError in get_hybrid_interpretation: {str(e)}")
            import traceback
            traceback.print_exc()
        return f"Error getting rule interpretation: {str(e)}"

def enhance_context_for_ambiguous_scenarios(search_results, query, hole_number, verbose=False):
    """
    Add clarifying context for ambiguous scenarios where location matters.
    This runs AFTER vector search but BEFORE sending to LLM.
    """
    query_lower = query.lower()
    
    # HOLE 17 WATER AMBIGUITY
    if (hole_number == 17 and 
        any(term in query_lower for term in ['water', 'pond', 'penalty', 'hazard']) and
        not any(specific in query_lower for specific in ['west of', 'east of', 'bridge', 'creek', 'stream'])):
        
        if verbose:
            print("🔍 Detected ambiguous water question on hole 17 - adding location context")
        
        # Find CCC-2 in results and enhance its context
        for result in search_results:
            if result['rule']['id'] == 'CCC-2':
                # Add location-specific guidance to the rule context
                if 'enhanced_context' not in result['rule']:
                    result['rule']['enhanced_context'] = ""
                
                result['rule']['enhanced_context'] += (
                    "\n\nLOCATION MATTERS ON HOLE 17: The dropping zone is only available "
                    "for balls in the main pond west of the footbridge. Balls in other "
                    "water areas (streams, ditches, etc.) must use standard penalty relief "
                    "under Rule 17.1 only."
                )
                
                if verbose:
                    print("   Added location context to CCC-2")
                break
    
    return search_results

def _build_detailed_context(search_results, verbose):
    """Build detailed context (original method) for comparison."""
    try:
        if verbose:
            print("\nBuilding detailed rules text...")
            
        relevant_rules_text = ""
        for i, result in enumerate(search_results):
            rule = result['rule']
            similarity = result['best_similarity']
            
            if verbose:
                print(f"Processing rule {rule['id']}...")
            
            # Add the basic rule information
            relevant_rules_text += f"Rule {rule['id']}: {rule['title']}\n{rule['text']}\n\n"
            
            # Handle conditions - different structure for local vs official rules
            if 'conditions' in rule:
                conditions = rule['conditions']
                
                if isinstance(conditions, list):
                    # Official rules format (list of dictionaries)
                    if verbose:
                        print(f"Rule has {len(conditions)} conditions (official format)...")
                        
                    relevant_rules_text += "Specific situations covered by this rule:\n"
                    for idx, cond in enumerate(conditions):
                        if isinstance(cond, dict) and 'situation' in cond and 'explanation' in cond:
                            if verbose:
                                print(f"Processing condition {idx+1}...")
                            relevant_rules_text += f"- {cond['situation']}: {cond['explanation']}\n"
                    relevant_rules_text += "\n"
                    
                elif isinstance(conditions, dict):
                    # Local rules format (nested dictionary)
                    if verbose:
                        print(f"Rule has conditions (local format)...")
                    
                    relevant_rules_text += "Specific situations covered by this rule:\n"
                    for condition_key, condition_value in conditions.items():
                        if isinstance(condition_value, str):
                            relevant_rules_text += f"- {condition_key}: {condition_value}\n"
                        elif isinstance(condition_value, list):
                            relevant_rules_text += f"- {condition_key}: {', '.join(condition_value)}\n"
                        elif isinstance(condition_value, dict):
                            # Handle nested dictionaries (like hole-specific conditions)
                            for sub_key, sub_value in condition_value.items():
                                if isinstance(sub_value, str):
                                    relevant_rules_text += f"- {condition_key} - {sub_key}: {sub_value}\n"
                    relevant_rules_text += "\n"
            
        if verbose:
                similarity_percent = round(similarity * 100, 1)
                print(f"  {i+1}. Rule {rule['id']} - {rule['title']} (Similarity: {similarity_percent}%)")

    except Exception as e:
        if verbose:
            print(f"Error building detailed context: {str(e)}")
        raise

def get_optimized_hybrid_interpretation(question, verbose=False, use_compression=True):
    """
    Optimized version that prioritizes local rules and reduces token usage.
    """
    try:
        # Step 1: Enhanced search with local rule priority
        if verbose:
            print("\n🔍 Performing optimized vector search...")
            search_start = time.time()
        
        # First, search local rules only
        local_results = search_engine.search_local_rules_only(question, top_n=2)
        
        # If strong local rule match found, use only local rules
        if local_results and local_results[0]['similarity'] > 0.7:
            if verbose:
                print(f"✅ Strong local rule match found (score: {local_results[0]['similarity']:.3f})")
                print("📋 Using LOCAL RULES ONLY to minimize tokens")
            
            # Use only the best local rule
            search_results = [local_results[0]]
            context_type = "local_only"
            
        else:
            # Use hybrid approach but limit results
            search_results = search_engine.search_with_precedence(question, top_n=2, verbose=True)

            # Extract hole number for context enhancement
            import re
            hole_match = re.search(r'\b(\d{1,2})(?:th|st|nd|rd)?\s+(?:hole|green)\b', question.lower())
            hole_number = int(hole_match.group(1)) if hole_match else None

            # Enhance context for ambiguous scenarios
            search_results = enhance_context_for_ambiguous_scenarios(search_results, question, hole_number, verbose)
            
            # Smart filtering: If first result is local and strong, remove official rules
            if (search_results and 
                search_results[0].get('is_local', False) and 
                search_results[0]['best_similarity'] > 0.6):
                
                if verbose:
                    print("📋 Local rule priority - filtering out official rules")
                search_results = [r for r in search_results if r.get('is_local', False)][:1]
                context_type = "local_priority"
            else:
                context_type = "hybrid"

        if verbose:
            search_end = time.time()
            search_time = round(search_end - search_start, 2)
            print(f"✓ Optimized search completed in {search_time} seconds")
            print(f"📊 Using {len(search_results)} rules (context: {context_type})")
        
        # Step 2: Build ultra-compressed context
        if use_compression:
            relevant_rules_text = _build_ultra_compressed_context(search_results, context_type, verbose)
        else:
            relevant_rules_text = _build_detailed_context(search_results, verbose)
        print(f"\n🔍 DEBUG: Context being sent to LLM:")
        print(f"'{relevant_rules_text}'")
        print(f"\n🔍 DEBUG: Context type: {context_type}")
        
        # Step 3: Create context-aware prompt
        prompt = _create_optimized_prompt(question, relevant_rules_text, context_type)

        if verbose:
            print(f"\n🧠 Consulting LLM (context: {context_type})...")
            print(f"📏 Prompt length: {len(prompt)} characters")
            llm_start = time.time()
        
        # Step 4: Send optimized request
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a golf rules expert for Columbia Country Club. When answering GENERAL rules questions (no specific hole mentioned), prioritize official Rules of Golf and reference rule numbers. When answering HOLE-SPECIFIC questions, prioritize Columbia's local rules. Use 'According to Columbia's local rules...' for local rules (NEVER mention CCC codes), 'According to the Rules of Golf, Rule X.X...' for official rules. Be concise but complete."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=150 if context_type == "local_only" else 200
        )
        
        result = response.choices[0].message.content
        
        if verbose:
            llm_end = time.time()
            llm_time = round(llm_end - llm_start, 2)
            print(f"✓ LLM response received in {llm_time} seconds")
            print(f"📊 Tokens used: {response.usage.total_tokens}")
            print(f"💡 Optimization: {context_type}")
        
        # Log usage with optimization info
        if response.usage:
            total_cost = (response.usage.prompt_tokens * 0.01 + response.usage.completion_tokens * 0.03) / 1000
            log_usage_optimized(response.usage.total_tokens, total_cost, question, context_type)
        
        return result
    
    except Exception as e:
        if verbose:
            print(f"\nError in get_optimized_hybrid_interpretation: {str(e)}")
        return f"Error getting rule interpretation: {str(e)}"

def _build_ultra_compressed_context(search_results, context_type, verbose=False):
    """Build ultra-compressed context optimized for local rules."""
    if not search_results:
        return "No relevant rules found."
    
    if verbose:
        print(f"\n📋 Building ultra-compressed context ({context_type})...")
    
    context_parts = []
    
    for result in search_results:
        rule = result['rule']
        is_local = result.get('is_local', False)
        
    if is_local:
        # Ultra-compressed local rule format
        rule_text = f"LOCAL RULE {rule['title']}"
    
        # Add essential rule text (first 250 chars)
        rule_text += f". {rule['text'][:250]}..."

        # ADD THIS: Include enhanced context if it exists
        if 'enhanced_context' in rule:
            rule_text += f"\n\n{rule['enhanced_context']}"

        # For "no relief" rules, emphasize the exceptions
        if any(phrase in rule['text'].lower() for phrase in ['no relief', 'not allowed', 'integral object']):
            # Extract the specific no-relief areas from the text
            text = rule['text']
            if 'behind' in text.lower() and 'green' in text.lower():
                rule_text += f" IMPORTANT: No free relief from these specific cart paths."
    
        # Add key conditions that affect relief
        if 'conditions' in rule and rule['conditions']:
            for condition in rule['conditions'][:2]:  # First 2 conditions only
                if 'no relief' in condition.get('explanation', '').lower():
                    rule_text += f" IMPORTANT: {condition['explanation'][:100]}..."
                    break
            
        else:
            # Compressed official rule format
            rule_text = f"OFFICIAL Rule {rule['id']}: {rule['title']}"
            
            # Add only first 100 chars of rule text
            text_preview = rule['text'][:100] + "..." if len(rule['text']) > 100 else rule['text']
            rule_text += f". {text_preview}"
        
        context_parts.append(rule_text)
    
    return "\n\n".join(context_parts)

def _create_optimized_prompt(question, context, context_type):
    """Create context-optimized prompts."""
    
    if context_type == "local_only":
        # Ultra-short prompt for local rules only
        return f"""Columbia Country Club Local Rule:
{context}

Q: {question}

Give direct answer with rule number and procedure. Under 100 words."""
    
    elif context_type == "local_priority":
        # Short prompt emphasizing local rule priority
        return f"""Golf Rules (Columbia Country Club local rules apply first):
    {context}

Q: {question}

If answering using a LOCAL rule, start with 'According to Columbia's local rules...' 
If answering using an OFFICIAL rule, start with 'According to the Rules of Golf, Rule X.X...'
Be concise and include key steps."""
    
    else:
        # Standard hybrid prompt
        return f"""Golf Rules Context:
{context}

Q: {question}

Provide:
1. Direct answer (start with "According to Columbia's local rules..." for LOCAL rules, or "According to the Rules of Golf, Rule X.X..." for OFFICIAL rules)
2. Rule number
3. Key procedure

Under 150 words."""

def log_usage_optimized(tokens_used, cost, question_preview, optimization_type):
    """Enhanced usage logging with optimization tracking."""
    try:
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "tokens": tokens_used,
            "cost": round(cost, 4),
            "question_preview": question_preview[:50] + "..." if len(question_preview) > 50 else question_preview,
            "optimization": optimization_type,
            "savings_estimate": _calculate_savings_estimate(optimization_type)
        }
        
        with open("usage_log_optimized.json", "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except:
        pass

def _calculate_savings_estimate(optimization_type):
    """Estimate token savings from optimization."""
    savings_map = {
        "local_only": "60-70%",  # Using only 1 local rule vs 2+ rules
        "local_priority": "40-50%",  # Filtering out official rules
        "hybrid": "20-30%",  # Standard compression
        "detailed": "0%"  # No optimization
    }
    return savings_map.get(optimization_type, "unknown")

# Common query templates for ultra-fast responses
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

    "clear out_of_bounds": {
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

Exception: player gets FREE RELIEF from a ball hit into the maintenace area to the left of #10, whether the ball is found or not. The player is entitled to a free drop at the nearest point of full relief (in most cases, just to the right of the paved driveway lining the maintenance area"""
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

If your ball is in other penalty areas on 17th:
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
    }  
}

def check_common_query(question):
    """Check if this is a common query that can use template response."""
    question_lower = question.lower()
    
     # Check each template for exact keyword matches
    for template_name, template_data in COMMON_QUERY_TEMPLATES.items():
        for keyword_phrase in template_data["keywords"]:
            if keyword_phrase in question_lower:
                return template_data
    
    # Default: Let search handle everything else
    return None

def get_ultra_fast_interpretation(question, verbose=False):
    """Ultra-fast response for common queries using templates."""
    
    # Check for common query patterns
    template = check_common_query(question)
    
    if template:
        if verbose:
            print(f"✅ Common query detected - using template response")
            print(f"📊 Tokens saved: ~200-300 (template vs full LLM)")
            print(f"💡 Local rule: {template['local_rule']}")
        
        # Log the ultra-fast usage
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "tokens": 0,  # Template uses no LLM tokens
            "cost": 0,
            "question_preview": question[:50],
            "optimization": "template",
            "template_used": template["local_rule"]
        }
        
        try:
            with open("usage_log_optimized.json", "a") as f:
                f.write(json.dumps(log_entry) + "\n")
        except:
            pass
        
        return template["quick_response"]
    
    else:

         # Fall back to optimized search

         # In get_ultra_fast_interpretation, add:
        print(f"\n🔍 DEBUG: Search results for '{question}':")
        search_results = search_engine.search_with_precedence(question, top_n=3)
        for i, result in enumerate(search_results):
            rule_id = result['rule']['id']
            title = result['rule']['title']
            is_local = result.get('is_local', False)
            score = result.get('best_similarity', 0)
            print(f"  {i+1}. {'LOCAL' if is_local else 'OFFICIAL'} - {rule_id}: {title} (score: {score:.3f})")
    
        return get_optimized_hybrid_interpretation(question, verbose, use_compression=True)

# Replace main() function to use optimizations
def main_optimized():
    """Optimized main function with multiple efficiency modes."""
    print("🏌️ Golf Rules Assistant - Ultra-Optimized Mode")
    print("="*50)
    print("🚀 Features:")
    print("  • Local rule priority (60-70% token savings)")
    print("  • Common query templates (100% LLM savings)")
    print("  • Smart context filtering")
    print("="*50)
    
    while True:
        try:
            question = input("\n❓ Enter your golf rules question (or 'quit' to exit): ").strip()
            
            if question.lower() in ['quit', 'exit', 'q']:
                print("👋 Thanks for using Golf Rules Assistant!")
                break
                
            if not question:
                print("Please enter a question.")
                continue
            
            print("\n🔍 Looking up rules...")
            
            # Use ultra-fast interpretation (templates + optimized search)
            result = get_ultra_fast_interpretation(question, verbose=False)
            
            print(f"\n📋 **Answer:**")
            print(result)
            print("\n" + "-"*50)
            
        except KeyboardInterrupt:
            print("\n👋 Thanks for using Golf Rules Assistant!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try rephrasing your question.")

def compare_compression(question):
    """Compare compressed vs detailed versions for testing."""
    print(f"🧪 TESTING COMPRESSION FOR: {question}\n")
    
    print("🔥 COMPRESSED VERSION:")
    print("-" * 30)
    compressed_result = get_hybrid_interpretation(question, verbose=True, use_compression=True)
    
    print("\n" + "🐌 DETAILED VERSION:")
    print("-" * 30)  
    detailed_result = get_hybrid_interpretation(question, verbose=True, use_compression=False)
    
    print(f"\n📝 RESPONSE COMPARISON:")
    print(f"Compressed: {compressed_result[:100]}...")
    print(f"Detailed: {detailed_result[:100]}...")

def main():
    """Run the production golf rules assistant."""
    print("🏌️ Golf Rules Assistant - Production Mode")
    print("="*50)
    print("Optimized for cost efficiency with vector search + LLM")
    print("Compression enabled for 65-70% cost savings")
    print("="*50)
    
    while True:
        try:
            # Get user input
            question = input("\n❓ Enter your golf rules question (or 'quit' to exit): ").strip()
            
            if question.lower() in ['quit', 'exit', 'q']:
                print("👋 Thanks for using Golf Rules Assistant!")
                break
                
            if not question:
                print("Please enter a question.")
                continue
            
            # Get interpretation (compressed by default, minimal output)
            print("\n🔍 Looking up rules...")
            result = get_hybrid_interpretation(question, verbose=True, use_compression=False)
            
            print(f"\n📋 **Answer:**")
            print(result)
            print("\n" + "-"*50)
            
        except KeyboardInterrupt:
            print("\n👋 Thanks for using Golf Rules Assistant!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try rephrasing your question.")

# Development/Testing functions
def run_test_suite():
    """Run comprehensive tests for development."""
    test_questions = [
        "My ball is in casual water in a bunker, what are my options?",
        "During a tournament, my ball hit another player's ball that was at rest on the green. Both balls moved. What happens next and are there any penalties?",
        "In match play, I accidentally marked my opponent's ball on the green. What do we do?"
    ]
    
    print("🧪 RUNNING COMPRESSION TEST SUITE")
    print("="*60)
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n🔬 TEST {i}: {question}")
        print("-"*60)
        compare_compression(question)
        print("\n" + "="*60)
    
    print("🏁 ALL TESTS COMPLETED!")

if __name__ == "__main__":
    # Production mode by default
    # Uncomment the line below to run tests instead:
    # run_test_suite()
    
    main_optimized()
