# # coding: utf-8

from collections import Counter

class RestrictiveWordClassifier:

    restrictive_words = ['shall', 'must', 'required', 'prohibited']
    restrictive_tuples = {'may':'not'}

    def getCount(self, text):
        counter = Counter()
        target = None
        key = None
        for word in text.lower().split():
            if word in self.restrictive_words:
                counter[word] += 1
                target = None
            elif word == target:
                counter[key + " " + target] += 1
                target = None
            elif word in self.restrictive_tuples:
                target = self.restrictive_tuples[word]
                key = word
            else:
                target = None
        return sum(counter.values())

