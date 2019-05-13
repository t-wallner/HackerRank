class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    @staticmethod
    def comparator(a, b):
        """ Returns -1 if  a < b, 0 if a = b, and 1 if a > b."""
        if a.score == b.score:
            if a.name == b.name:
                return 0
            else:
                return 1 if a.name > b.name else -1
        else:
            return 1 if a.score < b.score else -1

