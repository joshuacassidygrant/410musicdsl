from libs.node import Node
# INTEGER ::= \d+


class INTEGER(Node):

    # FIELDS:
    # value

    def parse(self):
        self.value = self.tokenizer.getAndCheckNext("\\d+")
        return
