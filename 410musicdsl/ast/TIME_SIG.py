from libs.node import Node
from ast.APP_VISITOR import Visitor
# TIMESIG ::= ("4/4" | "3/4")


class TIME_SIG(Node):
    # FIELDS:
    # value

    def parse(self):
        self.tokenizer.getAndCheckNext("\"")
        self.value = self.tokenizer.getAndCheckNext("((4\\/4)|(3\\/4))")
        self.tokenizer.getAndCheckNext("\"")
        return

    def accept(self, visitor: Visitor) -> None:
      print("====TIME_SIG.accept====")
      return visitor.visit_time_sig(self)