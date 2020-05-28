from libs.node import Node
from ast.STRING import STRING
# COMPOSER::= "Composer:" STRING


class COMPOSER(Node):
    # FIELDS:
    # composer

    def parse(self):
        self.tokenizer.getAndCheckNext("Composer:")
        self.composer = STRING()
        self.composer.parse()
        print("parsed composer: ", self.composer.toString())
        return
