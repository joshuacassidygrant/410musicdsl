from libs.node import Node
from ast.METADATA import METADATA
from ast.DECLARATION import DECLARATION

# COMPOSITION ::= METADATA DECLARATION*

class COMPOSITION(Node):

    # FIELDS:
    # metadata
    # list of declarations
    # play

    def parse(self):
        self.metadata = METADATA()
        self.declarations = []

        self.metadata.parse()

        while not self.tokenizer.checkNext("play"):
            token = self.tokenizer.getAndCheckNext("(seq|chord)")
            print(token)
            #declaration.parse()

        self.tokenizer.getAndCheckNext("play")
        self.play = self.tokenizer.getNext()

        if (self.tokenizer.moreTokens):
            print("Still have tokens after play statement!")

        return