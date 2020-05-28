from libs.node import Node
from ast.STRING import STRING
from ast.APP_VISITOR import Visitor
# ARRANGER::= "Arranged by:" STRING


class ARRANGER(Node):
  # FIELDS:
  # arranger

  def parse(self):
      self.tokenizer.getAndCheckNext("Arranged by:")
      self.tokenizer.getAndCheckNext("\"")
      self.value = self.tokenizer.getNext()
      self.tokenizer.getAndCheckNext("\"")
      return

  def accept(self, visitor: Visitor) -> None:
    print("====ARRANGER.accept====")
    return visitor.visit_arranger(self)

  def toString(self):
    return self.value