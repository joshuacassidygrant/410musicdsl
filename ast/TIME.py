from Node import Node

class TIME(Node):

    def parse(self):
        self.tokenizer.getAndCheckNext("Time:")
        self.time = self.tokenizer.getAndCheckNext('([^"]*)')