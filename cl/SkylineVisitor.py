# Generated from Skyline.g by ANTLR 4.7.1
from antlr4 import *
from skyline import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced
# by SkylineParser.

# Auxiliar functions


def valid_skyline(a, b, c):
    if a >= c or b < 0:
        return False
    return True


def get_values_building(text):
    aux = []
    start = 1
    for i in range(1, len(text)):
        if text[i] == ',' or text[i] == ')':
            aux.append(int(text[start:i]))
            start = i + 1
    return aux


class SkylineVisitor(ParseTreeVisitor):
    def __init__(self, table):
        self.table = table
    # Visit a parse tree produced by SkylineParser#root.

    def visitRoot(self, ctx: SkylineParser.RootContext):
        n = next(ctx.getChildren())
        return self.visit(n)
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx: SkylineParser.ExprContext):
        l = [n for n in ctx.getChildren()]
        # print("dd")
        if len(l) == 1:
            # nombre
            text = l[0].getText()
            if (text[0] == '-' and text[1] >= '0' and text[1]
                    <= '9') or (text[0] >= '0' and text[0] <= '9'):
                return int(text)
            # identificador
            if (text[0] >= 'a' and text[0] <= 'z') or (
                    text[0] >= 'A' and text[0] <= 'Z'):
                return text
            if text[0] == '(':
                aux = get_values_building(text)
                if not valid_skyline(aux[0], aux[1], aux[2]):
                    return "EXPRESSIO INCORRECTA"
                return Skyline((aux[0], aux[1], aux[2]))
            if text[0] == '{':
                aux = []
                start = 1
                for i in range(1, len(text)):
                    if text[i] == ',' or text[i] == '}':
                        aux.append(int(text[start:i]))
                        start = i + 1
                if aux[0] < 0 or aux[1] < 0 or aux[2] < 1 or (
                        aux[3] >= aux[4]):
                    return "EXPRESSIO INCORRECTA"
                return Skyline([aux[0], aux[1], aux[2], aux[3], aux[4]])
            if text[0] == '[':
                aux_list = []
                start = 1
                i = 1
                while i < len(text):
                    if text[i] == ')':
                        v = get_values_building(text[start:i + 1])
                        if not valid_skyline(v[0], v[1], v[2]):
                            return "EXPRESSIO INCORRECTA"
                        aux_list.append([v[0], v[2], v[1]])
                        start = i + 2
                        if start < len(text) and text[start] == ' ':
                            start += 1
                    i += 1

                return Skyline(aux_list)
        elif len(l) == 2:
            sky = self.visit(l[1])
            if isinstance(sky, Skyline):
                sky.reverse_skyline()
                return sky
            elif isinstance(sky, str):
                if sky in self.table:
                    aux = self.table[sky]
                    return aux.reverse_skyline()
                return "EXPRESSIO INCORRECTA"
            return "EXPRESSIO INCORRECTA"

        else:
            if l[0].getText() == "(":
                return self.visit(l[1])
            op = l[1].getText()
            left = self.visit(l[0])
            right = self.visit(l[2])
            if left == "EXPRESSIO INCORRECTA" or right == "EXPRESSIO INCORRECTA":
                return "EXPRESSIO INCORRECTA"
            if op == ":=":
                if not isinstance(left, str):
                    return "EXPRESSIO INCORRECTA"
                if isinstance(right, Skyline):
                    self.table[left] = right
                    # right.print()
                    # self.table[left].print()
                    return right
                if isinstance(right, str):
                    if right in self.table:
                        self.table[left] = right
                        return self.table[right]
                    else:
                        return "EXPRESSIO INCORRECTA"
                return "EXPRESSIO INCORRECTA"

            if isinstance(left, str):
                if left in self.table:
                    left = self.table[left]
                else:
                    return "EXPRESSIO INCORRECTA"
            if op == "+":
                if isinstance(right, int) and right >= 0:
                    return left.move_positions(right)
                elif isinstance(right, Skyline):
                    l1 = [[i.get_xmin(), i.get_xmax(), i.get_height()]
                          for i in left.get_buildings()]
                    l2 = [[i.get_xmin(), i.get_xmax(), i.get_height()]
                          for i in right.get_buildings()]
                    l1[len(l1):] = l2
                    aux = left.union(l1)
                    return left.reconstruct(aux)

                elif isinstance(right, str):
                    if right in self.table:
                        l1 = [[i.get_xmin(), i.get_xmax(), i.get_height()]
                              for i in left.get_buildings()]
                        l2 = [[i.get_xmin(), i.get_xmax(), i.get_height()]
                              for i in self.table[right].get_buildings()]
                        l1[len(l1):] = l2
                        aux = left.union(l1)
                        return left.reconstruct(aux)
                    else:
                        return "EXPRESSIO INCORRECTA"
                return "EXPRESSIO INCORRECTA"

            if op == "*":
                if isinstance(right, int) and right >= 0:

                    return left.replicate_skyline(right)

                elif isinstance(right, Skyline):
                    return left.intersect_skylines(right)

                elif isinstance(right, str):
                    if right in self.table:
                        return left.intersect_skylines(self.table[right])
                    else:
                        return "EXPRESSIO INCORRECTA"
                return "EXPRESSIO INCORRECTA"

            if op == '-':
                if isinstance(right, int) and right >= 0:
                    return left.move_positions(right * -1)
                return "EXPRESSIO INCORRECTA"


del SkylineParser
