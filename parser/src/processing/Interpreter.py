from antlr4 import *
from gen.CadLexer import CadLexer
from gen.CadParser import CadParser
from src.processing.VisitorImpl import VisitorImpl


def interpret_text(text):
    input_stream = InputStream(text)
    return interpret(input_stream)


def interpret_file(file_path):
    input_stream = FileStream(file_path)
    return interpret(input_stream)


def interpret(input_stream):
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
