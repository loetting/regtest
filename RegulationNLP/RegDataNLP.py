# # coding: utf-8

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
import os
from Corpus import Corpus


class RegDataNLP:

    def __init__(self, text):
        self.corpus = Corpus()
        self.text = text

    # get basic entity extraction results
    # params: text (text to be processed)
    def getNamedEntities(self):
        ne_set = set()
        try:
            tree = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(self.text)))
            iob_tagged = nltk.tree2conlltags(tree)
            for obj in iob_tagged:
                if obj[1] == 'NNP' and len(obj[0]) > 3: ne_set.add(obj[0])
        except:
            print "error in NER"
        return ne_set

    # get basic keyword results
    # params: text (text to be processed)
    def getKeywords(self):
        try:
            vectorizer = TfidfVectorizer(min_df=1, stop_words=self.corpus.stop_words)
            X = vectorizer.fit_transform([self.text])
            idf = vectorizer.idf_
            return dict(zip(vectorizer.get_feature_names(), idf))
        except:
            return {}
