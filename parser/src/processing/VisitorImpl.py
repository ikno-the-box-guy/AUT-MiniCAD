from gen.CadParser import CadParser
from gen.CadVisitor import CadVisitor
from src.commands.BorderCommand import BorderCommand
from src.commands.ClearCommand import ClearCommand
from src.commands.EllipseCommand import EllipseCommand
from src.commands.FillCommand import FillCommand
from src.commands.LineCommand import LineCommand
from src.commands.RectangleCommand import RectangleCommand
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

    def visitEllipseCommand(self, ctx:CadParser.EllipseCommandContext):
        position = self.visit(ctx.position())
        size = self.visit(ctx.size())
        return EllipseCommand("ELLIPSE", [position, size])

    def visitRectangleCommand(self, ctx:CadParser.RectangleCommandContext):
        position = self.visit(ctx.position())
        size = self.visit(ctx.size())
        return RectangleCommand("RECT", [position, size])

    def visitStart_(self, ctx: CadParser.Start_Context):
        commands = []
        for i in range(0, ctx.getChildCount(), 2):
            commands.append(self.visit(ctx.getChild(i)))
        return commands
