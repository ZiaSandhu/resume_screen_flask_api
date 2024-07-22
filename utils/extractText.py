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


def extract_links_and_emails(text):
    link_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    links = re.findall(link_pattern, text)
    emails = re.findall(email_pattern, text)
    text = re.sub(link_pattern, "", text)
    text = re.sub(email_pattern, "", text)
    return links, emails, text


def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    stop_words.add("http")
    filtered_text = [word for word in text if word.lower() not in stop_words]
    return " ".join(filtered_text)


def remove_punctuation(text):
    return re.sub(r"[^\w\s]", "", text)


def pre_process_text(raw):
    # Extract links and emails first
    links, emails, text = extract_links_and_emails(raw)

    # Remove punctuation and stopwords from the remaining text
    # text_no_punc = remove_punctuation(text)
    words = word_tokenize(text)
    clean_text = remove_stopwords(words)

    # Reinsert links and emails
    clean_text += " " + " ".join(links) + " " + " ".join(emails)
    return clean_text


# Usage example:
# with open('example.pdf', 'rb') as file:
#     clean_text = extract_text_from_pdf(file)
#     print(clean_text)
