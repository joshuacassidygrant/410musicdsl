from ast.TIME_SIG import TIME_SIG
from ast.META import META
from ast.APP_VISITOR import Visitor


class TIME(META):
  # FIELDS:
  # time

  def parse(self):
      self.tokenizer.getAndCheckNext("Time:")
      self.tokenizer.getAndCheckNext("\"")
      self.value = self.tokenizer.getAndCheckNext("((4\\/4)|(3\\/4))")
      self.tokenizer.getAndCheckNext("\"")
      return

  def accept(self, visitor: Visitor) -> None:
    print("====TIME.accept====")
    return visitor.visit_time(self)
