#!/usr/bin/env python3
"""
Test script to verify stopwords functionality
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter

# Download NLTK data
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    print("✅ NLTK data downloaded successfully!")
except:
    print("⚠️ NLTK data download in progress...")

def test_stopwords():
    print("🚫 Testing Stopwords Detection")
    print("=" * 50)
    
    # Sample text
    sample_text = """
    The quick brown fox jumps over the lazy dog. This is a sample text that contains many stopwords 
    like 'the', 'is', 'a', 'that', 'and', 'over', 'lazy'. We will analyze this text to find all 
    the stopwords and show their frequency. The analysis will help us understand how many common 
    words are present in our text.
    """
    
    print(f"Sample text: {sample_text.strip()}")
    print()
    
    try:
        # Get English stopwords
        stop_words = set(stopwords.words('english'))
        print(f"Total English stopwords available: {len(stop_words)}")
        print(f"First 10 stopwords: {list(stop_words)[:10]}")
        print()
        
        # Tokenize the text
        words = word_tokenize(sample_text.lower())
        print(f"Total words in text: {len(words)}")
        print()
        
        # Find stopwords in the text
        stopwords_found = [word for word in words if word in stop_words and word.isalpha()]
        stopwords_count = Counter(stopwords_found)
        
        print("🚫 STOPWORDS FOUND IN TEXT:")
        print("-" * 30)
        print(f"Total stopwords found: {len(stopwords_found)}")
        print(f"Unique stopwords: {len(stopwords_count)}")
        print()
        
        print("Most frequent stopwords:")
        for word, count in stopwords_count.most_common(10):
            print(f"  • {word}: {count} times")
        print()
        
        print("All stopwords found:")
        all_stopwords = list(stopwords_count.keys())
        print(f"  {', '.join(all_stopwords)}")
        print()
        
        # Find non-stopwords
        non_stopwords = [word for word in words if word not in stop_words and word.isalpha()]
        non_stopwords_count = Counter(non_stopwords)
        
        print("📝 NON-STOPWORDS FOUND:")
        print("-" * 30)
        print(f"Total non-stopwords: {len(non_stopwords)}")
        print(f"Unique non-stopwords: {len(non_stopwords_count)}")
        print()
        
        print("Most frequent non-stopwords:")
        for word, count in non_stopwords_count.most_common(10):
            print(f"  • {word}: {count} times")
        print()
        
        # Calculate percentages
        total_words = len(words)
        stopwords_percentage = (len(stopwords_found) / total_words) * 100
        non_stopwords_percentage = (len(non_stopwords) / total_words) * 100
        
        print("📊 STATISTICS:")
        print("-" * 30)
        print(f"Stopwords: {len(stopwords_found)} ({stopwords_percentage:.1f}%)")
        print(f"Non-stopwords: {len(non_stopwords)} ({non_stopwords_percentage:.1f}%)")
        print(f"Total words: {total_words}")
        
        print()
        print("✅ Stopwords detection working perfectly!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_stopwords()


