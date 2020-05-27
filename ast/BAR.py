from libs.node import Node
from ast.STAFF import STAFF
# BAR     ::= STAFF* 


class BAR(Node):

    # FIELDS:
    # list of staffs

    def parse(self):
        self.staffs = []
        while not self.tokenizer.checkToken("\-|\]"):
            staff = STAFF()
            staff.parse()
            self.staffs.append(staff)
        return
