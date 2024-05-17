from utils.extractText import extract_text_from_pdf
from utils.classification import classify
from collections import defaultdict

from flask import jsonify

def classifications(request):

    if 'file' not in request.files:
        return "Files not found", 409
    files = request.files.getlist('file')
    print(files)
    data = defaultdict(list)

    for index, file in enumerate(files):
        print(f"Processing file at index {index}: {file}")
        extractedText = extract_text_from_pdf(file)
        label = classify(extractedText)

    #   change index to file.id when used with website 
        data[label].append(file.filename)
    response_Data = {
                    "message":"Parse PDF",
                    "success":"true",
                    "data" : data
                }
    response = jsonify(response_Data)
    response.status = 200

    return response