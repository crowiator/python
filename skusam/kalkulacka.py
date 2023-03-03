import os
def scitanie(a,b):
    return a+b

def odcitanie(a,b):
    return a -b

def delenie(a,b):
    return a/b

def nasobenie(a,b):
    return a*b
 
operations = {
    "+": scitanie,
    "-": odcitanie,
    "/": delenie,
    "*": nasobenie
}
def getVysledok(cislo1, cislo2,choice):
    result = 0
    if choice == "+":
        result = scitanie(cislo1,cislo2)
    elif choice == "-":
        result = odcitanie(cislo1,cislo2)
    elif choice == "/":
        result = delenie(cislo1,cislo2)
    elif choice =="*":
        result = nasobenie(cislo1,cislo2)

    return result

# rekurzia
def calculator():
    run = "ano"
    cislo = float(input("Zadaj 1. cislo: "))
    while(run == "ano"):
        for symbol in operations:
            print(symbol)

        choice = input("Vyber si operaciu:")
        cislo2 = float(input("Zadaj 2. cislo: "))
        #vysledok =getVysledok(cislo,cislo2,choice)
        call_function = operations[choice]
        vysledok = call_function(cislo,cislo2)
        print(f"Vysledok operacie {choice} s cislami {cislo}, {cislo2} je {vysledok} ")
        run = input(f"Napiste ano, ak chcete pokracovat, inak nie, ak chcete ukoncit program: ")
        if run == "ano":
            cislo = float(vysledok)
        else:
            os.system("clear")
            calculator()    

calculator()
