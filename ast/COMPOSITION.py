from libs.node import Node
from ast.METADATA import METADATA

# COMPOSITION ::= METADATA DECLARATION*

class COMPOSITION(Node):

    # FIELDS:
    # metadata
    # list of declarations

    def parse(self):
        self.metadata = METADATA()
        self.declarations = []

        self.metadata.parse()

        for declaration in self.declarations:
            declaration.parse()

        return