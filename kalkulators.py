

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def div(a, b):
    return a / b


def substract(a, b):
    return a - b


def modulus(a, b):
    return a % b


a = float(input("Ievadi skaitli a: "))
b = float(input("Ievadi skaitli b: "))


operation = input(
    "Izvēlies vienu no darbībām (1.=add/2.= multiply/3.= div/ 4.= substract/):   ")

if operation == '1':
    print(a, "+", b, "=", add(a, b))

elif operation == '4':
    print(a, "-", b, "=", substract(a, b))

elif operation == '2':
    print(a, "*", b, "=", multiply(a, b))

elif operation == '3':
    print(a, "/", b, "=", div(a, b))

else:
    print("False")


print("Vai vēlis zināt modulo atlikumu?")

a = float(input("Ievadi skaitli a: "))
b = float(input("Ievadi skaitli b: "))

saldo = input("Ievadi burtu (c)    ")

if saldo == "c":
    print(a, "%", b, "=", modulus(a, b))
