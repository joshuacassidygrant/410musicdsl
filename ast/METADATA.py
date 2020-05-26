from libs.node import Node
from ast.ARRANGER import ARRANGER
from ast.TITLE import TITLE
from ast.TIME import TIME
from ast.TEMPO import TEMPO
from ast.COMPOSER import COMPOSER
from ast.YEAR import YEAR
from ast.KEY import KEY

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

        while (self.tokenizer.checkNext() and not self.tokenizer.checkToken("(seq|chord)")):

            nextToken = self.tokenizer.checkNext()
            metaType = metamap.get(nextToken, None)
            if metaType == None:
                print("Invalid meta " + nextToken)
            else:
                meta = metaType()
                meta.parse()
                self.metas.append(meta)





        return