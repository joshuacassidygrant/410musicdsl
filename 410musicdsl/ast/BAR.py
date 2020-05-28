from libs.node import Node
from ast.STAFF import STAFF
from ast.APP_VISITOR import Visitor
# BAR     ::= STAFF*

class BAR(Node):
  # FIELDS:
  # list of staffs

  def parse(self):
    self.staffs = []
    while not self.tokenizer.checkToken("-|\\]"):
      staff = STAFF()
      staff.parse()
      self.staffs.append(staff)
      print("ADDING A STAFF TO BAR: ", self.staffs)
    print(self.tokenizer.checkNext())
    return

  def accept(self, visitor: Visitor) -> None:
    print("====BAR.accept====")
    return visitor.visit_bar(self)
