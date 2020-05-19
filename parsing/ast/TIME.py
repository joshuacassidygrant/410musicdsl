from Node import Node
import re

class TIME(Node):
    def parse(self):
        self.tokenizer.getAndCheckNext("Time:")
        this.time = self.tokenizer.getAndCheckNext("")