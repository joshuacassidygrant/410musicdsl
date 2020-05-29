import re

# Follows the same Tokenizer ideas from class
# UBC CPSC 410

class Tokenizer:
    program = None
    theTokenizer = None
    literals = None
    tokens = []
    currentToken = 0

    def __init__(self, program, literals):
        Tokenizer.program = program
        Tokenizer.literals = literals
        self.tokenize()

    @staticmethod
    def initProgram(program):
        Tokenizer.program = program

    @staticmethod
    def makeTokenizer(program, literals):
        if (Tokenizer.theTokenizer is None):
            Tokenizer.theTokenizer = Tokenizer(program, literals)

    @staticmethod
    def getTokenizer():
        print(Tokenizer.theTokenizer)
        return Tokenizer.theTokenizer

    def tokenize(self):
        tokenizedProgram = Tokenizer.program
        print("1: " + tokenizedProgram + "\n")

        tokenizedProgram = tokenizedProgram.replace('\n', '')
        tokenizedProgram = tokenizedProgram.strip()
        print("2: " + tokenizedProgram + "\n")

        for lit in Tokenizer.literals:
            tokenizedProgram = tokenizedProgram.replace(lit, "_" + lit + "_")

        tokenizedProgram = tokenizedProgram.replace("__", "_")
        print("3: " + tokenizedProgram + "\n")

        if (len(tokenizedProgram) > 0 and tokenizedProgram[0] == '_'):
            tokenizedProgram = tokenizedProgram[1:]

        tokens = tokenizedProgram.split('_')
        tokens = [t.strip() for t in tokens]
        tokens = [t for t in tokens if t != '']
        print("4: ", tokens, "\n")
        Tokenizer.tokens = tokens
        print("5: ", Tokenizer.tokens, "\n")

    def checkNext(self):
        token = ""
        if (Tokenizer.currentToken < len(Tokenizer.tokens)):
            token = Tokenizer.tokens[Tokenizer.currentToken]
        else:
            token = "NO_MORE_TOKENS"
        return token

    def getNext(self):
        token = ""
        if (Tokenizer.currentToken < len(Tokenizer.tokens)):
            token = Tokenizer.tokens[Tokenizer.currentToken]
            Tokenizer.currentToken += 1
        else:
            token = "NULLTOKEN"
        return token

    def checkToken(self, regexp):
        s = self.checkNext()
        print("comparing: |"+s+"|  to  |"+regexp+"|")
        return bool(re.match(regexp, s))

    def getAndCheckNext(self, regexp):
        s = self.getNext()
        if not bool(re.match(regexp, s)):
            message = "Unexpected next token for Parsing! Expected something matching: " + regexp + " but got: " + s
            raise Exception(message)
        print("matched: "+s+"  to  "+regexp)
        return s

    def moreTokens(self):
        return Tokenizer.currentToken < len(Tokenizer.tokens)

    def printProgram(self):
        print("=====Program=====\n" + Tokenizer.program)
