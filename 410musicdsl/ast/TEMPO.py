from libs.node import Node
from ast.INTEGER import INTEGER
from ast.APP_VISITOR import Visitor


class TEMPO(Node):
  # FIELDS:
  # tempo

  def parse(self):
      self.tokenizer.getAndCheckNext("Tempo:")
      self.tempo = INTEGER()
      self.tempo.parse()
      return

  def accept(self, visitor: Visitor) -> None:
    print("====TEMPO.accept====")
    visitor.visit_tempo(self)