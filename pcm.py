from nemo.collections.nlp.models import PunctuationCapitalizationModel

class PunctuationCapitalizationAPI:
    def __init__(self):
        # model instanse
        self.model = PunctuationCapitalizationModel.from_pretrained("punctuation_en_bert")

    def punctuate_and_capitalize(self, text):
        out = self.model.add_punctuation_capitalization([text])
        return out

    def punctuate_and_capitalize_multiple(self, texts):
        out = self.model.add_punctuation_capitalization([texts])
        return out