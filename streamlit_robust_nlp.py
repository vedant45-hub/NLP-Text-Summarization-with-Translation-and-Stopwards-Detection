import streamlit as st
import re
import nltk
from deep_translator import GoogleTranslator
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

# Download NLTK data with error handling
def download_nltk_data():
    try:
        nltk.download('punkt_tab', quiet=True)
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)
        return True
    except Exception as e:
        st.warning(f"NLTK data download issue: {str(e)}")
        return False

# Try to download NLTK data
download_nltk_data()

# Import NLTK modules with fallback
try:
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.probability import FreqDist
    from nltk.tag import pos_tag
    NLTK_AVAILABLE = True
except ImportError:
    NLTK_AVAILABLE = False
    st.error("NLTK is not properly installed. Some features may not work.")

# Page configuration
st.set_page_config(
    page_title="Advanced Text Summarizer Pro",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    
    .sub-header {
        font-size: 1.5rem;
        color: #4a5568;
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    
    .summary-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .translation-box {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
    
    .analysis-box {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: #2c3e50;
        margin: 1rem 0;
    }
    
    .stopwords-box {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: #2c3e50;
        margin: 1rem 0;
    }
    
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #e2e8f0;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    .stSelectbox > div > div {
        border-radius: 10px;
    }
    
    .success-box {
        background: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

def simple_sentence_split(text):
    """Simple sentence splitting without NLTK"""
    # Split on sentence endings
    sentences = re.split(r'[.!?]+', text)
    # Clean up and filter empty sentences
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def simple_word_tokenize(text):
    """Simple word tokenization without NLTK"""
    # Split on whitespace and punctuation
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

def advanced_summarize(text, num_sentences=3):
    """Advanced extractive summarization with fallback options"""
    
    if NLTK_AVAILABLE:
        try:
            # Use NLTK if available
            sentences = sent_tokenize(text)
            stop_words = set(stopwords.words('english'))
            words = word_tokenize(text.lower())
        except:
            # Fallback to simple methods
            sentences = simple_sentence_split(text)
            stop_words = get_basic_stopwords()
            words = simple_word_tokenize(text)
    else:
        # Use simple methods
        sentences = simple_sentence_split(text)
        stop_words = get_basic_stopwords()
        words = simple_word_tokenize(text)
    
    # Filter words and calculate frequencies
    filtered_words = [word for word in words if word.isalpha() and word not in stop_words]
    word_freq = Counter(filtered_words)
    
    # Score sentences
    sentence_scores = []
    for i, sentence in enumerate(sentences):
        score = 0
        sentence_words = simple_word_tokenize(sentence.lower())
        
        # Word frequency score
        for word in sentence_words:
            if word in word_freq:
                score += word_freq[word]
        
        # Position bonus
        if i == 0 or i == len(sentences) - 1:
            score *= 1.2
        
        # Length optimization
        sentence_length = len(sentence_words)
        if 10 <= sentence_length <= 30:
            score *= 1.1
        elif sentence_length < 5 or sentence_length > 50:
            score *= 0.8
        
        sentence_scores.append((score, sentence))
    
    # Get top sentences
    sentence_scores.sort(reverse=True)
    top_sentences = [sent for score, sent in sentence_scores[:num_sentences]]
    
    return '. '.join(top_sentences) + '.'

def extract_stopwords(text):
    """Extract and analyze stopwords from text"""
    try:
        if NLTK_AVAILABLE:
            try:
                stop_words = set(stopwords.words('english'))
                words = word_tokenize(text.lower())
            except:
                stop_words = get_basic_stopwords()
                words = simple_word_tokenize(text)
        else:
            stop_words = get_basic_stopwords()
            words = simple_word_tokenize(text)
        
        # Find stopwords in the text
        stopwords_found = [word for word in words if word in stop_words and word.isalpha()]
        stopwords_count = Counter(stopwords_found)
        
        # Find non-stopwords
        non_stopwords = [word for word in words if word not in stop_words and word.isalpha()]
        non_stopwords_count = Counter(non_stopwords)
        
        return stopwords_count, non_stopwords_count, stop_words
    except Exception as e:
        return Counter(), Counter(), set()

def analyze_text(text):
    """Perform comprehensive text analysis"""
    try:
        if NLTK_AVAILABLE:
            try:
                sentences = sent_tokenize(text)
                words = word_tokenize(text)
                pos_tags = pos_tag(words)
                pos_counts = Counter([tag for word, tag in pos_tags])
            except:
                sentences = simple_sentence_split(text)
                words = simple_word_tokenize(text)
                pos_counts = Counter()
        else:
            sentences = simple_sentence_split(text)
            words = simple_word_tokenize(text)
            pos_counts = Counter()
        
        # Basic statistics
        avg_sentence_length = len(words) / len(sentences) if sentences else 0
        avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
        
        # Simple sentiment analysis
        positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'awesome', 'brilliant', 'outstanding', 'perfect']
        negative_words = ['bad', 'terrible', 'awful', 'horrible', 'disappointing', 'poor', 'worst', 'hate', 'dislike', 'negative']
        
        words_lower = [word.lower() for word in words]
        positive_count = sum(1 for word in words_lower if word in positive_words)
        negative_count = sum(1 for word in words_lower if word in negative_words)
        
        sentiment_score = (positive_count - negative_count) / len(words) if words else 0
        
        return {
            'pos_counts': pos_counts,
            'avg_sentence_length': avg_sentence_length,
            'avg_word_length': avg_word_length,
            'total_words': len(words),
            'total_sentences': len(sentences),
            'total_characters': len(text),
            'sentiment_score': sentiment_score,
            'positive_words': positive_count,
            'negative_words': negative_count
        }
    except Exception as e:
        return None

def translate_text(text, target_language):
    """Translate text to target language using deep-translator"""
    try:
        translator = GoogleTranslator(source='auto', target=target_language)
        result = translator.translate(text)
        return result
    except Exception as e:
        return f"Translation error: {str(e)}"

def main():
    # Header
    st.markdown('<h1 class="main-header">📝 Advanced Text Summarizer Pro</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">AI-powered text analysis with stopwords detection and translation</p>', unsafe_allow_html=True)
    
    # Show NLTK status
    if NLTK_AVAILABLE:
        st.success("✅ NLTK is available - Full NLP features enabled")
    else:
        st.warning("⚠️ NLTK not available - Using basic text processing")
    
    # Sidebar
    with st.sidebar:
        st.markdown("## ⚙️ Settings")
        
        # Summary length slider
        summary_length = st.slider(
            "Number of sentences in summary",
            min_value=1,
            max_value=10,
            value=3,
            help="Choose how many sentences you want in your summary"
        )
        
        # Translation options
        st.markdown("## 🌍 Translation Options")
        translate_to = st.selectbox(
            "Translate summary to:",
            ["None", "Hindi", "Marathi", "Spanish", "French", "German", "Japanese", "Chinese", "Arabic"],
            help="Select a language to translate your summary"
        )
        
        # Language codes mapping
        lang_codes = {
            "Hindi": "hi",
            "Marathi": "mr", 
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Japanese": "ja",
            "Chinese": "zh",
            "Arabic": "ar"
        }
        
        st.markdown("---")
        st.markdown("## 📊 Features")
        st.markdown("✅ **Advanced NLP Analysis**")
        st.markdown("✅ **Stopwords Detection**")
        st.markdown("✅ **Sentiment Analysis**")
        st.markdown("✅ **POS Tagging**")
        st.markdown("✅ **Multi-language Translation**")
        st.markdown("✅ **Beautiful Visualizations**")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Text input
        st.markdown("### 📝 Enter your text here:")
        user_text = st.text_area(
            "Paste your text below:",
            height=300,
            placeholder="Enter the text you want to analyze and summarize here...",
            help="You can paste any long text and we'll provide comprehensive analysis!"
        )
        
        # Process button
        if st.button("🚀 Analyze & Summarize", type="primary"):
            if user_text.strip():
                with st.spinner("🔄 Processing your text with advanced NLP..."):
                    # Generate summary
                    summary = advanced_summarize(user_text, summary_length)
                    
                    # Extract stopwords
                    stopwords_found, non_stopwords_found, all_stopwords = extract_stopwords(user_text)
                    
                    # Analyze text
                    analysis = analyze_text(user_text)
                    
                    # Store in session state
                    st.session_state['summary'] = summary
                    st.session_state['original_text'] = user_text
                    st.session_state['translate_to'] = translate_to
                    st.session_state['stopwords_found'] = stopwords_found
                    st.session_state['non_stopwords_found'] = non_stopwords_found
                    st.session_state['all_stopwords'] = all_stopwords
                    st.session_state['analysis'] = analysis
                    
                    # Show success message
                    st.success("✅ Text analysis completed successfully!")
            else:
                st.warning("⚠️ Please enter some text to analyze!")
    
    with col2:
        # Metrics
        if 'summary' in st.session_state:
            st.markdown("### 📊 Statistics")
            
            col2a, col2b = st.columns(2)
            with col2a:
                st.metric(
                    "Original Length",
                    f"{len(st.session_state['original_text'])} chars"
                )
            with col2b:
                st.metric(
                    "Summary Length", 
                    f"{len(st.session_state['summary'])} chars"
                )
            
            compression_ratio = len(st.session_state['summary']) / len(st.session_state['original_text'])
            st.metric(
                "Compression Ratio",
                f"{compression_ratio:.1%}"
            )
            
            if st.session_state['analysis']:
                st.metric(
                    "Sentiment Score",
                    f"{st.session_state['analysis']['sentiment_score']:.2f}"
                )
    
    # Display results
    if 'summary' in st.session_state:
        st.markdown("---")
        
        # Summary section
        st.markdown('<div class="summary-box">', unsafe_allow_html=True)
        st.markdown("### 🎯 Your Summary")
        st.write(st.session_state['summary'])
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Translation section
        if st.session_state['translate_to'] != "None":
            with st.spinner(f"🌍 Translating to {st.session_state['translate_to']}..."):
                try:
                    translated_summary = translate_text(st.session_state['summary'], lang_codes[st.session_state['translate_to']])
                    
                    st.markdown('<div class="translation-box">', unsafe_allow_html=True)
                    st.markdown(f"### 🌍 Summary in {st.session_state['translate_to']}")
                    st.write(translated_summary)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Store translation in session state
                    st.session_state['translated_summary'] = translated_summary
                    
                except Exception as e:
                    st.error(f"Translation failed: {str(e)}")
                    st.session_state['translated_summary'] = None
        
        # NLP Analysis Section
        st.markdown("---")
        st.markdown("## 🔍 Advanced NLP Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Stopwords Analysis
            st.markdown('<div class="stopwords-box">', unsafe_allow_html=True)
            st.markdown("### 🚫 Stopwords Found in Text")
            
            if st.session_state['stopwords_found']:
                # Most common stopwords
                most_common_stopwords = st.session_state['stopwords_found'].most_common(10)
                st.write("**Most frequent stopwords:**")
                for word, count in most_common_stopwords:
                    st.write(f"• {word}: {count} times")
                
                # Total stopwords count
                total_stopwords = sum(st.session_state['stopwords_found'].values())
                st.write(f"\n**Total stopwords found:** {total_stopwords}")
                
                # Show all stopwords found
                st.write(f"\n**All stopwords in text:**")
                all_stopwords_list = list(st.session_state['stopwords_found'].keys())
                st.write(", ".join(all_stopwords_list[:20]))  # Show first 20
                if len(all_stopwords_list) > 20:
                    st.write(f"... and {len(all_stopwords_list) - 20} more")
            else:
                st.write("No stopwords found in the text.")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            # Text Statistics
            if st.session_state['analysis']:
                st.markdown('<div class="analysis-box">', unsafe_allow_html=True)
                st.markdown("### 📈 Text Statistics")
                
                analysis = st.session_state['analysis']
                st.write(f"**Total Words:** {analysis['total_words']}")
                st.write(f"**Total Sentences:** {analysis['total_sentences']}")
                st.write(f"**Avg Sentence Length:** {analysis['avg_sentence_length']:.1f} words")
                st.write(f"**Avg Word Length:** {analysis['avg_word_length']:.1f} characters")
                st.write(f"**Sentiment Score:** {analysis['sentiment_score']:.2f}")
                st.write(f"**Positive Words:** {analysis['positive_words']}")
                st.write(f"**Negative Words:** {analysis['negative_words']}")
                
                st.markdown('</div>', unsafe_allow_html=True)
        
        # Stopwords Visualization
        if st.session_state['stopwords_found']:
            st.markdown("### 📊 Stopwords Frequency Visualization")
            
            # Get top stopwords for visualization
            top_stopwords = st.session_state['stopwords_found'].most_common(15)
            
            if top_stopwords:
                # Create DataFrame for stopwords
                stopwords_df = pd.DataFrame(top_stopwords, columns=['Stopword', 'Frequency'])
                
                # Display as table
                st.write("**Stopwords Frequency Table:**")
                st.dataframe(stopwords_df, use_container_width=True)
                
                # Create stopwords visualizations (2 charts only)
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
                
                # Horizontal bar chart for better readability
                words_h, freqs_h = zip(*top_stopwords[:12])
                y_pos = range(len(words_h))
                bars_h = ax1.barh(y_pos, freqs_h, color='#4ecdc4', alpha=0.8)
                ax1.set_yticks(y_pos)
                ax1.set_yticklabels(words_h)
                ax1.set_xlabel('Frequency')
                ax1.set_title('Stopwords Frequency (Horizontal)')
                ax1.invert_yaxis()
                
                # Add value labels on horizontal bars
                for i, (bar, freq) in enumerate(zip(bars_h, freqs_h)):
                    ax1.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, 
                            str(freq), ha='left', va='center')
                
                # Stopwords vs Non-stopwords comparison
                total_stopwords = sum(st.session_state['stopwords_found'].values())
                total_non_stopwords = sum(st.session_state['non_stopwords_found'].values()) if st.session_state['non_stopwords_found'] else 0
                total_words = total_stopwords + total_non_stopwords
                
                if total_words > 0:
                    stopwords_pct = (total_stopwords / total_words) * 100
                    non_stopwords_pct = (total_non_stopwords / total_words) * 100
                    
                    categories = ['Stopwords', 'Non-Stopwords']
                    percentages = [stopwords_pct, non_stopwords_pct]
                    colors = ['#ff6b6b', '#4ecdc4']
                    
                    bars_comp = ax2.bar(categories, percentages, color=colors, alpha=0.8)
                    ax2.set_ylabel('Percentage (%)')
                    ax2.set_title('Stopwords vs Non-Stopwords Distribution')
                    ax2.set_ylim(0, 100)
                    
                    # Add percentage labels on bars
                    for bar, pct in zip(bars_comp, percentages):
                        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                                f'{pct:.1f}%', ha='center', va='bottom', fontweight='bold')
                
                plt.tight_layout()
                st.pyplot(fig)
                
                # Stopwords statistics
                total_stopwords = sum(st.session_state['stopwords_found'].values())
                unique_stopwords = len(st.session_state['stopwords_found'])
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Total Stopwords", total_stopwords)
                with col2:
                    st.metric("Unique Stopwords", unique_stopwords)
                with col3:
                    avg_freq = total_stopwords / unique_stopwords if unique_stopwords > 0 else 0
                    st.metric("Avg Frequency", f"{avg_freq:.1f}")
                with col4:
                    if total_words > 0:
                        stopwords_pct = (total_stopwords / total_words) * 100
                        st.metric("Stopwords %", f"{stopwords_pct:.1f}%")
                
                # Most and least frequent stopwords
                if len(top_stopwords) > 1:
                    most_frequent = top_stopwords[0]
                    least_frequent = top_stopwords[-1]
                    
                    st.markdown("#### 🔍 Stopwords Insights")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.info(f"**Most Frequent:** '{most_frequent[0]}' appears {most_frequent[1]} times")
                    with col2:
                        st.info(f"**Least Frequent:** '{least_frequent[0]}' appears {least_frequent[1]} times")
        
        # Word Frequency Analysis (Non-Stopwords)
        if st.session_state['non_stopwords_found']:
            st.markdown("### 📊 Word Frequency Analysis (Non-Stopwords)")
            
            # Get top 20 most frequent words
            top_words = st.session_state['non_stopwords_found'].most_common(20)
            
            if top_words:
                # Create DataFrame for better display
                df = pd.DataFrame(top_words, columns=['Word', 'Frequency'])
                
                # Display as table
                st.dataframe(df, use_container_width=True)
                
                # Create a simple bar chart
                fig, ax = plt.subplots(figsize=(10, 6))
                words, freqs = zip(*top_words[:10])  # Top 10 for better visualization
                bars = ax.bar(words, freqs, color='skyblue', alpha=0.7)
                ax.set_xlabel('Words')
                ax.set_ylabel('Frequency')
                ax.set_title('Top 10 Most Frequent Words (Non-Stopwords)')
                ax.tick_params(axis='x', rotation=45)
                
                # Add value labels on bars
                for bar, freq in zip(bars, freqs):
                    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                           str(freq), ha='center', va='bottom')
                
                plt.tight_layout()
                st.pyplot(fig)
        
        # POS Tagging Analysis (only if NLTK is available)
        if NLTK_AVAILABLE and st.session_state['analysis'] and st.session_state['analysis']['pos_counts']:
            st.markdown("### 🏷️ Part-of-Speech Analysis")
            
            pos_data = st.session_state['analysis']['pos_counts']
            pos_df = pd.DataFrame(list(pos_data.items()), columns=['POS Tag', 'Count'])
            pos_df = pos_df.sort_values('Count', ascending=False)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**POS Tag Distribution:**")
                st.dataframe(pos_df.head(10), use_container_width=True)
            
            with col2:
                # Create pie chart for top POS tags
                top_pos = pos_df.head(8)
                fig, ax = plt.subplots(figsize=(8, 6))
                ax.pie(top_pos['Count'], labels=top_pos['POS Tag'], autopct='%1.1f%%', startangle=90)
                ax.set_title('Part-of-Speech Distribution')
                st.pyplot(fig)
        
        # Download options
        st.markdown("### 💾 Download Options")
        col3, col4, col5 = st.columns(3)
        
        with col3:
            st.download_button(
                label="📄 Download Summary",
                data=st.session_state['summary'],
                file_name="summary.txt",
                mime="text/plain"
            )
        
        with col4:
            if st.session_state['translate_to'] != "None" and 'translated_summary' in st.session_state and st.session_state['translated_summary']:
                st.download_button(
                    label=f"🌍 Download {st.session_state['translate_to']} Translation",
                    data=st.session_state['translated_summary'],
                    file_name=f"summary_{st.session_state['translate_to'].lower()}.txt",
                    mime="text/plain"
                )
        
        with col5:
            # Create a comprehensive report
            report = f"""
ADVANCED TEXT ANALYSIS REPORT
============================

Original Text Length: {len(st.session_state['original_text'])} characters
Summary Length: {len(st.session_state['summary'])} characters
Compression Ratio: {compression_ratio:.1%}
Number of Sentences: {summary_length}

SUMMARY:
--------
{st.session_state['summary']}

"""
            if st.session_state['translate_to'] != "None" and 'translated_summary' in st.session_state and st.session_state['translated_summary']:
                report += f"""
{st.session_state['translate_to'].upper()} TRANSLATION:
----------------------------
{st.session_state['translated_summary']}

"""
            
            if st.session_state['analysis']:
                analysis = st.session_state['analysis']
                report += f"""
TEXT ANALYSIS:
--------------
Total Words: {analysis['total_words']}
Total Sentences: {analysis['total_sentences']}
Average Sentence Length: {analysis['avg_sentence_length']:.1f} words
Average Word Length: {analysis['avg_word_length']:.1f} characters
Sentiment Score: {analysis['sentiment_score']:.2f}
Positive Words: {analysis['positive_words']}
Negative Words: {analysis['negative_words']}

STOPWORDS ANALYSIS:
------------------
Total Stopwords: {sum(st.session_state['stopwords_found'].values())}
Unique Stopwords: {len(st.session_state['stopwords_found'])}
Stopwords Percentage: {(sum(st.session_state['stopwords_found'].values()) / (sum(st.session_state['stopwords_found'].values()) + sum(st.session_state['non_stopwords_found'].values()))) * 100:.1f}%

Most Frequent Stopwords:
"""
                for word, count in st.session_state['stopwords_found'].most_common(20):
                    report += f"  {word}: {count} times\n"
                
                report += f"""
All Stopwords Found:
"""
                all_stopwords_list = list(st.session_state['stopwords_found'].keys())
                report += f"  {', '.join(all_stopwords_list)}\n"
            
            st.download_button(
                label="📋 Download Full Report",
                data=report,
                file_name="advanced_analysis_report.txt",
                mime="text/plain"
            )
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 2rem;'>
            <p>Made with ❤️ using Streamlit, NLTK | Advanced Text Summarizer Pro v2.0</p>
            <p>🔬 Powered by Advanced NLP Libraries</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
