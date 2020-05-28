from ast.TIME_SIG import TIME_SIG
from ast.META import META
from ast.APP_VISITOR import Visitor


class TIME(META):
  # FIELDS:
  # time

  def parse(self):
      self.tokenizer.getAndCheckNext("Time:")
      self.time = TIME_SIG()
      self.time.parse()
      return

  def accept(self, visitor: Visitor) -> None:
    print("====TIME.accept====")
    visitor.visit_time(self)
