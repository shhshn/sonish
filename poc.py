#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    top, bottom = ["""#include <iostream>
#include <vector>
#include <unordered_map>
    """], []
    for line in sys.stdin:
        line = line.split("#", 1)[0].strip()
        if line.startswith("def"):
            line = line.split("def", 1)[1].rsplit(":", 1)[0]
            top.append("int " + line + "{")
            bottom.append("return 0; }")
            continue
        if line.startswith("print"):
            line = line.split("print(", 1)[1].rsplit(")", 1)[0]
            top.append("std::cout << " + line + " << std::endl;")
            continue
        if line.startswith("for"):
            var, seq = line.split("for", 1)[1].rsplit(":", 1)[0].split(" in ", 1)
            top.append("for (auto " + var + " : " + seq + ")")
            continue
        if ".append(" in line:
            name, obj = line.split(".append(", 1)
            obj = obj.rsplit(")", 1)[0]
            top.append(name + ".push_back(" + obj + ");")
        if "=" in line:
            name, obj = map(str.strip, line.split("=", 1))
            if obj.startswith("["):
                values = obj.split("[", 1)[1].rsplit("]", 1)[0]
                value = values.split(",", 1)[0].strip()
                if value.startswith('"'):
                    placeholder = "const char *"
                elif "." in value:
                    placeholder = "float"
                else:
                    placeholder = "int"
                top.append("auto " + name + " = std::vector<"
                           + placeholder + ">{" + values + "};")
                continue
            if obj.startswith("{"):
                kvs = obj.split("{", 1)[1].rsplit("}", 1)[0]
                key, value = map(str.strip, kvs.split(",", 1)[0].split(":"))
                if key.startswith('"'):
                    k_placeholder = "const char *"
                elif "." in key:
                    k_placeholder = "float"
                else:
                    k_placeholder = "int"
                if value.startswith('"'):
                    v_placeholder = "const char *"
                elif "." in key:
                    v_placeholder = "float"
                else:
                    v_placeholder = "int"
                kvs = "{" + kvs.replace(",", "},{").replace(":", ",") + "}"
                top.append("auto " + name + " = std::unordered_map<"
                           + k_placeholder + "," + v_placeholder + ">{"
                           + kvs + "};")
                continue
            continue
    for line in top + bottom:
        print(line)

if __name__ == "__main__":
    main()
