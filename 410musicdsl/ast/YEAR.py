from ast.INTEGER import INTEGER
from ast.META import META
from ast.APP_VISITOR import Visitor

class YEAR(META):
  # FIELDS:
  # year

  def parse(self):
    self.tokenizer.getAndCheckNext("Year:")
    self.tempo = INTEGER()
    self.tempo.parse()
    return

  def accept(self, visitor: Visitor) -> None:
    print("====YEAR.accept====")
    visitor.visit_year(self)