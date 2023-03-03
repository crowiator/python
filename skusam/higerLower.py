import random
data = [
    {
        'name': 'Instagram',
        'follower_count': 501,
        'description': 'Sociální platforma',
        'country': 'USA'
    },
    {
        'name': 'Facebook',
        'follower_count': 4,
        'description': 'Sociální platforma',
        'country': 'USA'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 436,
        'description': 'Fotbalový hráč',
        'country': 'Portugal'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 161,
        'description': 'Herec a wrestler',
        'country': 'USA'
    },
    {
        'name': 'Harry Potter film',
        'follower_count': 8,
        'description': 'Film',
        'country': 'USA'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 307,
        'description': 'Podnikatelka',
        'country': 'USA'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 324,
        'description': 'Fotbalista',
        'country': 'Argentina'
    },
    {
        'name': 'Neymar',
        'follower_count': 158,
        'description': 'Fotbalista',
        'country': 'Brazilie'
    },
    {
        'name': 'Eminem',
        'follower_count': 40,
        'description': 'Hudebník',
        'country': 'USA'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 193,
        'description': 'Hudebník',
        'country': 'Canada'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 111,
        'description': 'Herečka',
        'country': 'Francie'
    }
]
#print(data[0]["name"])
# print(data[1]["follower_count"])
# #0-10
# print(len(data))
run=True
skore=0
while(run):
    # generator 
    position1 = random.randint(0,10)
    position2 = random.randint(0,10)

    #postava 1
    objekt1 = data[position1]
    name1 =objekt1["name"]
    profesion1 = objekt1["description"]
    country1= objekt1["country"]
    followers1= int(objekt1["follower_count"])

    #postava 2
    objekt2 = data[position2]
    name2 = objekt2["name"]
    profesion2 = objekt2["description"]
    country2= objekt2["country"]
    followers2= int(objekt2["follower_count"])
    #A -
    #name1
    #profesion1 
    #followers1

    #B -
    #name2
    #profesion2 
    #followers2

    def getChar(countA, countB):
        if countA > countB:
            return "A"
        elif countB > countA:
            return "B"   



    print(f"Porovnajte A: {name1}, {profesion1}, z {country1}")
    print(f"Porovnajte B: {name2}, {profesion2}, z {country2}")
    print(f"Testovaci vypis- A: {followers1}")
    print(f"Testovaci vypis- B: {followers2}")


    choice= input("Kto ma viac sledujucich na instagramu?")
    vacsie = getChar(followers1,followers2)
    if choice == vacsie:
        run = True
        skore +=1
        print(f"Uhadli ste, vase skore je {skore}")
        if vacsie == "A":
            objekt1=objekt1
        else:
            objekt1= objekt2    
    else:
        print(f"Je mi luto, prehrali ste so skore {skore}")
        run = False    
