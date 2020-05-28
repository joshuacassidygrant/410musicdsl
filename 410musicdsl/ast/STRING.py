from libs.node import Node
from ast.APP_VISITOR import Visitor

# STRING  ::= ([^"]*)


class STRING(Node):

  # FIELDS:
  # value

  def parse(self):
    self.tokenizer.getAndCheckNext("\"")
    self.value = self.tokenizer.getNext()
    self.tokenizer.getAndCheckNext("\"")
    return

  def accept(self, visitor: Visitor) -> None:
    print("====STRING.accept====")
    return visitor.visit_string(self)

  def toString(self):
    return self.value