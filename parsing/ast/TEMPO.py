from Node import Node

class TEMPO(Node):
    def parse(self):
        self.tokenizer.getAndCheckNext("Tempo:")
        self.tokenizer.getNext() #todo - regex X/X or 3/4, 4/4