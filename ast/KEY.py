from libs.node import Node
from ast.KEY_OF import KEY_OF

# KEY     ::= "Key:" KEYOF

class KEY(Node):

    # FIELDS:
    # key

    def parse(self):
        self.tokenizer.getAndCheckNext("Key:")
        self.key = KEY_OF()
        self.key.parse()
        return