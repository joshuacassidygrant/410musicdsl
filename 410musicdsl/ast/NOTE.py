from libs.node import Node
from ast.LENGTH import LENGTH
from ast.PITCH import PITCH
from ast.APP_VISITOR import Visitor
# NOTE    ::= PITCH LENGTH


class NOTE(Node):
    # FIELDS
    # pitch
    # length

    def parse(self):
        token = self.tokenizer.getNext()
        self.pitch = PITCH()
        self.pitch.note = token[0]
        self.pitch.octave = token[1]
        self.length = LENGTH()
        self.length.value = token[2:]
        return

    def accept(self, visitor: Visitor) -> None:
        print("====NOTE.accept====")
        return visitor.visit_note(self)