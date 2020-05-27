from libs.node import Node
from ast.LENGTH import LENGTH
from ast.PITCH import PITCH
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
