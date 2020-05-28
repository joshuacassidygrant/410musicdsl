from libs.node import Node
from ast.KEY_OF import KEY_OF
from ast.APP_VISITOR import Visitor
# KEY     ::= "Key:" KEYOF


class KEY(Node):
  # FIELDS:
  # key

  def parse(self):
      self.tokenizer.getAndCheckNext("Key:")
      self.key = KEY_OF()
      self.key.parse()
      return

  def accept(self, visitor: Visitor) -> None:
    print("====KEY.accept====")
    visitor.visit_key(self)