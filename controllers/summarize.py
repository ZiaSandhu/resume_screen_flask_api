from flask import jsonify

from utils.extractText import extract_text_from_pdf
from utils.parsing import parsingPdf
from collections import defaultdict


def summarize(request):
    
    if 'file' not in request.files:
        return "Files not found", 409
    file = request.files['file']

    extractedText = extract_text_from_pdf(file)
    parsedEnt = {}
    parsedText = parsingPdf(extractedText)
    for ent in parsedText:
        if ent.label_ in parsedEnt:
            parsedEnt[ent.label_].append(ent.text)
        else: 
            parsedEnt[ent.label_] = [ent.text]

    response_Data = {
                "message":"Parse PDF",
                "success":"true",
                "parsed" : parsedEnt
            }
    response = jsonify(response_Data)
    response.status = 200

    return response