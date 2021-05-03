def Multiply(x,y):
    pdt = x*y
    print(f"the product of {x} and {y} is {pdt}")

def Add(x,y):
    sum = x+y
    print(f"the sum of {x} and {y} is {sum}")

def Divide(x,y):
    qtnt = x/y

def Power(x,y):
    pow = x**y
    print(f"{x} raise to the power of {y} gives {pow}")

def countLetters(g):
    a = len(g)
    print(f"the number of letters in string is {a}")

d = "this is a string of characters which is to be counted"
Multiply(3,7); print("\n")
Add(3,7); print("\n")
Divide(3,7); print("\n")
Power(3,7); print("\n")
countLetters(d)