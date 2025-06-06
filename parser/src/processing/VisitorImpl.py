from gen.CadParser import CadParser
from gen.CadVisitor import CadVisitor
from src.commands.BorderCommand import BorderCommand
from src.commands.ClearCommand import ClearCommand
from src.commands.EllipseCommand import EllipseCommand
from src.commands.FileCommand import FileCommand
from src.commands.FillCommand import FillCommand
from src.commands.LineCommand import LineCommand
from src.commands.PolygonCommand import PolygonCommand
from src.commands.RectangleCommand import RectangleCommand
from src.commands.UndoCommand import UndoCommand
from src.commands.WidthCommand import WidthCommand


class VisitorImpl(CadVisitor):
    def visitPosition(self, ctx: CadParser.PositionContext):
        return self.visit(ctx.int_(0)), self.visit(ctx.int_(1))

    def visitSize(self, ctx: CadParser.SizeContext):
        return self.visit(ctx.int_(0)), self.visit(ctx.int_(1))

    def visitInt(self, ctx: CadParser.IntContext):
        return int(ctx.getText())

    def visitColor(self, ctx: CadParser.ColorContext):
        return ctx.getText()

    def visitFilepath(self, ctx:CadParser.FilepathContext):
        return ctx.getText().strip('"')

    # Commands
    def visitClearCommand(self, ctx: CadParser.ClearCommandContext):
        return ClearCommand("CLEAR", [self.visit(ctx.color())])

    def visitBorderCommand(self, ctx: CadParser.BorderCommandContext):
        return BorderCommand("BORDER", [self.visit(ctx.color())])

    def visitFillCommand(self, ctx: CadParser.FillCommandContext):
        return FillCommand("FILL", [self.visit(ctx.color())])

    def visitWidthCommand(self, ctx: CadParser.WidthCommandContext):
        return WidthCommand("WIDTH", [self.visit(ctx.int_())])

    def visitLineCommand(self, ctx: CadParser.LineCommandContext):
        start = self.visit(ctx.position(0))
        end = self.visit(ctx.position(1))
        return LineCommand("LINE", [start, end])

    def visitEllipseCommand(self, ctx: CadParser.EllipseCommandContext):
        position = self.visit(ctx.position())
        size = self.visit(ctx.size())
        return EllipseCommand("ELLIPSE", [position, size])

    def visitRectangleCommand(self, ctx: CadParser.RectangleCommandContext):
        position = self.visit(ctx.position())
        size = self.visit(ctx.size())
        return RectangleCommand("RECT", [position, size])

    def visitPolygonCommand(self, ctx: CadParser.PolygonCommandContext):
        points = [self.visit(point) for point in ctx.position()]
        return PolygonCommand("POLYGON", points)

    def visitFileCommand(self, ctx: CadParser.FileCommandContext):
        filepath = self.visit(ctx.filepath())
        return FileCommand("FILE", [filepath])

    def visitUndoCommand(self, ctx: CadParser.UndoCommandContext):
        return UndoCommand("UNDO", [])

    def visitStart_(self, ctx: CadParser.Start_Context):
        commands = []
        for cmd in ctx.cmd():
            commands.append(self.visit(cmd))
        return commands
