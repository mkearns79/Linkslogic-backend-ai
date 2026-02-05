"""
Check which OpenAI models you have access to
Run this script to see available models and test them
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def check_available_models():
    """List all available models"""
    print("🔍 Checking available OpenAI models...\n")
    
    try:
        models = client.models.list()
        
        # Filter for GPT models
        gpt_models = []
        for model in models.data:
            if 'gpt' in model.id.lower():
                gpt_models.append(model.id)
        
        print("✅ Available GPT Models:")
        for model in sorted(gpt_models):
            print(f"  - {model}")
        
        return gpt_models
    except Exception as e:
        print(f"❌ Error listing models: {e}")
        return []

def test_model(model_name, test_prompt="What is Rule 8.1d in golf?"):
    """Test a specific model"""
    print(f"\n🧪 Testing model: {model_name}")
    
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": test_prompt}],
            max_tokens=50,
            temperature=0.1
        )
        
        # Calculate cost estimate
        tokens = response.usage.total_tokens if response.usage else 0
        
        # Pricing per 1K tokens (as of Jan 2025)
        pricing = {
            "gpt-4": {"input": 0.03, "output": 0.06},
            "gpt-4-turbo": {"input": 0.01, "output": 0.03},
            "gpt-4-turbo-preview": {"input": 0.01, "output": 0.03},
            "gpt-4-1106-preview": {"input": 0.01, "output": 0.03},
            "gpt-4-0125-preview": {"input": 0.01, "output": 0.03},
            "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},
            "gpt-3.5-turbo-1106": {"input": 0.001, "output": 0.002},
            "gpt-3.5-turbo-0125": {"input": 0.0005, "output": 0.0015},
        }
        
        # Find matching pricing
        model_pricing = None
        for price_key in pricing:
            if price_key in model_name:
                model_pricing = pricing[price_key]
                break
        
        if model_pricing:
            # Rough estimate (assuming 70% input, 30% output)
            cost_per_1k = (model_pricing["input"] * 0.7 + model_pricing["output"] * 0.3)
            query_cost = (tokens / 1000) * cost_per_1k
        else:
            query_cost = 0
        
        print(f"  ✅ Success!")
        print(f"  Tokens used: {tokens}")
        print(f"  Estimated cost per query: ${query_cost:.4f}")
        print(f"  Estimated monthly cost (30 queries/day): ${query_cost * 30 * 30:.2f}")
        print(f"  Response preview: {response.choices[0].message.content[:100]}...")
        
        return True, tokens, query_cost
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False, 0, 0

def recommend_best_model(models_tested):
    """Recommend the best model based on tests"""
    print("\n📊 RECOMMENDATION:")
    print("=" * 60)
    
    if "gpt-4-turbo-preview" in models_tested or "gpt-4-0125-preview" in models_tested:
        print("✅ Use 'gpt-4-turbo-preview' or 'gpt-4-0125-preview'")
        print("   - 3x cheaper than standard GPT-4")
        print("   - Nearly identical quality for rules questions")
        print("   - Estimated monthly cost: $15-30 for your volume")
    elif "gpt-4" in models_tested:
        print("⚠️  You have GPT-4 but not the cheaper turbo versions")
        print("   Consider requesting access to gpt-4-turbo models")
        print("   Current estimated monthly cost: $45-90")
    else:
        print("⚠️  No GPT-4 models found")
        print("   You'll need to use gpt-3.5-turbo (less accurate on complex rules)")

def main():
    print("🏌️ OpenAI Model Access Checker for LinksLogic")
    print("=" * 60)
    
    # Check available models
    available_models = check_available_models()
    
    # Test specific models we want to use
    models_to_test = [
        "gpt-4-turbo-preview",
        "gpt-4-0125-preview", 
        "gpt-4-1106-preview",
        "gpt-4-turbo",
        "gpt-4",
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-0125"
    ]
    
    tested_successfully = []
    
    print("\n" + "=" * 60)
    print("Testing specific models for golf rules...")
    
    for model in models_to_test:
        if model in available_models or "preview" in model:  # Try preview models even if not listed
            success, tokens, cost = test_model(model)
            if success:
                tested_successfully.append(model)
    
    # Make recommendation
    recommend_best_model(tested_successfully)
    
    print("\n✅ Test complete!")
    print("Copy the recommended model name to use in your simplified_golf_system.py")

if __name__ == "__main__":
    main()
