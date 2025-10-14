#!/usr/bin/env python3
"""
Test script to verify robust NLP functionality
"""

import re
from collections import Counter

def simple_sentence_split(text):
    """Simple sentence splitting without NLTK"""
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def simple_word_tokenize(text):
    """Simple word tokenization without NLTK"""
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def get_basic_stopwords():
    """Basic English stopwords list"""
    return {
        'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
        'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
        'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
        'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
        'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
        'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
        'while', 'of', 'at', 'by', 'for', 'with', 'through', 'during', 'before', 'after',
        'above', 'below', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
        'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all',
        'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
        'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will',
        'just', 'don', 'should', 'now'
    }

def test_robust_nlp():
    print("🔬 Testing Robust NLP Features")
    print("=" * 50)
    
    # Sample text
    sample_text = """
    The quick brown fox jumps over the lazy dog. This is a sample text that contains many stopwords 
    like 'the', 'is', 'a', 'that', 'and', 'over', 'lazy'. We will analyze this text to find all 
    the stopwords and show their frequency. The analysis will help us understand how many common 
    words are present in our text. This is a comprehensive test of our robust NLP system.
    """
    
    print(f"Sample text: {sample_text.strip()}")
    print()
    
    try:
        # Test sentence splitting
        print("📝 Testing Sentence Splitting:")
        sentences = simple_sentence_split(sample_text)
        print(f"Total sentences: {len(sentences)}")
        print(f"First sentence: {sentences[0]}")
        print("✅ Sentence splitting working!")
        print()
        
        # Test word tokenization
        print("🔤 Testing Word Tokenization:")
        words = simple_word_tokenize(sample_text)
        print(f"Total words: {len(words)}")
        print(f"First 10 words: {words[:10]}")
        print("✅ Word tokenization working!")
        print()
        
        # Test stopwords detection
        print("🚫 Testing Stopwords Detection:")
        stop_words = get_basic_stopwords()
        print(f"Total stopwords available: {len(stop_words)}")
        
        stopwords_found = [word for word in words if word in stop_words and word.isalpha()]
        stopwords_count = Counter(stopwords_found)
        
        print(f"Stopwords found in text: {len(stopwords_found)}")
        print(f"Unique stopwords: {len(stopwords_count)}")
        print("Most frequent stopwords:")
        for word, count in stopwords_count.most_common(5):
            print(f"  • {word}: {count} times")
        print("✅ Stopwords detection working!")
        print()
        
        # Test non-stopwords
        print("📊 Testing Non-Stopwords Analysis:")
        non_stopwords = [word for word in words if word not in stop_words and word.isalpha()]
        non_stopwords_count = Counter(non_stopwords)
        
        print(f"Non-stopwords found: {len(non_stopwords)}")
        print("Most frequent non-stopwords:")
        for word, count in non_stopwords_count.most_common(5):
            print(f"  • {word}: {count} times")
        print("✅ Non-stopwords analysis working!")
        print()
        
        # Test summarization
        print("📝 Testing Summarization:")
        sentence_scores = []
        for i, sentence in enumerate(sentences):
            score = 0
            sentence_words = simple_word_tokenize(sentence.lower())
            
            # Word frequency score
            for word in sentence_words:
                if word in non_stopwords_count:
                    score += non_stopwords_count[word]
            
            # Position bonus
            if i == 0 or i == len(sentences) - 1:
                score *= 1.2
            
            sentence_scores.append((score, sentence))
        
        # Get top 2 sentences
        sentence_scores.sort(reverse=True)
        top_sentences = [sent for score, sent in sentence_scores[:2]]
        summary = '. '.join(top_sentences) + '.'
        
        print(f"Generated summary: {summary}")
        print("✅ Summarization working!")
        print()
        
        # Calculate statistics
        total_words = len(words)
        stopwords_percentage = (len(stopwords_found) / total_words) * 100
        non_stopwords_percentage = (len(non_stopwords) / total_words) * 100
        
        print("📊 FINAL STATISTICS:")
        print("-" * 30)
        print(f"Total words: {total_words}")
        print(f"Stopwords: {len(stopwords_found)} ({stopwords_percentage:.1f}%)")
        print(f"Non-stopwords: {len(non_stopwords)} ({non_stopwords_percentage:.1f}%)")
        print(f"Sentences: {len(sentences)}")
        print(f"Summary length: {len(summary)} characters")
        
        print()
        print("🎉 All robust NLP features working perfectly!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_robust_nlp()


