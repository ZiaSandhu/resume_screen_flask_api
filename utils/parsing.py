import spacy
# from spacy.tokens import DocBin

def parsingPdf(pdfText):
    nlp = spacy.load('models/summerize_model/model-best')
    doc = nlp(pdfText)
    return doc.ents