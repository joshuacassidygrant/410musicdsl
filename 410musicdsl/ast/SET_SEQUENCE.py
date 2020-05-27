from libs.node import Node
from ast.NAME import NAME
# SET_SEQUENCE::= "seq " STRING "= [" ((BAR | SEQUENCE)"-")*(BAR | SEQUENCE)? "]"     // Sets new sequence variable with name STRING


class SET_SEQUENCE(Node):

    # FIELDS:
    # name
    # list of bars or sequences

    def parse(self):
        # TODO add variable for name to some sort of symbols table
        self.name = NAME()
        self.name.parse()

        # TODO parse internal sequence
        self.tokenizer.getAndCheckNext("= \[")
        while not self.tokenizer.checkToken("]"):
            # TODO actually build up bars
            self.tokenizer.getNext()

        self.tokenizer.getNext()
        return
