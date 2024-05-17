from utils.extractText import extract_text_from_pdf
from flask import jsonify

def extract(request):

    if 'file' not in request.files:
        response_Data = {
        "message":"Extract Text From PDF",
        "success":"false"
    }
        response = jsonify(response_Data)
        response_Data['status'] = 400
        return response
    
    print("line 15")
    file = request.files['file']

    extractedText = extract_text_from_pdf(file)

    response_Data = {
            "message":"Extract Text From PDF",
            "success":"true",
            "text" : extractedText
        }
    response = jsonify(response_Data)
    response.status = 200

    return response