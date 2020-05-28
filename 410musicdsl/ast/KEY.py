from libs.node import Node
from ast.KEY_OF import KEY_OF
from ast.APP_VISITOR import Visitor
# KEY     ::= "Key:" KEYOF


class KEY(Node):
  # FIELDS:
  # key

  def parse(self):
      self.tokenizer.getAndCheckNext("Key:")
      self.tokenizer.getAndCheckNext("\"")
      self.value = self.tokenizer.getAndCheckNext("([A-G](b|#|)(maj|min))")
      self.tokenizer.getAndCheckNext("\"")
      return

  def accept(self, visitor: Visitor) -> None:
    print("====KEY.accept====")
    return visitor.visit_key(self)