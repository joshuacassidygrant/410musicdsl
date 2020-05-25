from libs.node import Node
class TEMPO(Node):
    def parse(self):
        self.tokenizer.getAndCheckNext("Tempo:")
        self.tempo = self.tokenizer.getAndCheckNext('"3/4"|"4/4"')