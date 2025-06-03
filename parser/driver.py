import sys
from antlr4 import *
from gen.CadLexer import CadLexer
from gen.CadParser import CadParser
from TreeView import build_treeview


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CadLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CadParser(stream)
    tree = parser.start_()

    build_treeview(tree, parser.ruleNames)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main(["driver.py", "input.txt"])
    else:
        main(sys.argv)
