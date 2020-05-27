from libs.node import Node
# TIMESIG ::= ("4/4" | "3/4")


class TIME_SIG(Node):

    # FIELDS:

    def parse(self):
        self.tokenizer.getAndCheckNext("\"")
        self.value = self.tokenizer.getAndCheckNext("4/4")  #TODO - figure out regex
        self.tokenizer.getAndCheckNext("\"")
        return