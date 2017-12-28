import os

# I used this to experiment with building my own
# stop-word corpus for tf-idf keyword extraction.
# Should be updated as data is ingested, but for
# now it's static.

class Corpus:
    def __init__(self):
        curr_dir = os.path.dirname(__file__)
        path = "data/stop_words"
        with open(os.path.join(curr_dir, path)) as file:
            self.stop_words = [word.strip() for word in file.readlines()]

    @property
    def stop_words(self):
        return self.stop_words