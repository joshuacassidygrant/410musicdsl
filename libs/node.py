from libs.tokenizer import Tokenizer

class Node:

    def __init__(self):
        print("init node for " + str(type(self)))
        self.tokenizer = Tokenizer.getTokenizer()

    def parse(self):
        pass

    def evaluate(self):
        pass 