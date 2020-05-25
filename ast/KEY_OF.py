from libs.node import Node
# KEYOF   ::= ([A-G](b|#|)(maj|min))   

class KEY_OF(Node):

    # FIELDS:
    # value

    def parse(self):
        self.tokenizer.getAndCheckNext("\"")
        # todo
        self.tokenizer.getAndCheckNext("\"")
        return