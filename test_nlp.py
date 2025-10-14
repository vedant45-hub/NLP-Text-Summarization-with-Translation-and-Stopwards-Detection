#!/usr/bin/env python3
"""
Test script to verify NLP functionality
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk.tag import pos_tag
from textblob import TextBlob
from collections import Counter

# Download NLTK data
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
    print("✅ NLTK data downloaded successfully!")
except:
    print("⚠️ NLTK data download in progress...")

def test_nlp_features():
    print("🔬 Testing Advanced NLP Features")
    print("=" * 50)
    
    # Sample text
    sample_text = """
    Artificial Intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. 
    Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. 
    Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving".
    As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect.
    """
    
    print(f"Sample text: {sample_text[:100]}...")
    print()
    
    # Test stopwords extraction
    print("🚫 Testing Stopwords Extraction:")
    try:
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(sample_text.lower())
        stopwords_found = [word for word in words if word in stop_words and word.isalpha()]
        stopwords_count = Counter(stopwords_found)
        
        print(f"Total stopwords found: {len(stopwords_found)}")
        print(f"Most common stopwords: {stopwords_count.most_common(5)}")
        print("✅ Stopwords extraction working!")
    except Exception as e:
        print(f"❌ Stopwords extraction failed: {e}")
    
    print()
    
    # Test sentiment analysis
    print("😊 Testing Sentiment Analysis:")
    try:
        blob = TextBlob(sample_text)
        sentiment = blob.sentiment
        print(f"Sentiment polarity: {sentiment.polarity:.2f}")
        print(f"Sentiment subjectivity: {sentiment.subjectivity:.2f}")
        print("✅ Sentiment analysis working!")
    except Exception as e:
        print(f"❌ Sentiment analysis failed: {e}")
    
    print()
    
    # Test POS tagging
    print("🏷️ Testing POS Tagging:")
    try:
        words = word_tokenize(sample_text)
        pos_tags = pos_tag(words)
        pos_counts = Counter([tag for word, tag in pos_tags])
        
        print(f"Total words tagged: {len(pos_tags)}")
        print(f"Most common POS tags: {pos_counts.most_common(5)}")
        print("✅ POS tagging working!")
    except Exception as e:
        print(f"❌ POS tagging failed: {e}")
    
    print()
    
    # Test word frequency analysis
    print("📊 Testing Word Frequency Analysis:")
    try:
        words = word_tokenize(sample_text.lower())
        filtered_words = [word for word in words if word.isalpha() and word not in stop_words]
        word_freq = FreqDist(filtered_words)
        
        print(f"Total filtered words: {len(filtered_words)}")
        print(f"Most frequent words: {word_freq.most_common(5)}")
        print("✅ Word frequency analysis working!")
    except Exception as e:
        print(f"❌ Word frequency analysis failed: {e}")
    
    print()
    
    # Test sentence tokenization
    print("📝 Testing Sentence Tokenization:")
    try:
        sentences = sent_tokenize(sample_text)
        print(f"Total sentences: {len(sentences)}")
        print(f"First sentence: {sentences[0][:50]}...")
        print("✅ Sentence tokenization working!")
    except Exception as e:
        print(f"❌ Sentence tokenization failed: {e}")
    
    print()
    print("🎉 NLP features test completed!")

if __name__ == "__main__":
    test_nlp_features()


