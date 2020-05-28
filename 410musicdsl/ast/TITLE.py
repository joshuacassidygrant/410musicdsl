from ast.META import META
from ast.STRING import STRING
from ast.APP_VISITOR import Visitor

class TITLE(META):
  # FIELDS:
  # title

  def parse(self):
    self.tokenizer.getAndCheckNext("Title:")
    self.tokenizer.getAndCheckNext("\"")
    self.value = self.tokenizer.getNext()
    self.tokenizer.getAndCheckNext("\"")
    return

  def accept(self, visitor: Visitor) -> None:
    print("====TITLE.accept====")
    return visitor.visit_title(self)

  def toString(self):
    return self.value
  
