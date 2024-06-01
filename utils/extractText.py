import PyPDF2
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

def extract_text_from_pdf(file):
    raw = ""
    reader = PyPDF2.PdfReader(file)
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        raw += page.extract_text()
    
    return pre_process_text(raw)

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    stop_words.add('http')
    filtered_text = [word for word in text if word.lower() not in stop_words]
    return ' '.join(filtered_text)

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

def pre_process_text(raw):
    # Remove punctuation
    text_no_punc = remove_punctuation(raw)
    # Tokenize text
    words = word_tokenize(text_no_punc)
    # Remove stopwords
    clean_text = remove_stopwords(words)
    return clean_text