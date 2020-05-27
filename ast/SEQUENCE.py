from libs.node import Node
from ast.NAME import NAME
from ast.INTEGER import INTEGER
# SEQUENCE ::= "{" NAME "}(" INTEGER ")"  
# Where STRING is seq variable and int is times to play it.

class SEQUENCE(Node):

    # FIELDS:
    # sequence name
    # sequence repeats

    def parse(self):
        self.tokenizer.getAndCheckNext("{")
        self.name = NAME()
        self.name.parse()
        self.tokenizer.getAndCheckNext("}")
        self.tokenizer.getAndCheckNext("(")
        self.repeats = INTEGER()
        self.repeats.parse()
        self.tokenizer.getAndCheckNext(")")
        return