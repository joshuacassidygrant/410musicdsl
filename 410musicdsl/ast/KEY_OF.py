from libs.node import Node
from ast.APP_VISITOR import Visitor
# KEYOF   ::= ([A-G](b|#|)(maj|min))


class KEY_OF(Node):
    # FIELDS:
    # value

    def parse(self):
        self.tokenizer.getAndCheckNext("\"")
        self.key_of = self.tokenizer.getAndCheckNext("([A-G](b|#|)(maj|min))")
        print("INSIDE KEY OF")
        self.tokenizer.getAndCheckNext("\"")
        return

    def accept(self, visitor: Visitor) -> None:
        print("====KEY_OF.accept====")
        visitor.key_of(self)
