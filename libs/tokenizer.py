import re

class Tokenizer:
  program = None
  theTokenizer = None
  literals = None
  tokens = None
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
    if (Tokenizer.theTokenizer == None):
      theTokenizer = Tokenizer(program, literals)

  def getTokenizer(self):
    return Tokenizer

  def tokenize(self):
    tokenizedProgram = Tokenizer.program
    print("1: " + tokenizedProgram)

    tokenizedProgram = tokenizedProgram.replace('\n', '')
    tokenizedProgram = tokenizedProgram.strip()
    print("2: " + tokenizedProgram)

    for l in Tokenizer.literals:
      tokenizedProgram = tokenizedProgram.replace(l, "_" + l + "_")
    
    tokenizedProgram = tokenizedProgram.replace("__", "_")
    print("3: " + tokenizedProgram)

    if (len(tokenizedProgram) > 0 and tokenizedProgram[0] == '_'):
      tokenizedProgram = tokenizedProgram[1:]

    tokens = tokenizedProgram.split('_')
    tokens = [t.strip() for t in tokens]
    tokens = [t for t in tokens if t != '']
    print("4: ", tokens)
    Tokenizer.tokens = tokens
    print("5: ", Tokenizer.tokens)

  @staticmethod
  def printProgram():
    print("WAS CALLED")
    print("=====Program=====/n" + Tokenizer.program)

