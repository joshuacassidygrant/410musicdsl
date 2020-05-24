from Node import Node

# SET_SEQUENCE::= "seq " STRING "= [" ((BAR | SEQUENCE)"-")*(BAR | SEQUENCE)? "]"     // Sets new sequence variable with name STRING

class SEQUENCE(Node):

    # FIELDS:
    # list of bars or sequences

    def parse(self):
        #TODO
        return