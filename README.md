
# Sonish: Python-ish syntax sugar added to C++

## Getting Started

Just write a Python snippet like this:

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
$ cat demo.py | make run
$ ./a.out
Hello and, again!
3
2
1
SUCCESS
```

## How It Works

Technically speaking, there is nothing but a Python to C++ compiler (*transcompiler*), which works like a Python-ish frontend connected to a C++ backend.

The goal of the project, and a major difference from others, is to support a small subset of Python and C++ (*intersection*), which will benefit from several techniques incompatible with a full Python to C++ compiler.

## Supported Python Features

- Integers
- Lists
- Dicts
- Tuples
- Functions

### Unsupported Features

- `compile` and `eval`
- Comprehensions
- Closures
- Generators
- Exceptions
- Big numbers

## Related Work

- https://github.com/google/tmppy
- https://github.com/google/grumpy
- https://github.com/wmww/Python-plus-plus
- https://preshing.com/20141202/cpp-has-become-more-pythonic/
