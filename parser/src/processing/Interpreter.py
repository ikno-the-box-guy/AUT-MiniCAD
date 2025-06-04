from antlr4 import *
from gen.CadLexer import CadLexer
from gen.CadParser import CadParser
from src.processing.VisitorImpl import VisitorImpl


def interpret(text):
    input_stream = InputStream(text)
    lexer = CadLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CadParser(stream)
    tree = parser.start_()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
        return []
    else:
        commands = VisitorImpl().visit(tree)
        return commands
