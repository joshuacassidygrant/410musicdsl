from libs.node import Node
# STRING  ::= ([^"]*)  


class STRING(Node):

    # FIELDS:
    # value

    def parse(self):
        self.tokenizer.getAndCheckNext("\"")
        self.value = self.tokenizer.getNext()
        self.tokenizer.getAndCheckNext("\"")
        return