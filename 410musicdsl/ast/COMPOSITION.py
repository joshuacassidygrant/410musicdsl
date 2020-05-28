from libs.node import Node
from ast.METADATA import METADATA
from ast.DECLARATION import DECLARATION
from ast.PLAY import PLAY
from ast.APP_VISITOR import Visitor
# COMPOSITION ::= METADATA DECLARATION*


class COMPOSITION(Node):
    # FIELDS:
    # metadata
    # list of declarations
    # play

    def parse(self):
        self.__parse_metadata()
        self.__parse_declaration()
        self.__parse_play()
        self.__parse_more_tokens()
        return

    def __parse_metadata(self):
        self.metadata = METADATA()
        self.declarations = []
        self.metadata.parse()

    def __parse_declaration(self):
        while not self.tokenizer.checkToken("play"):
            token = self.tokenizer.getAndCheckNext("(seq|chord)")
            declaration = DECLARATION.makeDec(token)
            declaration.parse()
            self.declarations.append(declaration)
        return

    def __parse_play(self):
        self.play = PLAY()
        self.play.parse()
        # Check if NAME in "play NAME" is defined in self.declarations
        exists = False
        for dec in self.declarations:
            print(f"Declaration Name: {dec.name.value}")
            if dec.name.value == self.play.name.value:
                exists = True

        if (not exists):
            raise Exception(f"Variable {self.play.name} does not exist")
        return

    def __parse_more_tokens(self):
        if (self.tokenizer.moreTokens()):
            # print("Still have tokens after play statement!")
            raise Exception("More tokens defined after play not allowed.")
        return

    def accept(self, visitor: Visitor) -> None:
      print("====COMPOSITION.accept====")
      return visitor.visit_composition(self)