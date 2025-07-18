#!/usr/bin/env python3
"""
Automatic patch script to fix the local rules prioritization issue
in golf_rules_hybrid.py
"""

import os
import re
import shutil
from datetime import datetime

def backup_file(file_path):
    """Create a backup of the original file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{file_path}_backup_{timestamp}"
    shutil.copy2(file_path, backup_path)
    print(f"✅ Backup created: {backup_path}")
    return backup_path

def apply_context_fix(content):
    """Apply the fix to _build_ultra_compressed_context function."""
    
    # Find the function definition
    pattern = r'def _build_ultra_compressed_context\(search_results, context_type, verbose=False\):(.*?)(?=def |\Z)'
    
    # New function implementation
    new_function = '''def _build_ultra_compressed_context(search_results, context_type, verbose=False):
    """Build ultra-compressed context optimized for local rules - FIXED VERSION."""
    if not search_results:
        return "No relevant rules found."
    
    if verbose:
        print(f"\\n📋 Building ultra-compressed context ({context_type})...")
    
    context_parts = []
    
    for result in search_results:
        rule = result['rule']
        is_local = result.get('is_local', False)
        
        if is_local:
            # ENHANCED local rule format with key information preserved
            rule_text = f"COLUMBIA CC LOCAL RULE - {rule['title']}: "
            
            # For maintenance facility, preserve the "FREE RELIEF" information
            if 'maintenance' in rule['title'].lower():
                rule_text += "The maintenance facility (holes 9 & 10) including buildings, storage tanks, sheds, paved areas, and equipment is treated as one immovable obstruction. FREE RELIEF under Rule 16.1 - drop within one club-length of nearest point of complete relief, not nearer hole."
            
            # For other local rules, include more complete text
            else:
                rule_text += rule['text'][:400] + ("..." if len(rule['text']) > 400 else "")
            
            # Add enhanced context if it exists
            if 'enhanced_context' in rule:
                rule_text += f" ADDITIONAL: {rule['enhanced_context']}"
        
        else:
            # Compressed official rule format
            rule_text = f"OFFICIAL Rule {rule['id']}: {rule['title']}"
            text_preview = rule['text'][:200] + "..." if len(rule['text']) > 200 else rule['text']
            rule_text += f". {text_preview}"
        
        context_parts.append(rule_text)
    
    return "\\n\\n".join(context_parts)

'''
    
    # Replace the function
    new_content = re.sub(pattern, new_function, content, flags=re.DOTALL)
    
    if new_content == content:
        print("⚠️  Could not find _build_ultra_compressed_context function to replace")
        return content, False
    else:
        print("✅ Fixed _build_ultra_compressed_context function")
        return new_content, True

def apply_prompt_fix(content):
    """Apply the fix to _create_optimized_prompt function."""
    
    # Find the function definition
    pattern = r'def _create_optimized_prompt\(question, context, context_type\):(.*?)(?=def |\Z)'
    
    # New function implementation
    new_function = '''def _create_optimized_prompt(question, context, context_type):
    """Create context-optimized prompts - ENHANCED VERSION."""
    
    if context_type == "local_only" or context_type == "local_priority":
        # Enhanced prompt for local rules
        return f"""You are a golf rules expert for Columbia Country Club.

RULES CONTEXT:
{context}

QUESTION: {question}

INSTRUCTIONS:
- If the context shows a COLUMBIA CC LOCAL RULE, start your answer with "According to Columbia Country Club's local rules..."
- If FREE RELIEF is mentioned in the context, emphasize that in your answer
- If PENALTY or NO RELIEF is mentioned, emphasize that instead
- Be specific about the procedure (where to drop, penalty strokes, etc.)
- Keep under 150 words

ANSWER:"""
    
    else:
        # Standard hybrid prompt
        return f"""You are a golf rules expert. Use these rules to answer the question.

RULES:
{context}

QUESTION: {question}

If using a LOCAL rule, start with "According to Columbia Country Club's local rules..."
If using an OFFICIAL rule, start with "According to the Rules of Golf, Rule X.X..."

Provide clear procedure and mention any free relief or penalties.

ANSWER:"""

'''
    
    # Replace the function
    new_content = re.sub(pattern, new_function, content, flags=re.DOTALL)
    
    if new_content == content:
        print("⚠️  Could not find _create_optimized_prompt function to replace")
        return content, False
    else:
        print("✅ Fixed _create_optimized_prompt function")
        return new_content, True

def main():
    """Main patch application function."""
    
    file_path = "golf_rules_hybrid.py"
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found!")
        print("Make sure you're in the correct directory:")
        print("cd /Users/michaelkearns/Documents/golf_rules_assistant/linkslogic-backend")
        return False
    
    print(f"🔧 Applying patches to {file_path}...")
    
    # Create backup
    backup_path = backup_file(file_path)
    
    # Read the file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False
    
    # Apply fixes
    fixes_applied = 0
    
    # Fix 1: Context building function
    content, success = apply_context_fix(content)
    if success:
        fixes_applied += 1
    
    # Fix 2: Prompt creation function  
    content, success = apply_prompt_fix(content)
    if success:
        fixes_applied += 1
    
    # Write the patched file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Patches applied successfully!")
        print(f"📊 {fixes_applied}/2 functions updated")
        
        if fixes_applied == 2:
            print("\n🎯 All fixes applied! Now test the system:")
            print("python3 -c \"from golf_rules_hybrid import get_hybrid_interpretation; result = get_hybrid_interpretation('I hit my ball into the maintenance facility on hole 10', verbose=True); print('\\n=== RESULT ==='); print(result)\"")
        else:
            print(f"\n⚠️  Only {fixes_applied}/2 fixes applied. Manual review may be needed.")
            
        return True
        
    except Exception as e:
        print(f"❌ Error writing patched file: {e}")
        print(f"Restoring from backup: {backup_path}")
        shutil.copy2(backup_path, file_path)
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("\n✅ Patch complete! Ready to test and deploy.")
    else:
        print("\n❌ Patch failed. Check the backup file if needed.")
