
# Sonish: Python-ish syntax sugar added to C++

Sonish is yet another Python to C++ compiler that generates C++ snippet from restricted Python code.

## Getting Started

Just write down a Python snippet like the following.

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

After that, specify the file path to `make`, by replacing the `.py` extension with `.compile`.

```console
$ make test/demo.compile
$ test/demo
Hello and, again!
3
2
1
SUCCESS
```

As you can see, the Python snippet runs as C++!

## How It Works

Technically speaking, there is nothing but a Python to C++ compiler (*transcompiler*),
which works like a Python-ish frontend added to C++.

The project goal, and a major difference from others, is to support only a small but modern subset of Python and C++.
In that way, we benefit from several techniques incompatible with a full Python to C++ compiler.

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

and
- https://github.com/hayamiz/minipy (we use test data obtained from this repo)
