
from libs.tokenizer import Tokenizer

def main():
  literals = ["Title:", "Time:", "Tempo:", "Composer:", "Arranged by:", "Key:", "seq", "main", "= [", "|T|", "|B|", "||", "]", ",", "\""]
  program = open("test-input.mz", "r").read()

  print("Tokenizer program before: ", Tokenizer.program)
  Tokenizer.initProgram(program)
  print("Tokenizer program after: ", Tokenizer.program)


  print ("===NON SINGLETON STARTS HERE===")
  t = Tokenizer(program, literals)
  t.tokenize()
  print("=====Done tokenizing=====")

if __name__ == '__main__':
  main()