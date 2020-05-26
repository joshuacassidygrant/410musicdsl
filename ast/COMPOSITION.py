from libs.node import Node
from ast.METADATA import METADATA
from ast.DECLARATION import DECLARATION
from ast.PLAY import PLAY

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

        while not self.tokenizer.checkToken("play"):
            token = self.tokenizer.getAndCheckNext("(seq|chord)")
            declaration = DECLARATION.makeDec(token)
            declaration.parse()
            self.declarations.append(declaration)

        self.play = PLAY()
        self.play.parse()

        if (self.tokenizer.moreTokens()):
            print("Still have tokens after play statement!")

        return