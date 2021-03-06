import requests
import json

class Dandelion:

    # in production, credential would be maintained within the 
    # configuration and certainly not in the source code!
    # this is a free test account so not too worried about it :)
    TOKEN = "2c0edee96e414d7e8fa468a38f688a2e"
    URL = "https://api.dandelion.eu/datatxt/nex/v1"

    # these are pretty arbitrary, just played around a bit
    NUM_ENTITIES = 3
    MIN_CONFIDENCE = 0.7

    # dandelion API limits text length
    CHAR_LIMIT = 3000

    def getEntities(self, text):
        keywords = set()
        min_index = 0
        max_index = self.CHAR_LIMIT if len(text) > self.CHAR_LIMIT else len(text)
        while max_index <= len(text):
            short_text = text[min_index:max_index]
            params = {
                    'token': self.TOKEN,
                    'text': short_text,
                    'top_entities': self.NUM_ENTITIES,
                    'min_confidence': self.MIN_CONFIDENCE
                }
            response = requests.get(self.URL, params=params)
            for annotation in response.json()['topEntities']:
                keywords.add(annotation['uri'])

            min_index = max_index
            if (max_index == len(text)):
                break
            max_index = max_index + self.CHAR_LIMIT if max_index + self.CHAR_LIMIT <= len(text) else len(text)
        return keywords
