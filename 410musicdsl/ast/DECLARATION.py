from libs.node import Node
from ast.SET_SEQUENCE import SET_SEQUENCE
from ast.SET_CHORD import SET_CHORD

decmap = {
    "seq": SET_SEQUENCE,
    "chord": SET_CHORD
}


class DECLARATION(Node):

    @staticmethod
    def makeDec(token):
        metaType = decmap.get(token, None)
        if metaType is None:
            print("Invalid meta " + token)
            return None
        else:
            return metaType()

    def parse(self):
        return
