from collections import Counter

import openai
import spacy


class TextClusteringAnalyzer:
    def __init__(self, oai_api_key: str):
        openai.api_key = oai_api_key
        self.nlp = spacy.load("ru_core_news_lg")

    def determine_texts_topic(self, text: str) -> str:
        doc = self.nlp(text)
        nouns = [token.lemma_ for token in doc if token.pos_ == "NOUN"]
        result_nouns = [noun for noun, count in Counter(nouns).most_common(7)]
        return "Группу можно классифицировать такими тэгами: " + ", ".join(result_nouns) + "."
