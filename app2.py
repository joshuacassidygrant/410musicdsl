from libs.tokenizer import Tokenizer
from ast.COMPOSITION import COMPOSITION

def main():
  literals = ["Title:", "Time:", "Tempo:", "Composer:", "Arranged by:", "Key:", "Year:", "{", "}", "(", ")", "seq", "play", "chord", "= [", "|T|", "|B|", "||", "]", ",", "\"", "//", "$(", ")"]
  program = open("test-input-p.mz", "r").read()
  Tokenizer.makeTokenizer(program, literals)
  p = COMPOSITION() 
  print("=====Done tokenizing=====\n")
  p.parse()


if __name__ == '__main__':
  main()