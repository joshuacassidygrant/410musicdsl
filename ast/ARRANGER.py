from libs.node import Node
from ast.STRING import STRING

# ARRANGER::= "Arranged by:" STRING


class ARRANGER(Node):

    # FIELDS:
    # arranger

    def parse(self):
        self.tokenizer.getAndCheckNext("Arranged by:")
        self.arranger = STRING()
        self.arranger.parse()
        return
