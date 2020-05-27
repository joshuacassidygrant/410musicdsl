from libs.node import Node
# LENGTH ::=  \.?(s|e|q|h|w)

class LENGTH(Node):

    # FIELDS:
    # value

    def parse(self):
        self.value = self.tokenizer.getAndCheckNext("(\.?(s|e|q|h|w))")
        return