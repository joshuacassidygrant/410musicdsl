import re

class Tokenizer:

    tokenizer = None

    def __init__(self):
        self.nextToken = "4/4"

    @staticmethod
    def getTokenizer():
        if (Tokenizer.tokenizer == None):
            Tokenizer.tokenizer = Tokenizer()
        else:
            return Tokenizer.tokenizer

    def getAndCheckNext(self, regex):
        res = re.search(regex, self.nextToken)
        if (res == None):
            print("none")
        else: 
            return re.search(regex, self.nextToken)[0].string
        

    def checkNext(self, regex):
        res = re.search(regex, self.nextToken)
        return (res != None and len(re.search(regex, self.nextToken)) == 1)
        

    def getNext(self):
        return self.nextToken