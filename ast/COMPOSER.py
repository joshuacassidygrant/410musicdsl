from libs.node import Node
from ast.STRING import STRING
from libs.tokenizer import Tokenizer

#COMPOSER::= "Composer:" STRING

class COMPOSER(Node):

    # FIELDS:
    # composer

    def parse(self):
        self.tokenizer.getAndCheckNext("Composer:")
        self.composer = STRING()
        self.composer.parse()
        return