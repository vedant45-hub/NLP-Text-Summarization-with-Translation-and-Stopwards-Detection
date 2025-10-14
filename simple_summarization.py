import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq

# Function for custom extractive summarization
def extractive_summarization_custom(text):
    try:
        stop_words = set(stopwords.words('english'))
    except LookupError:
        print("Downloading stopwords...")
        nltk.download('stopwords', quiet=True)
        stop_words = set(stopwords.words('english'))
    
    try:
        words = word_tokenize(text)
    except LookupError:
        print("Downloading punkt...")
        nltk.download('punkt', quiet=True)
        words = word_tokenize(text)

    freq_table = {}
    for word in words:
        word = word.lower()
        if word not in stop_words and word.isalpha():
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1

    sentences = sent_tokenize(text)
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_table:
                if sentence in sentence_scores:
                    sentence_scores[sentence] += freq_table[word]
                else:
                    sentence_scores[sentence] = freq_table[word]

    summary_sentences = heapq.nlargest(3, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    
    return summary

# Sample text
text = """
Artificial Intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving".

As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect. A quip in Tesler's Theorem says "AI is whatever hasn't been done yet." For instance, optical character recognition is frequently excluded from things considered to be AI, having become a routine technology.

Artificial intelligence was founded as an academic discipline in 1956, and in the years since has experienced several waves of optimism, followed by disappointment and the loss of funding (known as an "AI winter"), followed by new approaches, success and renewed funding. For most of its history, AI research has been divided into sub-fields that often fail to communicate with each other. These sub-fields are based on technical considerations, such as particular goals (e.g. "robotics" or "machine learning"), the use of particular tools ("logic" or artificial neural networks), or deep philosophical differences. Sub-fields have also been based on social factors (particular institutions or the work of particular researchers).

The traditional problems (or goals) of AI research include reasoning, knowledge representation, planning, learning, natural language processing, perception and the ability to move and manipulate objects. General intelligence is among the field's long-term goals. Approaches include statistical methods, computational intelligence, and traditional symbolic AI. Many tools are used in AI, including versions of search and mathematical optimization, artificial neural networks, and methods based on statistics, probability and economics. The AI field draws upon computer science, mathematics, psychology, linguistics, philosophy, and many other fields.
"""

# Generate summary
print("Custom NLTK Summary:")
print("=" * 50)
summary = extractive_summarization_custom(text)
print(summary)
print("=" * 50)
print(f"Original text length: {len(text)} characters")
print(f"Summary length: {len(summary)} characters")
print(f"Compression ratio: {len(summary)/len(text):.2%}")


