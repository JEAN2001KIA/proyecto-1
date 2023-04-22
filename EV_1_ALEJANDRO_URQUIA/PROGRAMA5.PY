# escriba un progama que pida al usuario dos nuemeros enteros y muentre en la patalla #
a = int(input("ingresa un numero: "))
b = int(input("ingresa otro numero: "))
if a == b:
    print("inresa 2 numeros diferentes: ")
else:
    if a > b:
        c = a
        a = b
        b = c
    while a <= b:
        if a % 2 == 0:
            print("el numero ",a, "es par")
        else:
            print("el numero ",a, "es impar")
        a = a + 1