from libs.node import Node
from ast.NAME import NAME
from ast.LENGTH import LENGTH
# CHORD ::= "{" NAME "}" LENGTH		    // Where NAME refers to chord variable


class CHORD(Node):

    # FIELDS:
    # name of chord
    # length

    def parse(self):
        print("INSIDE CHORD.PARSE")
        self.tokenizer.getAndCheckNext("{")
        self.name = NAME()
        self.name.parse()
        self.tokenizer.getAndCheckNext("}")
        self.length = LENGTH()
        self.length.parse()
        return
