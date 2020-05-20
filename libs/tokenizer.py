import re

class Tokenizer:
  tokenizer = None

  def __init__(self, program, literals):
    self.program = program
    self.literals = literals

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

  def printProgram(self):
    print("=====Program=====n" + self.program)

