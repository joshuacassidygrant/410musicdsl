from libs.node import Node
from ast.NAME import NAME
from ast.APP_VISITOR import Visitor
# PLAY    ::= play NAME


class PLAY(Node):
    # FIELDS
    # name

    def parse(self):
      print("=====PLAY.parse======")
      self.tokenizer.getAndCheckNext("play")
      self.name = NAME()
      self.name.parse()
      return
    
    def accept(self, visitor: Visitor) -> None:
      print("====PLAY.accept====")
      return visitor.visit_play(self)
