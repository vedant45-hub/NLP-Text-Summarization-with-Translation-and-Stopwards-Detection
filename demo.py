#!/usr/bin/env python3
"""
Text Summarizer Pro - Demo Script
Demonstrates the core functionality without UI
"""

import re
from googletrans import Translator

def simple_summarize(text, num_sentences=3):
    """Simple extractive summarization based on sentence length and word frequency"""
    
    # Split into sentences
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Simple scoring based on sentence length and word frequency
    word_freq = {}
    words = re.findall(r'\b\w+\b', text.lower())
    
    for word in words:
        if len(word) > 3:  # Only count words longer than 3 characters
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Score sentences
    sentence_scores = []
    for sentence in sentences:
        score = 0
        words_in_sentence = re.findall(r'\b\w+\b', sentence.lower())
        for word in words_in_sentence:
            if word in word_freq:
                score += word_freq[word]
        # Add bonus for longer sentences (up to a point)
        score += min(len(sentence) / 10, 10)
        sentence_scores.append((score, sentence))
    
    # Get top sentences
    sentence_scores.sort(reverse=True)
    top_sentences = [sent for score, sent in sentence_scores[:num_sentences]]
    
    return '. '.join(top_sentences) + '.'

def translate_text(text, target_language):
    """Translate text to target language using Google Translate"""
    try:
        translator = Translator()
        result = translator.translate(text, dest=target_language)
        return result.text
    except Exception as e:
        return f"Translation error: {str(e)}"

def main():
    print("=" * 80)
    print("📝 TEXT SUMMARIZER PRO - DEMO")
    print("=" * 80)
    print()
    
    # Sample text
    sample_text = """
    Artificial Intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving".

    As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect. A quip in Tesler's Theorem says "AI is whatever hasn't been done yet." For instance, optical character recognition is frequently excluded from things considered to be AI, having become a routine technology.

    Artificial intelligence was founded as an academic discipline in 1956, and in the years since has experienced several waves of optimism, followed by disappointment and the loss of funding (known as an "AI winter"), followed by new approaches, success and renewed funding. For most of its history, AI research has been divided into sub-fields that often fail to communicate with each other. These sub-fields are based on technical considerations, such as particular goals (e.g. "robotics" or "machine learning"), the use of particular tools ("logic" or artificial neural networks), or deep philosophical differences. Sub-fields have also been based on social factors (particular institutions or the work of particular researchers).

    The traditional problems (or goals) of AI research include reasoning, knowledge representation, planning, learning, natural language processing, perception and the ability to move and manipulate objects. General intelligence is among the field's long-term goals. Approaches include statistical methods, computational intelligence, and traditional symbolic AI. Many tools are used in AI, including versions of search and mathematical optimization, artificial neural networks, and methods based on statistics, probability and economics. The AI field draws upon computer science, mathematics, psychology, linguistics, philosophy, and many other fields.
    """
    
    print("📄 ORIGINAL TEXT:")
    print("-" * 40)
    print(sample_text[:200] + "...")
    print(f"\nLength: {len(sample_text)} characters")
    print()
    
    # Generate summary
    print("🔄 Generating summary...")
    summary = simple_summarize(sample_text, 3)
    
    print("🎯 SUMMARY:")
    print("-" * 40)
    print(summary)
    print(f"\nLength: {len(summary)} characters")
    print(f"Compression ratio: {len(summary)/len(sample_text):.1%}")
    print()
    
    # Translation demo
    print("🌍 TRANSLATION DEMO:")
    print("-" * 40)
    
    languages = {
        "Hindi": "hi",
        "Marathi": "mr",
        "Spanish": "es"
    }
    
    for lang_name, lang_code in languages.items():
        print(f"\n{lang_name} Translation:")
        try:
            translated = translate_text(summary, lang_code)
            print(f"  {translated}")
        except Exception as e:
            print(f"  Error: {e}")
    
    print("\n" + "=" * 80)
    print("✅ Demo completed! Try the full UI applications:")
    print("   🌐 Web UI: streamlit run app.py")
    print("   🖥️ Desktop UI: python desktop_app.py")
    print("   🚀 Launcher: python launcher.py")
    print("=" * 80)

if __name__ == "__main__":
    main()


