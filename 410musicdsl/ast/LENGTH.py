from libs.node import Node
from ast.APP_VISITOR import Visitor
# LENGTH ::=  \.?(s|e|q|h|w)


class LENGTH(Node):
    # FIELDS:
    # value

    def parse(self):
        self.value = self.tokenizer.getAndCheckNext("(\\.?(s|e|q|h|w))")
        return

    def accept(self, visitor: Visitor) -> None:
        print("====LENGTH.accept====")
        return visitor.visit_length(self)