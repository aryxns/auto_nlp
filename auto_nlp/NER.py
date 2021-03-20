import textacy
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_lg')

def basic_ner(text):
    doc = nlp(text)
    answer = {"Entities":[], "Label":[]}
    for entity in doc.ents:
        answer["Word"].append(entity.text)
        if entity.label_ == "GPE":
            answer["Label"].append("LOC")
        else:
            answer["Label"].append(entity.label_)
    return answer
