import re

test = open("test-input.mz", "r")
program = test.read()
print(program)

literals = ["Title:", "Time:", "Tempo", "Composer", "Arranged by", "Key", "seq", "main", "= [", "|T|", "|B|", "||", "]", ","]

class Tokenizer:

  def __init__(self, program):
    self.program = program

  def printProgram(self):
    print("======Program======\n" + self.program)

  def tokenize(self):
    tokenizedProgram = self.program + "TOKENIZED"
    tokenizedProgram = tokenizedProgram.replace('\n', '')
    print(tokenizedProgram)

    for l in literals:
      tokenizedProgram = tokenizedProgram.replace(l, "_" + l + "_")
    
    print("REPLACED RW====================\n" + tokenizedProgram)


t = Tokenizer(program)
t.printProgram()
t.tokenize()