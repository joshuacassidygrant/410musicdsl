
from libs.tokenizer import Tokenizer
from temp import Program, Node

def main():
  literals = ["Title:", "Time:", "Tempo:", "Composer:", "Arranged by:", "Key:", "Year:", "{", "}", "(", ")", "seq", "main", "= [", "|T|", "|B|", "||", "]", ",", "\"", "//", "$(", ")"]
  program = open("test-input2.mz", "r").read()
  Tokenizer.makeTokenizer(program, literals)
  p = Program()
  print("=====Done tokenizing=====\n")
  p.test()


if __name__ == '__main__':
  main()