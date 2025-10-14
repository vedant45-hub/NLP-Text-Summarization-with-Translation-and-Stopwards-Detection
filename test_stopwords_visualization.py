#!/usr/bin/env python3
"""
Test script to demonstrate stopwords visualization features
"""

import re
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

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

def test_stopwords_visualization():
    print("📊 Testing Stopwords Visualization Features")
    print("=" * 60)
    
    # Sample text with many stopwords
    sample_text = """
    The quick brown fox jumps over the lazy dog. This is a sample text that contains many stopwords 
    like 'the', 'is', 'a', 'that', 'and', 'over', 'lazy'. We will analyze this text to find all 
    the stopwords and show their frequency. The analysis will help us understand how many common 
    words are present in our text. This is a comprehensive test of our robust NLP system.
    The system works very well and provides excellent results. We can see that the stopwords 
    are detected properly and the visualization shows clear patterns. This is exactly what we 
    wanted to achieve with our advanced text analysis system.
    """
    
    print(f"Sample text: {sample_text.strip()}")
    print()
    
    try:
        # Process text
        words = simple_word_tokenize(sample_text)
        stop_words = get_basic_stopwords()
        
        # Find stopwords and non-stopwords
        stopwords_found = [word for word in words if word in stop_words and word.isalpha()]
        non_stopwords = [word for word in words if word not in stop_words and word.isalpha()]
        
        stopwords_count = Counter(stopwords_found)
        non_stopwords_count = Counter(non_stopwords)
        
        print("🚫 STOPWORDS ANALYSIS:")
        print("-" * 30)
        print(f"Total stopwords found: {len(stopwords_found)}")
        print(f"Unique stopwords: {len(stopwords_count)}")
        print(f"Total non-stopwords: {len(non_stopwords)}")
        print(f"Unique non-stopwords: {len(non_stopwords_count)}")
        
        # Calculate percentages
        total_words = len(words)
        stopwords_pct = (len(stopwords_found) / total_words) * 100
        non_stopwords_pct = (len(non_stopwords) / total_words) * 100
        
        print(f"\nStopwords percentage: {stopwords_pct:.1f}%")
        print(f"Non-stopwords percentage: {non_stopwords_pct:.1f}%")
        print()
        
        # Show most frequent stopwords
        print("Most frequent stopwords:")
        for word, count in stopwords_count.most_common(10):
            print(f"  • {word}: {count} times")
        print()
        
        # Create visualization
        print("📊 Creating stopwords visualization...")
        
        # Get top stopwords for visualization
        top_stopwords = stopwords_count.most_common(12)
        
        if top_stopwords:
            # Create DataFrame
            stopwords_df = pd.DataFrame(top_stopwords, columns=['Stopword', 'Frequency'])
            print("\nStopwords DataFrame:")
            print(stopwords_df)
            print()
            
            # Create visualization
            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
            
            # Bar chart for stopwords
            words, freqs = zip(*top_stopwords[:10])
            bars = ax1.bar(words, freqs, color='#ff6b6b', alpha=0.8)
            ax1.set_xlabel('Stopwords')
            ax1.set_ylabel('Frequency')
            ax1.set_title('Top 10 Most Frequent Stopwords')
            ax1.tick_params(axis='x', rotation=45)
            
            # Add value labels on bars
            for bar, freq in zip(bars, freqs):
                ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                        str(freq), ha='center', va='bottom')
            
            # Pie chart for stopwords distribution
            if len(top_stopwords) > 5:
                pie_data = top_stopwords[:8]
                words_pie, freqs_pie = zip(*pie_data)
                colors = plt.cm.Set3(range(len(words_pie)))
                
                ax2.pie(freqs_pie, labels=words_pie, autopct='%1.1f%%', 
                       colors=colors, startangle=90)
                ax2.set_title('Stopwords Distribution')
            
            # Horizontal bar chart
            words_h, freqs_h = zip(*top_stopwords[:10])
            y_pos = range(len(words_h))
            bars_h = ax3.barh(y_pos, freqs_h, color='#4ecdc4', alpha=0.8)
            ax3.set_yticks(y_pos)
            ax3.set_yticklabels(words_h)
            ax3.set_xlabel('Frequency')
            ax3.set_title('Stopwords Frequency (Horizontal)')
            ax3.invert_yaxis()
            
            # Add value labels on horizontal bars
            for i, (bar, freq) in enumerate(zip(bars_h, freqs_h)):
                ax3.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, 
                        str(freq), ha='left', va='center')
            
            # Stopwords vs Non-stopwords comparison
            categories = ['Stopwords', 'Non-Stopwords']
            percentages = [stopwords_pct, non_stopwords_pct]
            colors = ['#ff6b6b', '#4ecdc4']
            
            bars_comp = ax4.bar(categories, percentages, color=colors, alpha=0.8)
            ax4.set_ylabel('Percentage (%)')
            ax4.set_title('Stopwords vs Non-Stopwords Distribution')
            ax4.set_ylim(0, 100)
            
            # Add percentage labels on bars
            for bar, pct in zip(bars_comp, percentages):
                ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                        f'{pct:.1f}%', ha='center', va='bottom', fontweight='bold')
            
            plt.tight_layout()
            plt.savefig('stopwords_visualization.png', dpi=300, bbox_inches='tight')
            print("✅ Visualization saved as 'stopwords_visualization.png'")
            
            # Show statistics
            print("\n📈 VISUALIZATION STATISTICS:")
            print("-" * 30)
            print(f"Total Stopwords: {len(stopwords_found)}")
            print(f"Unique Stopwords: {len(stopwords_count)}")
            print(f"Average Frequency: {len(stopwords_found) / len(stopwords_count):.1f}")
            print(f"Stopwords Percentage: {stopwords_pct:.1f}%")
            
            # Most and least frequent
            if len(top_stopwords) > 1:
                most_frequent = top_stopwords[0]
                least_frequent = top_stopwords[-1]
                print(f"Most Frequent: '{most_frequent[0]}' ({most_frequent[1]} times)")
                print(f"Least Frequent: '{least_frequent[0]}' ({least_frequent[1]} times)")
        
        print()
        print("🎉 Stopwords visualization test completed successfully!")
        print("📊 The visualization includes:")
        print("  • Bar chart of most frequent stopwords")
        print("  • Pie chart of stopwords distribution")
        print("  • Horizontal bar chart for better readability")
        print("  • Comparison chart of stopwords vs non-stopwords")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_stopwords_visualization()


