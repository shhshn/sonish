#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, ast, sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-file", required=True)
    args = parser.parse_args()
    with open(args.file) as file:
        source = file.read()
    tree = ast.parse(source)
#    import astpretty
#    astpretty.pprint(tree)
#    print(ast.dump(tree))
#    return
    print("#include <iostream>\n#include <vector>\n#include <unordered_map>\n#include <iomanip>")
    print()
    try:
        print(parse(tree))
    except Exception as e:
#        astpretty.pprint(tree)
        sys.exit("ParseError: %s" % e)
#    print(globals()["parse"](tree))
#    print("#", str(tree), "#")

def parse(x, declare = False):
    # TODO: make use of a pseudo switch using {ast.foobar:foobar()}
    if isinstance(x, ast.If):
        test = parse(x.test)
        if "__name__" in test and "==" in test and "__main__" in test: return ""
        return "if (" + test + ") {\n    " + \
            "\n    ".join(parse(line) for line in x.body) + \
            "\n} else {\n    " + \
            "\n    ".join(parse(line) for line in x.orelse) + \
            "\n}"
    if isinstance(x, ast.NotEq):
        return "!="
    if isinstance(x, ast.Eq):
        return "=="
    if isinstance(x, ast.LtE):
        return "<="
    if isinstance(x, ast.Lt):
        return "<"
    if isinstance(x, ast.GtE):
        return ">="
    if isinstance(x, ast.Gt):
        return ">"
    if isinstance(x, ast.Mod):
        return "%"
    if isinstance(x, ast.Mult):
        return "*"
    if isinstance(x, ast.Sub):
        return "-"
    if isinstance(x, ast.Add):
        return "+"
    if isinstance(x, ast.Return):
        return "return %s;" % parse(x.value)
    if isinstance(x, ast.BinOp):
        return "(%s %s %s)" % (parse(x.left), parse(x.op), parse(x.right))
    if isinstance(x, ast.Compare):
        return parse(x.left) +" "+ " ".join(parse(o) for o in x.ops) +" "+ " ".join(parse(c) for c in x.comparators)
    if isinstance(x, ast.While):
        return "while (" + parse(x.test) + ") {\n    " + \
            "\n    ".join(parse(line) for line in x.body) + \
            "\n}"
    if isinstance(x, ast.Dict):
        return "std::unordered_map<int, const char *>{%s}" % \
            ", ".join("{%s, %s}" % (parse(k), parse(v)) for k, v in zip(x.keys, x.values))
    if isinstance(x, ast.Num):
        return str(x.n)
    if isinstance(x, ast.List):
        return "std::vector<int>{%s}" % ", ".join(parse(element) for element in x.elts)
    if isinstance(x, ast.Assign):
        # TODO: support tuple targets
        if declare:
            return "auto %s = %s;" % (parse(x.targets[0]), parse(x.value))
        else:
            return "%s = %s;" % (parse(x.targets[0]), parse(x.value))
    if isinstance(x, ast.Name):
        return x.id
    if isinstance(x, ast.For):
        return "for (auto %s : %s) {\n" % (x.target.id, x.iter.id) + \
            "\n".join(parse(line) for line in x.body) + \
            "\n}"
    if isinstance(x, ast.Index):
        return "[%d]" % x.value.n
    if isinstance(x, ast.Subscript):
        return x.value.id + parse(x.slice)
    if isinstance(x, ast.Str):
        return '"%s"' % x.s
    if isinstance(x, ast.Call):
        if isinstance(x.func, ast.Attribute):
            if x.func.attr == "append":
                return "%s.push_back(%s);" % (parse(x.func.value), parse(x.args[0]))
        if isinstance(x.func, ast.Name):
            if x.func.id == "print":
                return "std::cout << std::fixed << std::setprecision(17) << " + \
                    " << ".join(parse(line) for line in x.args) + \
                    " << std::endl;"
        return "%s(%s)" % (parse(x.func), ", ".join(parse(a) for a in x.args))
    if isinstance(x, ast.Expr):
        return parse(x.value)
    if isinstance(x, ast.FunctionDef):
        typename = "int" if x.name == "main" else "auto"
        return "%s %s(%s) {\n" % (typename, x.name, ", ".join("auto " + a.arg for a in x.args.args)) + \
            "\n".join(parse(line, declare = True) for line in x.body) + \
            "%s}\n" % ("return 0;\n" if x.name == "main" else "")
    if isinstance(x, ast.Module):
        return "\n".join(parse(line) for line in x.body)
    raise Exception(x)
    return ""
    if False:
        pass

if __name__ == "__main__":
    main()
