from libs.tokenizer import Tokenizer
from ast.COMPOSITION import COMPOSITION


def main():
    literals = [
        "Title:", "Time:", "Tempo:", "Composer:", "Arranged by:",
        "Key:", "Year:", "{", "}", "(", ")", "seq", "play", "chord",
        "= [", "|T|", "|B|", "||", "]", ",", "\"", "//", "$(", ")"
    ]

    # Tokenizing
    print("Starting TOKENIZING")
    program = open("test-input-p.mz", "r").read()
    Tokenizer.makeTokenizer(program, literals)
    p = COMPOSITION()
    print("Completed TOKENIZING")

    # Parsing
    print("Starting PARSING")
    p.parse()
    print("Completed PARSING")


if __name__ == '__main__':
    main()
