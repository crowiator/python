import random
import os

logo = """
 _____                     _                                          
|  __ \                   (_)                                        
| |  \/_   _  ___  ___ ___ _ _ __   __ _    __ _  __ _ _ __ ___   ___
| | __| | | |/ _ \/ __/ __| | '_ \ / _` |  / _` |/ _` | '_ ` _ \ / _ \\
| |_\ \ |_| |  __/\__ \__ \ | | | | (_| | | (_| | (_| | | | | | |  __/
 \____/\__,_|\___||___/___/_|_| |_|\__, |  \__, |\__,_|_| |_| |_|\___|
                                    __/ |   __/ |                    
                                   |___/   |___/                      
"""

def uvod():
    print(logo)
    print("Vitajte v hre Guess secret number. Porazte počitač")
    print("Myslim si cislo od 1 do 100")


def get_pocet_pokusov():
    obtiaznost = input("Vyberte obtiažnost 'easy' alebo 'hard': ")
    pocet_pokusov=0
    if obtiaznost == "easy":
        pocet_pokusov=10
    elif obtiaznost == "hard":
        pocet_pokusov =5
    return pocet_pokusov 

def getNumber():
    return int(input("Tipnite si cislo: "))


#MAIN
uvod()
random_number=random.randint(1,100)
print(f"Random number: {random_number}")
pocet_pokusov = int(get_pocet_pokusov())
print(f"Pocet pokusov: {pocet_pokusov}")

your_number = getNumber()
print(your_number)
run = "yes"
while run == "yes":
    while pocet_pokusov > 0:
        if your_number == random_number:
            print(f"Trafil si, cislo bolo: {random_number}")
            break
        elif your_number < random_number:
            print("Priliz nizke")
            pocet_pokusov-=1
        elif your_number > random_number:
            print("Priliz vysoke")
            pocet_pokusov-=1
        your_number = getNumber()    
    run = input("Napiste 'yes', pokud chcete pokracovat. Napiste 'no', pokud chcete skoncit hru:")
    if run=="no":
        os.system("clear")
