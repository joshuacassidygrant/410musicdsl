from libs.node import Node
from ast.NAME import NAME
# PLAY    ::= play NAME

class PLAY(Node):
    
    # FIELDS
    # name

    def parse(self):
        self.tokenizer.getAndCheckNext("play")
        self.name = NAME()
        self.name.parse()
        return