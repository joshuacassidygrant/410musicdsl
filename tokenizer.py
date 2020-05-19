import re

test = open("test-input.mz", "r")
program = test.read()
print(program)

literals = ["Title:", "Time:", "Tempo:", "Composer:", "Arranged by:", "Key:", "seq", "main", "= [", "|T|", "|B|", "||", "]", ","]

class Tokenizer:

  def __init__(self, program):
    self.program = program

  def printProgram(self):
    print("======Program======\n" + self.program)

  def tokenize(self):
    tokenizedProgram = self.program
    tokenizedProgram = tokenizedProgram.replace('\n', '')
    print(tokenizedProgram)

    for l in literals:
      tokenizedProgram = tokenizedProgram.replace(l, "_" + l + "_")
    

    tokenizedProgram = tokenizedProgram.replace("__", "_")

    if (len(tokenizedProgram) > 0 and tokenizedProgram[0] == '_'):
      tokenizedProgram = tokenizedProgram[1:]

    tokens = tokenizedProgram.split('_')
    for t in tokens:
      print(t)

  

t = Tokenizer(program)
t.printProgram()
t.tokenize()