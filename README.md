
# Sonish: Python-ish syntax sugar added to C++

Sonish is yet another restricted Python to C++ compiler, which takes static Python code (without `eval`) as input and then generates C++ code as output.

## Getting Started

Just write down a Python snippet like this:

```python
def main():
    print("Hello and, again!")
    l = [3, 2]
    l.append(1)
    for x in l:
        print(x)
    d = {4: "HUGE", 5: "SUCCESS"}
    print(d[5])
```

Then it runs as C++:

```console
$ make test/demo
$ test/demo
Hello and, again!
3
2
1
SUCCESS
```

## How It Works

Technically speaking, there is nothing but a Python to C++ compiler (*transcompiler*), which works like a Python-ish frontend added to C++ backend.

The goal of the project, and a major difference from others, is to support only a small but modern subset of Python and C++, which will benefit from several techniques incompatible with a full Python to C++ compiler.

## Supported Features

- Integers
- Lists
- Dicts
- Tuples
- Functions

### Unsupported Features

- `compile`, `eval`, `type`, and `isinstance`
- Nested Functions
- Comprehensions
- Closures
- Generators
- Exceptions
- Big numbers

## Related Work

- https://github.com/google/tmppy
- https://github.com/google/grumpy
- https://github.com/shedskin/shedskin
- https://github.com/lukasmartinelli/py14
- https://github.com/wmww/Python-plus-plus
- https://preshing.com/20141202/cpp-has-become-more-pythonic/
