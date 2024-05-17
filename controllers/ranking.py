from utils.extractText import extract_text_from_pdf
from collections import defaultdict
from flask import jsonify
import random

def ranking(request):

    if 'file' not in request.files:
        return "Files not found", 409
    files = request.files.getlist('file')
    data = list()

    for file in files:
        # print(f"Processing file at index {index}: {file}")
        # extractedText = extract_text_from_pdf(file)
        # label = classify(extractedText)

        data.append(file.filename)

    random.shuffle(data)
    response_Data = {
                    "message":"Ranking Resume",
                    "success":"true",
                    "data" : data
                }
    response = jsonify(response_Data)
    response.status = 200

    return response