from libs.node import Node
from ast.NAME import NAME
from ast.BAR import BAR
from ast.SEQUENCE import SEQUENCE
from ast.APP_VISITOR import Visitor
# SET_SEQUENCE::=
# "seq " STRING "= [" ((BAR | SEQUENCE)"-")*(BAR | SEQUENCE)? "]"
# // Sets new sequence variable with name STRING


class SET_SEQUENCE(Node):
  # FIELDS:
  # name
  # list of bars or sequences

  def parse(self):
    # TODO add variable for name to some sort of symbols table
    self.name = NAME()
    self.name.parse()
    self.measures = []

    # TODO parse internal sequence
    self.tokenizer.getAndCheckNext("=")
    self.tokenizer.getAndCheckNext("\\[")
    while not self.tokenizer.checkToken("]"):
        if self.tokenizer.checkToken("\\|(T)\\|"):
            print("Found a BAR inside SET_SEQUENCE")
            bar = BAR()
            bar.parse()
            self.measures.append(bar)
        elif self.tokenizer.checkToken("{"):
            seq = SEQUENCE()
            seq.parse()
            self.measures.append(seq)
        if self.tokenizer.checkToken("-"):
            self.tokenizer.getNext()

    self.tokenizer.getNext()
    return

  def accept(self, visitor: Visitor) -> None:
    print("====SET_SEQUENCE.accept====")
    return visitor.visit_set_sequence(self)
