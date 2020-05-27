from libs.node import Node
from ast.NAME import NAME
from ast.PITCH import PITCH
# SET_CHORD   ::=  "chord " STRING "= {" (PITCH "-")* PITCH "}"  

class SET_CHORD(Node):

    # FIELDS:
    # list of pitches
    # name of chord

    def parse(self):
        self.pitches = []

        self.name = NAME()
        self.name.parse()

        self.tokenizer.getAndCheckNext("{")

        p = PITCH()
        p.parse()
        self.pitches.append(p)

        while self.tokenizer.checkToken("-"):
            self.tokenizer.getNext()
            p = PITCH()
            p.parse()
            self.pitches.append(p)

        self.tokenizer.getAndCheckNext("}")
        return