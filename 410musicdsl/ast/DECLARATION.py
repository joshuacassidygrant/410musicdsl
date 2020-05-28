from libs.node import Node
from ast.SET_SEQUENCE import SET_SEQUENCE
from ast.SET_CHORD import SET_CHORD
from ast.APP_VISITOR import Visitor

decmap = {
    "seq": SET_SEQUENCE,
    "chord": SET_CHORD
}

class DECLARATION(Node):

  @staticmethod
  def makeDec(token):
    metaType = decmap.get(token, None)
    if metaType is None:
        print("Invalid meta " + token)
        return None
    else:
        return metaType()

  def parse(self):
    return
    
  def accept(self, visitor: Visitor) -> None:
    print("====DECLARATION.accept====")
    return visitor.visit_declaration(self)