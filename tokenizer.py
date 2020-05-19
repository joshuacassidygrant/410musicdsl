test = open("test-input.mz", "r")
program = test.read()
print(program)

class Tokenizer:
  def __init__(self, program):
    self.program = program

  def printProgram(self):
    print("======Program======\n" + self.program)

t = Tokenizer(program)
t.printProgram()