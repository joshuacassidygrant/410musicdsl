from ast.TIME_SIG import TIME_SIG
from ast.META import META


class TIME(META):
    # FIELDS:
    # time

    def parse(self):
        self.tokenizer.getAndCheckNext("Time:")
        self.time = TIME_SIG()
        self.time.parse()
        return
