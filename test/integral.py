def f(x):
    return x * x

def integrate(a, b, dx):
    S = 0.0
    x = a
    x_dx = 0.0
    A = 0.0
    B = 0.0
    while x < b:
        x_dx = x + dx
        if x + dx > b:
            x_dx = b
        A = f(x)
        B = f(x_dx)
        S = S + 0.5 * (A + B) * dx
        x = x + dx
    return S

def main():
    i = 0
    while i < 10:
        print(integrate(0.0, 1.0, 0.1))
        print(integrate(0.0, 1.0, 0.01))
        print(integrate(0.0, 1.0, 0.001))
        print(integrate(0.0, 1.0, 0.0001))
        i = i + 1
    
if __name__ == "__main__":
    main()
