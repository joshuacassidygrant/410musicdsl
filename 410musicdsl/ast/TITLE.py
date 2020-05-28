from ast.META import META
from ast.STRING import STRING
from ast.APP_VISITOR import Visitor

class TITLE(META):
  # FIELDS:
  # title

  def parse(self):
    self.tokenizer.getAndCheckNext("Title:")
    self.title = STRING()
    self.title.parse()
    return

  def accept(self, visitor: Visitor) -> None:
    print("====TITLE.accept====")
    visitor.visit_title(self)
  
