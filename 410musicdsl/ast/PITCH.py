from libs.node import Node
from ast.APP_VISITOR import Visitor
# PITCH	 ::=  ([A-G](#|b|)[0-8]


class PITCH(Node):
    # FIELDS:
    # note
    # octave

    def parse(self):
      token = self.tokenizer.getAndCheckNext("(([A-G]|R)(#|b|)[0-8])")
      self.note = token[0]
      self.octave = token[1]
      return

    def accept(self, visitor: Visitor) -> None:
      print("====PITCH.accept====")
      return visitor.visit_pitch(self)


    
