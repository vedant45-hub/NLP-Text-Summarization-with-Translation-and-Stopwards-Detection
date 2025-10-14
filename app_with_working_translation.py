import streamlit as st
import re
from deep_translator import GoogleTranslator

# Page configuration
st.set_page_config(
    page_title="Text Summarizer Pro",
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
    
    .feature-box {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
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
    """Translate text to target language using deep-translator"""
    try:
        translator = GoogleTranslator(source='auto', target=target_language)
        result = translator.translate(text)
        return result
    except Exception as e:
        return f"Translation error: {str(e)}"

def main():
    # Header
    st.markdown('<h1 class="main-header">📝 Text Summarizer Pro</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Transform your text into concise summaries with beautiful translations</p>', unsafe_allow_html=True)
    
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
        st.markdown("✅ **Smart Summarization**")
        st.markdown("✅ **Multi-language Translation**")
        st.markdown("✅ **Beautiful UI**")
        st.markdown("✅ **Real-time Processing**")
        st.markdown("✅ **Download Options**")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Text input
        st.markdown("### 📝 Enter your text here:")
        user_text = st.text_area(
            "Paste your text below:",
            height=300,
            placeholder="Enter the text you want to summarize here...",
            help="You can paste any long text and we'll create a concise summary for you!"
        )
        
        # Process button
        if st.button("🚀 Generate Summary", type="primary"):
            if user_text.strip():
                with st.spinner("🔄 Processing your text..."):
                    # Generate summary
                    summary = simple_summarize(user_text, summary_length)
                    
                    # Store in session state
                    st.session_state['summary'] = summary
                    st.session_state['original_text'] = user_text
                    st.session_state['translate_to'] = translate_to
                    
                    # Show success message
                    st.success("✅ Summary generated successfully!")
            else:
                st.warning("⚠️ Please enter some text to summarize!")
    
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
            
            st.metric(
                "Sentences",
                f"{summary_length}"
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
            # Create a combined report
            report = f"""
TEXT SUMMARIZATION REPORT
========================

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
            
            st.download_button(
                label="📋 Download Full Report",
                data=report,
                file_name="summarization_report.txt",
                mime="text/plain"
            )
    
    # Features section
    st.markdown("---")
    st.markdown("## 🌟 Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        st.markdown("### 🧠 Smart AI")
        st.markdown("Advanced algorithms analyze your text to extract the most important sentences.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        st.markdown("### 🌍 Multi-language")
        st.markdown("Translate summaries to Hindi, Marathi, Spanish, French, German, and more!")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        st.markdown("### ⚡ Fast Processing")
        st.markdown("Get your summaries and translations in seconds with our optimized engine.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 2rem;'>
            <p>Made with ❤️ using Streamlit | Text Summarizer Pro v1.0</p>
            <p>🌍 Translation powered by Google Translate</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()


