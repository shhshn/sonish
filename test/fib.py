def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    print(fib(18))
    print(fib(20))
    print(fib(22))
    print(fib(24))
    print(fib(26))

if __name__ == "__main__":
    main()
