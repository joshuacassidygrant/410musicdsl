from libs.node import Node
from ast.APP_VISITOR import Visitor
# INTEGER ::= \d+


class INTEGER(Node):

    # FIELDS:
    # value

    def parse(self):
        self.value = self.tokenizer.getAndCheckNext("\\d+")
        return

    def accept(self, visitor: Visitor) -> None:
      print("====INTEGER.accept====")
      return visitor.visit_integer(self)
