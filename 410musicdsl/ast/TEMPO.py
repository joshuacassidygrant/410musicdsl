from libs.node import Node
from ast.INTEGER import INTEGER
from ast.APP_VISITOR import Visitor


class TEMPO(Node):
  # FIELDS:
  # tempo

  def parse(self):
      self.tokenizer.getAndCheckNext("Tempo:")
      self.value = self.tokenizer.getAndCheckNext("\\d+")
      return

  def accept(self, visitor: Visitor) -> None:
    print("====TEMPO.accept====")
    return visitor.visit_tempo(self)