from ast.INTEGER import INTEGER
from ast.META import META


class YEAR(META):
    # FIELDS:
    # year

    def parse(self):
        self.tokenizer.getAndCheckNext("Year:")
        self.tempo = INTEGER()
        self.tempo.parse()
        return
