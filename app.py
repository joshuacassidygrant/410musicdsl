
from libs.tokenizer import Tokenizer

def main():
  literals = ["Title:", "Time:", "Tempo:", "Composer:", "Arranged by:", "Key:", "seq", "main", "= [", "|T|", "|B|", "||", "]", ",", "\""]
  program = open("test-input.mz", "r").read()
  t = Tokenizer(program, literals)
  t.tokenize()
  print("=====Done tokenizing=====")

if __name__ == '__main__':
  main()