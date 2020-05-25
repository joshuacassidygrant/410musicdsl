from libs.node import Node
from ast.ARRANGER import ARRANGER
from ast.TITLE import TITLE
from ast.TIME import TIME
from ast.TEMPO import TEMPO
from ast.COMPOSER import COMPOSER

# METADATA::= META*

metamap = {
    "Title:": TITLE(),
    "Time:": TIME(),
    "Tempo:": TEMPO(),
    "Arranged by:": ARRANGER(),
    "Composer:": COMPOSER(),

}

class METADATA(Node):

    # FIELDS
    # list of meta



    def parse(self):
        
        self.metas = []

        while (self.tokenizer.checkNext() and not self.tokenizer.checkToken("(seq|chord)")):

            nextToken = self.tokenizer.checkNext()
            print(nextToken)
            meta = metamap.get(nextToken, None)
            print(meta)
            if meta == None:
                # throw an error
                raise "Invalid meta!"
            
            meta.parse()
            self.metas.append(meta)





        return