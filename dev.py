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
    astpretty.pprint(tree)

if __name__ == "__main__":
    main()
