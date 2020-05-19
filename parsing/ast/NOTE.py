from Node import Node

class NOTE(Node):
    def parse(self):
        self.tokenizer.getAndCheckNext('([A-G](#|b|)[0-8]\.?(s|e|q|h|w))')
        if (self.tokenizer.checkNext(',')):
            self.tokenizer.getNext()