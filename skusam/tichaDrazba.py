import os
auction_logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
'''
print(auction_logo)
print("Vitaje v programe pre tichu dražbu ")
run= "ano"
zaujemci={}
while run != "nie":
    meno = input("Zadajte vase meno: ")
    price = input("Zadajte vase castku ")
    zaujemci[meno] = price
    run = input("Su dalsi zaujemci? ano alebo nie ").lower()
    if run == "nie":
        os.system("clear")

def highest_bid(bidders):
    max=0
    for x in zaujemci:
        cena = int(zaujemci[x])
        if max < cena:
            max = cena
            name = x
    print(f"Najvyssiu ponuku mal {name} s hodnotou {max}")
 
highest_bid(zaujemci)           