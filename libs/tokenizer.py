import re

class Tokenizer:
  program = None
  theTokenizer = None
  literals = None
  tokens = None
  currentToken = 0

  def __init__(self, program, literals):
    self.program = program
    self.literals = literals

  @staticmethod
  def initProgram(program):
    Tokenizer.program = program

  def makeTokenizer(self, program, literals):
    if (Tokenizer.theTokenizer == None):
      theTokenizer = Tokenizer(program, literals)

  def getTokenizer(self):
    return Tokenizer

  def tokenize(self):
    tokenizedProgram = self.program
    print(tokenizedProgram)

    tokenizedProgram = tokenizedProgram.replace('\n', '')
    tokenizedProgram = tokenizedProgram.strip()
    print(tokenizedProgram)

    for l in self.literals:
      tokenizedProgram = tokenizedProgram.replace(l, "_" + l + "_")
    
    tokenizedProgram = tokenizedProgram.replace("__", "_")
    print(tokenizedProgram)

    if (len(tokenizedProgram) > 0 and tokenizedProgram[0] == '_'):
      tokenizedProgram = tokenizedProgram[1:]

    tokens = tokenizedProgram.split('_')

    tokens = [t.strip() for t in tokens]
    tokens = [t for t in tokens if t != '']
    print(tokens)

  @staticmethod
  def printProgram():
    print("WAS CALLED")
    print("=====Program=====/n" + Tokenizer.program)

