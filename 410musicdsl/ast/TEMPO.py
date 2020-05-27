from libs.node import Node
from ast.INTEGER import INTEGER


class TEMPO(Node):
    # FIELDS:
    # tempo

    def parse(self):
        self.tokenizer.getAndCheckNext("Tempo:")
        self.tempo = INTEGER()
        self.tempo.parse()
        return
