class Library(object):
    def __init__(self):
        self.dictionary = {
            "Micah": ["Judgement on Samaria and Judah", "Reason for the judgement", "Judgement on wicked leaders",
            "Messianic Kingdom", "Birth of the Messiah", "Indictment 1, 2", "Promise of salvation"]
        }

    def get(self, book):
        return self.dictionary.get(book)
