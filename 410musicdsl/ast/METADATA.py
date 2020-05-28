from libs.node import Node
from ast.ARRANGER import ARRANGER
from ast.TITLE import TITLE
from ast.TIME import TIME
from ast.TEMPO import TEMPO
from ast.COMPOSER import COMPOSER
from ast.YEAR import YEAR
from ast.KEY import KEY
from ast.APP_VISITOR import Visitor
# METADATA::= META*

metamap = {
    "Title:": TITLE,
    "Time:": TIME,
    "Tempo:": TEMPO,
    "Arranged by:": ARRANGER,
    "Composer:": COMPOSER,
    "Year:": YEAR,
    "Key:": KEY
}


class METADATA(Node):
    # FIELDS
    # list of meta

    def parse(self):
        self.metas = []
        while self.tokenizer.checkNext()\
                and not self.tokenizer.checkToken("(seq|chord)"):
            nextToken = self.tokenizer.checkNext()
            metaType = metamap.get(nextToken, None)
            if metaType is None:
                # print("Invalid meta " + nextToken)
                raise Exception(f"Invalid meta {nextToken}")
            else:
                print(f"\n============== Parsing {nextToken}\n")
                meta = metaType()
                meta.parse()
                self.metas.append(meta)
                print(f"\n============== {nextToken} added to meta list\n")

        return

    def accept(self, visitor: Visitor) -> None:
      print("====METADATA.accept====")
      return visitor.visit_meta_data(self)