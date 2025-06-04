import sys
from antlr4 import *
from gen.CadLexer import CadLexer
from gen.CadParser import CadParser
from TreeView import build_treeview
from src.processing.VisitorImpl import VisitorImpl


def main(argv):
    # input_stream = FileStream(argv[1])
    input_stream = InputStream("CLEAR #FF0000;RECT 10 10 20 20")
    lexer = CadLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CadParser(stream)
    tree = parser.start_()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax errors detected.")
        return
    else:
        commands = VisitorImpl().visit(tree)
        print("Commands:", commands)

    build_treeview(tree, parser.ruleNames)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main(["driver.py", "input.txt"])
    else:
        main(sys.argv)
