from libs.node import Node
# STRING  ::= ([^"]*)


class STRING(Node):

    # FIELDS:
    # value

    def parse(self):
        self.tokenizer.getAndCheckNext("\"")
        self.value = self.tokenizer.getNext()
        print("INSIDE STRING SELF: " + self.value)
        self.tokenizer.getAndCheckNext("\"")
        return

    def toString(self):
      return self.value