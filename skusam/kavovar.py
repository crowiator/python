MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 40,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 60,
    }
}
 
resources = {
    "water": 400,
    "milk": 300,
    "coffee": 150,
}
#print(MENU["espresso"]["ingredients"]["water"])
def report():
    print(f"Voda: {resources['water']}")
    print(f"Mliko: {resources['milk']}")
    print(f"Káva: {resources['coffee']}")

def mince():
    sum=0
    print("Prosim vlozete mince 1,2,5,10,20,50")
    jedna_koruna = int(input("Kolik 1 KČ chcete vložiť?: "))
    sum+=jedna_koruna
    dva_koruna = int(input("Kolik 2 KČ chcete vložiť?: "))
    sum+=( dva_koruna*2)
    pat_koruna = int(input("Kolik 5 KČ chcete vložiť?: "))
    sum+=( pat_koruna*5)
    desat_koruna = int(input("Kolik 10 KČ chcete vložiť?: "))
    sum+=( desat_koruna*10)
    dvadsat_koruna = int(input("Kolik 20 KČ chcete vložiť?: "))
    sum+=( dvadsat_koruna*20)
    patdesiat_koruna = int(input("Kolik 50 KČ chcete vložiť?: "))
    sum+=( patdesiat_koruna*50)
    return sum

#  "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 60,
#     }
def druh(vyber):
    if vyber=="report":
        report()
    else:
        water = int(MENU[vyber]["ingredients"]["water"])
        print(water)
        r_water-=water
        milk= int(MENU[vyber]["ingredients"]["milk"])
        print(milk)
        r_milk-=milk
        coffee=int(MENU[vyber]["ingredients"]["coffee"])
        print(coffee)
        r_cofee-=coffee
        cost =int(MENU[vyber]["cost"])
        print(cost)
       

vyber = input("Co byste si dal? (espresso/latte/cappucino): ")
r_water = int(resources["water"])
r_milk = int(resources["milk"])
r_cofee= int(resources["coffee"])
price =druh(vyber)
