#!/usr/bin/env python3
"""
Test script to verify translation functionality
"""

from deep_translator import GoogleTranslator

def test_translation():
    print("🌍 Testing Translation Functionality")
    print("=" * 50)
    
    # Test text
    test_text = "Hello, this is a test of the translation functionality. How are you today?"
    
    print(f"Original text: {test_text}")
    print()
    
    # Test different languages
    languages = {
        "Hindi": "hi",
        "Marathi": "mr",
        "Spanish": "es",
        "French": "fr",
        "German": "de"
    }
    
    for lang_name, lang_code in languages.items():
        try:
            print(f"Translating to {lang_name}...")
            translator = GoogleTranslator(source='auto', target=lang_code)
            result = translator.translate(test_text)
            print(f"✅ {lang_name}: {result}")
            print()
        except Exception as e:
            print(f"❌ {lang_name}: Error - {str(e)}")
            print()
    
    print("🎉 Translation test completed!")

if __name__ == "__main__":
    test_translation()


