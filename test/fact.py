def fact(n):
    p = 1
    i = 1
    while i <= n:
        p = p * i
        i = i + 1
    return p


def ffact(n):
    p = 1.0
    i = 1
    while i <= n:
        p = p * i
        i = i + 1
    return p

def main():
    i = 0
    while i < 1000:
        print(int(ffact(11)))
        print(fact(11))
        print(int(ffact(12)))
        print(fact(12))
        #print(int(ffact(13)))
        #print(fact(13))
        i = i + 1

if __name__ == "__main__":
    main()
