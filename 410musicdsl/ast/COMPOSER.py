from libs.node import Node
from ast.STRING import STRING
from ast.APP_VISITOR import Visitor
# COMPOSER::= "Composer:" STRING


class COMPOSER(Node):
  # FIELDS:
  # composer

  def parse(self):
    self.tokenizer.getAndCheckNext("Composer:")
    self.composer = STRING()
    self.composer.parse()
    print("parsed composer: ", self.composer.toString())
    return

  def accept(self, visitor: Visitor) -> None:
    print("====COMPOSER.accept====")
    visitor.visit_composer(self)