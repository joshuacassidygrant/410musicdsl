from libs.node import Node
# NAME    ::=


class NAME(Node):

    # FIELDS
    # value

    def parse(self):
        self.value = self.tokenizer.getAndCheckNext("[^\"]*")
        return
