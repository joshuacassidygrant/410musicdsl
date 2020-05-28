from libs.node import Node
from ast.STRING import STRING
from ast.APP_VISITOR import Visitor
# COMPOSER::= "Composer:" STRING


class COMPOSER(Node):
  # FIELDS:
  # composer

  def parse(self):
    self.tokenizer.getAndCheckNext("Composer:")
    self.tokenizer.getAndCheckNext("\"")
    self.value = self.tokenizer.getNext()
    self.tokenizer.getAndCheckNext("\"")
    return

  def accept(self, visitor: Visitor) -> None:
    print("====COMPOSER.accept====")
    return visitor.visit_composer(self)

  def toString(self):
    return self.value