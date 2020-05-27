from abc import ABC, abstractmethod
from libs.tokenizer import Tokenizer


class Node(ABC):

    def __init__(self):
        self.tokenizer = Tokenizer.getTokenizer()

    @abstractmethod
    def parse(self): pass

    @abstractmethod
    def evaluate(self): pass

    # Test abstract class
    @abstractmethod
    def test(self): print(self.tokenizer.program)


# TODO: REMOVE (PROGRAM in ast module)
class Program(Node):
    def parse(self):
        return super().parse()

    def evaluate(self):
        return super().evaluate()

    def test(self):
        return super().test()
