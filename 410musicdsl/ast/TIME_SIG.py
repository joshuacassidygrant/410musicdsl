from libs.node import Node
# TIMESIG ::= ("4/4" | "3/4")


class TIME_SIG(Node):
    # FIELDS:
    # value

    def parse(self):
        self.tokenizer.getAndCheckNext("\"")
        self.value = self.tokenizer.getAndCheckNext("((4\\/4)|(3\\/4))")
        self.tokenizer.getAndCheckNext("\"")
        return
