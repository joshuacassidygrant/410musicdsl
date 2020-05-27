from libs.node import Node
from ast.NOTE import NOTE
from ast.CHORD import CHORD
# STAFF ::= ("||" | "|" ("T"|"B") "|" (SOUND ,)* SOUND"||"


class STAFF(Node):
    # FIELDS:
    # clef (T or B)
    # list of sounds

    def parse(self):
        self.clef = self.tokenizer.getAndCheckNext("\\|(T|B)\\|")
        self.sounds = []

        while not self.tokenizer.checkToken("\\|\\|"):
            if self.tokenizer.checkToken("{"):
                chord = CHORD()
                chord.parse()
                self.sounds.append(chord)
            elif self.tokenizer.checkToken("(([A-G]|R)(#|b|)[0-8]\\.?\\w)"):
                note = NOTE()
                note.parse()
                self.sounds.append(note)
                if self.tokenizer.checkToken(","):
                    self.tokenizer.getNext()

        self.tokenizer.getNext()
        return
