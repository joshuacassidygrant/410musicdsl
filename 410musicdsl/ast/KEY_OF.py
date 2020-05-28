from libs.node import Node
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
