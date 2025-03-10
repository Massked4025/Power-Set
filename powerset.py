def printPowerset(set, setsize):
    powersetsize = 2**setsize
    outer = 0
    inner = 0
    for outer in range(0, powersetsize):
        for inner in range(0, setsize):
            if (outer & (1 << inner)> 0):
                print(set[inner], end=" ")
        print("")

size = int(input("Enter the set size: "))
set = []
for i in range(0, size):
    a = int(input("Enter the element: "))
    set.append(a)
printPowerset(set, size)

#Flipbits

def flipbits(num1, num2):
    flip = 0
    while (num1>0 or num2>0):
        t1 = num1 & 1
        t2 = num2 & 1
        if t1 != t2:
            flip += 1
        num1 >>= 1
        num2 >>= 1
    return flip

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(flipbits(num1, num2))