import spacy


class TextProcessor:
    def __init__(self, model_name="en_core_web_sm"):
        print(f"Loading the model: {model_name}...")
        self.nlp = spacy.load(model_name)

    def analyze_text(self, text):
        doc = self.nlp(text)
        results = []
        for token in doc:
            results.append({"word": token.text, "pos": token.pos_})
        return results
