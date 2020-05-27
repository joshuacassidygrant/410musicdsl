from ast.META import META
from ast.STRING import STRING


class TITLE(META):
    # FIELDS:
    # title

    def parse(self):
        self.tokenizer.getAndCheckNext("Title:")
        self.title = STRING()
        self.title.parse()
        return
