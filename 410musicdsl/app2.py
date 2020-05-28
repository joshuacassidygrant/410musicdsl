import os
from libs.tokenizer import Tokenizer
from ast.COMPOSITION import COMPOSITION
from ast.APP_EVALUATOR import Evaluator

def open_file():
    # For accessing the file in a folder contained in the current folder
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir, '410musicdsl/data/test-input-p.mz')
    return open(filename, "r").read()


def main():
    literals = [
        "Title:", "Time:", "Tempo:", "Composer:", "Arranged by:",
        "Key:", "Year:", "{", "}", "(", ")", "seq", "play", "chord",
        "= [", "|T|", "|B|", "||", "]", ",", "\"", "//", "$(", ")", "("
    ]

    # Tokenizing
    print("Starting TOKENIZING")
    program = open_file()

    Tokenizer.makeTokenizer(program, literals)
    p = COMPOSITION()
    print("Completed TOKENIZING")

    # Parsing
    print("Starting PARSING")
    p.parse()
    print("Completed PARSING")

    print("Starting EVALUATION")
    # TODO
    print("Completed EVALUATION")

if __name__ == '__main__':
    main()
