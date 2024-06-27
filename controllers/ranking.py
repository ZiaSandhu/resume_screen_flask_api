from utils.extractText import extract_text_from_pdf
from collections import defaultdict
from flask import jsonify
import random

# from gensim.summarization import summarize
# from gensim.sumarization import keywords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize(text,ratio=1):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document,ratio)  # Summarize to 3 sentences
    return " ".join(str(sentence) for sentence in summary)


def ranking(request):

    if 'file' not in request.files:
        return "Files not found", 409
    files = request.files.getlist('file')
    data = list()
    jd = request.form.get('jobDescription')
    summarize_description = summarize(jd,ratio=1)

    for file in files:
        extractedText = extract_text_from_pdf(file)

        textlist = [summarize_description,extractedText] 
        cv = CountVectorizer()
        countmatrix = cv.fit_transform(textlist)
        matchpercentage = cosine_similarity(countmatrix)[0][1]*100
        matchpercentage = round(matchpercentage,2)
        data.append({"name":file.filename,"score":matchpercentage})

    # print(data)

    response_Data = {
                    "message":"Ranking Resume",
                    "success":"true",
                    "data" : data
                }
    response = jsonify(response_Data)
    response.status = 200

    return response