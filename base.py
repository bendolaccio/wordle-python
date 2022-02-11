class Player(object):
    def choose(self, i, letter_not_in_word):
        raise NotImplementedError
    def update_knowledge(self, result):
        raise NotImplementedError