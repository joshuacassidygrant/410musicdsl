from libs.node import Node
from ast.STRING import STRING
from ast.APP_VISITOR import Visitor
# ARRANGER::= "Arranged by:" STRING


class ARRANGER(Node):
  # FIELDS:
  # arranger

  def parse(self):
      self.tokenizer.getAndCheckNext("Arranged by:")
      self.arranger = STRING()
      self.arranger.parse()
      return

  def accept(self, visitor: Visitor) -> None:
    print("====ARRANGER.accept====")
    visitor.visit_arranger(self)