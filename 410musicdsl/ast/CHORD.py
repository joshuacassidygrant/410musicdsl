from libs.node import Node
from ast.NAME import NAME
from ast.LENGTH import LENGTH
from ast.APP_VISITOR import Visitor
# CHORD ::= "{" NAME "}" LENGTH		    // Where NAME refers to chord variable


class CHORD(Node):
  # FIELDS:
  # name of chord
  # length

  def parse(self):
    self.tokenizer.getAndCheckNext("{")
    self.name = NAME()
    self.name.parse()
    self.tokenizer.getAndCheckNext("}")
    self.length = LENGTH()
    self.length.parse()
    return

  def accept(self, visitor: Visitor) -> None:
    print("====CHORD.accept====")
    return visitor.visit_chord(self)