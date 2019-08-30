#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, ast, astpretty

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-file", required=True)
    args = parser.parse_args()
    with open(args.file) as file:
        source = file.read()
    tree = ast.parse(source)
    #print(ast.dump(tree))
    #astpretty.pprint(tree)
    print("#include <iostream>\n#include <vector>\n#include <unordered_map>")
    print(parse(tree))
#    try:
#        print(parse(tree))
#    except Exception as e:
#        print("ParseError: ", e)

def parse(x):
    # TODO: make use of a pseudo switch made of {ast.foobar:foobar()}
    if isinstance(x, ast.Dict):
        return "std::unordered_map<int, const char *>{%s}" % \
            ", ".join("{%s, %s}" % (parse(k), parse(v)) for k, v in zip(x.keys, x.values))
    if isinstance(x, ast.Num):
        return str(x.n)
    if isinstance(x, ast.List):
        return "std::vector<int>{%s}" % ", ".join(parse(element) for element in x.elts)
    if isinstance(x, ast.Assign):
        # TODO support tuple targets
        return "auto %s = %s;" % (parse(x.targets[0]), parse(x.value))
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
    if isinstance(x, ast.Expr):
        if isinstance(x.value, ast.Call):
            if isinstance(x.value.func, ast.Attribute):
                if x.value.func.attr == "append":
                    return "%s.push_back(%s);" % (parse(x.value.func.value), parse(x.value.args[0]))
            if isinstance(x.value.func, ast.Name):
                if x.value.func.id == "print":
                    return "std::cout << " + \
                        " << ".join(parse(line) for line in x.value.args) + \
                        " << std::endl;"
    if isinstance(x, ast.FunctionDef):
        return "int %s() {\n" % x.name + \
            "\n".join(parse(line) for line in x.body) + \
            "return 0;\n" + "\n}"
    if isinstance(x, ast.Module):
        return "\n".join(parse(line) for line in x.body)
    return ""
    if False:
        pass
    #raise Exception(x)

if __name__ == "__main__":
    main()
