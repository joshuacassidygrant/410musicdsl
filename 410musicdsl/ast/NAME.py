from libs.node import Node
from ast.APP_VISITOR import Visitor
# NAME    ::=


class NAME(Node):
    # FIELDS
    # value

    def parse(self):
      self.value = self.tokenizer.getAndCheckNext("[^\"]*")
      return
    
    def toString(self):
      return self.value
    
    def accept(self, visitor: Visitor) -> None:
      print("====NAME.accept====")
      return visitor.visit_name(self)

