# print("Ucim sa python")
# print("Funkcia print zacina s print")
# print('Funkciu print zavolame print("nejaky text")')

# #Odradkovanie
# print("Hello, my name is Sam \nI am 24 years old")
# #Spojenie
# print("Jablko" + "Hruska")
# #Odsadenie

# print("Naucili sme sa vela veci o stringu\n" + "Tiez sme pouzivali print('nejaky text')\n"
# + "Prvy riadok \n" + "Druhy riadok sa robi cez \n")


# city = input("What is your hometown? ")
# print("I live in " + city)

# name= input("What is your name ?\n")
# length= len(name)
# print(length)
# print(name)
# length = len(input("What is your name ?\n"))
# print(length)

#applikacia
# print("Vitajte v aplikacii na fanky mena")
# name = input("Napis svoje meno\n")
# description = input("Tvoja funky vlastnost:\n")
# print("Tvoje meno je " + name + " " + description)

# cislo = input("Napis dvojmiestne cislo:")
# cifra1 = int(cislo[0])
# cifra2 = int(cislo[1])
# print(cifra1 + cifra2)

#BMI

# height = float(input("Enter your height: "))
# weight = float(input("Enter your weight: "))
# BMI = weight / (height**2)
# BMI = round(BMI,2)

# if BMI <= 18.5:
#     print(f"Your BMI={BMI} is underweight")
# elif BMI >18.5 and BMI <= 24.9:    
#     print(f"Your BMI={BMI} is normal")
# elif BMI >25.0 and BMI <= 29.9:    
#     print(f"Your BMI={BMI} is overweight")
# elif BMI >30.0 and BMI <= 34.9:    
#     print(f"Your BMI={BMI} is obese")
# else:
#      print(f"Your BMI={BMI} is extremely obese")         
#F string
# x= 5
# print(f"Premnna x je: {x}")

#90 let
# age = int(input("Enter your age: "))
# limit_age = 90
# age_left = limit_age - age
# months = age_left * 12
# weeks = age_left * 52
# days = 365 * age_left

# print(f"Tvoj  vek je {age}, \n" + f"zostava ti {age_left} rokov\n" + f"zostava ti {months} mesiacov\n"
# + f"zostava ti {weeks} tyzdnov\n" + f"zostava ti {days} dni\n")

# price = int(input("Kolik mate celkem zaplatit"))
# tip = int(input("Kolik chcete dat propitne v %  "))
# people = int(input("Medzi kolko ludi chcete rozdelit castku "))
# sum_price = price + ((tip/100)*price)
# price_for_people= "{:.2f}".format(sum_price / people,2)
# print(f"Kazdy clovek by mal zaplatit: {price_for_people} ")

# podmienky
# print("Vitajte na horskej drahe")
# height = int(input("Zadajte svoju výšku: "))
# price=0
# if height >= 87 :
#     print("You can go")
#     age = int(input("How old are you ?"))
#     if age <= 12:
#         print("Cena listku je 80 KČ")
#         price=80
#     elif age > 12 and age <= 18:
#         print("Cena listku je 100 KČ")
#         price=100    
#     else:
#         print("Cena listku je 150 KČ")
#         price = 150

#     photo =input("Do you wanna photo ? Yes or No\n") 
#     if photo == "yes":
#         print("Price of photo is 50 KC")
#         price += 50
#     else:
#         print("No price for photo")

#     print(f"Celkova cena je {price}")
# else:
#     print("You cant go, sorry")   


# age = int(input("Enter your age: "))
# if age>= 18:
#     print(f"Your age is {age}, you are adult")
# else:
#     print(f"Your age is {age}, you are not adult")

# Cena lístku do kina je za normálních okolností 150 Kč. 
# Pokud jste student, tak máte nárok na studentskou slevu a lístek tak stojí 120 Kč. 
# Zeptejte se uživatele stránky, zda je student (odpoví ano nebo ne).
#  Pokud odpoví ano, tak vypište, že cena jeho lístku je 120 kč. 
# Pokud odpoví ne, tak vypište text, že jeho cena lístku je 150 Kč.    

# is_student = input("Are you student ? Yes or No ?")
# if is_student == "yes":
#     print("You are student, your price is 120 KČ")
# else: 
#     print("You are not  student, your price is 150 KČ")
# 
# type = input("Choose your type of mobile ? You can choose: \n1. normal \n2. smart\n3. extrasmart\n")
# if type == "smart":
#        print(f"Price of {type} is 15 000 kč ")
# elif type == "normal":
#        print(f"Price of {type} is 20 000 kč ")
# elif type == "extrasmart":
#        print(f"Price of {type} is 25 000 kč ")
# else:
#       print(f"You didnt choose anyone")     
# 

# cislo = int(input("Enter your number"))
# if cislo % 2 == 0: 
#     print(f"Cislo {cislo} je parne")
# else:
#     print(f"Cislo {cislo} je neparne")    


#Prestupny rok:
# year = int(input("Enter year:"))

# if (year % 4 == 0):
#     if (year % 100 != 0):
#         print("Priestupny rok")
#     elif(year % 100 == 0) and (year % 100 == 0):
#         print("Priestupny rok")
#     else: 
#         print("Nepriestupny rok")               
# else:
#     print("Nepriestupny rok")
# 
# Návštěvník si nejdříve zvolí velikost pizzy (S, M, L). Za velikost S se platí 100 Kč, za M 150 Kč a za L 200 Kč.
# Poté se zeptáte, zda chce feferonky. Pokud ano, tak u velikosti S se bude platit 20 Kč navíc a u velikostí M a L 30 Kč navíc.
# Poté se ještě zeptáte, zda chce návštěvník sýr navíc. Pokud ano, tak si připlatí dalších 15 Kč.

# size_of_pizza = input("Choose your size of pizza? S,M,L?") 
# price = 0
# if size_of_pizza == "S" or size_of_pizza == "M" or size_of_pizza == "L":
#     feferony = input("Do you wanna feferones ? yes or no ? ")

#     if size_of_pizza == "S":
#         price = 100
#         if(feferony == "yes"):
#             price+=20
#     elif size_of_pizza == "M":
#         price = 150
#         if(feferony == "yes"):
#             price+=30
#     elif size_of_pizza == "L":
#         price = 200
#         if(feferony == "yes"):
#             price+=30

#     cheese = input("Do you wanna cheese? yes or no")
#     if(cheese == "yes"):
#             price+=15
    
#     print(f"You choose {size_of_pizza}, price of pizza is {price} kČ")
# else:
#     print("Error input")                   
#



#Moduly
import random
# #Generovanie cisel z rozsahu
# print(random.randint(0,100))
# #generovanie medzi 0 az 1
# print(random.random())
# #generovaveni v rozsahu a s krokom
# print(random.randrange(0,100,5))

#hlava orel- minca
# for x in range(6):
#     coin = random.randint(0,1)
#     if coin == 1:
#         print("Hlava")
#     else:
#         print("Orel")    

# List
# employees = ["Ivan", "Harry", "Ron"]
# print(employees)
# # menime polozku
# employees[0] = "Severus"
# print(employees)
# #pridavanie
# employees.append("Hermiona")
# print(employees)
# #pridavenie viacerych poloziek
# employees.extend(["Mama", "Tara"])
# print(employees)

# import random
# names= input("Napis mena, vsetkych ucastnikov odelenych ciarkov ")
# list_people = names.split(", ")
# random_number=random.randint(0,len(list_people)-1)
# print(f"Pays: {list_people[random_number]}")

# # IndexError
# gryffindor = ["David", "Harry", "Ron", "Hermiona"]
# slytherin = ["Draco", "Crabbe", "Goyle"]

# number = len(gryffindor)
# # print(gryffindor[number])
# # Nested list
# students = [gryffindor, slytherin]
# print(students[1][2])

# set1 = ["⬜️", "⬜️", "⬜️"]
# set2= ["⬜️", "⬜️", "⬜️"]
# set3 = ["⬜️", "⬜️", "⬜️"]
# all_sets= [set1, set2, set3]
# print(f"{set1,}\n{set2,}\n{set3,}\n")
# black_choice =input("Choose position x, y: ")
# list_choice = black_choice.split(", ")
# position_x = int(list_choice[0])
# position_y = int(list_choice[1])
# all_sets[position_x][position_y] = "⬛️"
# print(f"{set1,}\n{set2,}\n{set3,}\n")

#Kamen, papier, noznice
# import random
 
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
 
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
 
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# all_list = [rock, paper, scissors]
# user_choice = int(input("Enter your choice\n0=rock\n1=paper\n2=scissors\n"))
# print(f"Your choice:\n {all_list[user_choice]}")

# computer_choice = random.randint(0,len(all_list)-1)
# print(f"Computer choice:\n {all_list[computer_choice]}")

# if user_choice == computer_choice:
#     print("It is draw")
# elif user_choice == 0 and computer_choice == 1:
#     print("You lost")
# elif user_choice == 0 and computer_choice == 2:
#     print("You won")
# elif user_choice == 1 and computer_choice == 0:
#     print("You won")
# elif user_choice == 1 and computer_choice == 2:
#     print("You lost")
# elif user_choice == 2 and computer_choice == 0:
#     print("You lost")
# elif user_choice == 2 and computer_choice == 1:
#     print("You won")                      

# heights=input("Enter height of people: ")
# list_people = heights.split(", ")
# sumHeight=0
# for x in list_people:
#     number = int(x)
#     sumHeight+=number

# number_of_people=float(len(list_people))
# average = sumHeight / number_of_people
# print(f"Average is {average}")    

# Nejvyšší skóre v testu
# score = [98, 50, 25, 78, 92]
# print(max(score))
# print(min(score))


# scores =input("Enter score of people: ")
# list_scores= scores.split(", ")
# print(list_scores)
# max=0
# min = 1000
# for x in list_scores:
#     number = int(x)
#     if max< number:
#         max=number

#     if min>number:
#         min=number

# print(f"Max is {max}")
# print(f"Min is {min}")

# range
# for one_number in range(1,10):
#     print(one_number)
# suma_cisel = 0
# for one_number in range(1,101):
#     suma_cisel += one_number
# print(suma_cisel)
#

# sum_par_cisel = 0
# for x in range(1,101):
#     if x % 2 == 0:
#         sum_par_cisel +=x    
# print(sum_par_cisel)
# 
# číslo dělitelné 3 = Fizz
# číslo dělitelné 5 = Buzz
# číslo dělitelné 3 a 5 = FizzBuzz
# jinak vypsat běžné číslo

# for x in range(1,101):
#     if x % 3 == 0 and x % 5 == 0:
#         print("FizzBuzz")
#     elif x % 3 == 0:
#         print("Fizz")
#     elif x % 5 == 0:
#         print("Buzz")
#     else:
#         print(x)  

#GENERATOR HESIEL
# import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']   

# print("Password generator")
# letters_count = int(input("How many letters do you want to have in password?\n"))
# numbers_count = int(input("How many numbers do you want to have in password?\n"))
# speacial_chars_count = int(input("How many special chars do you want to have in password?\n"))
# password=""
# result =[]
# for x in range(0,letters_count):
#     position = random.randint(0, (len(letters)-1))
#     result.append(letters[position])

# for x in range(0,numbers_count):
#     position = random.randint(0, (len(numbers)-1))
#     result.append(numbers[position])

# for x in range(0,speacial_chars_count):
#     position = random.randint(0, (len(special_char)-1))
#     result.append(special_char[position])

# random.shuffle(result)
# print(result)
# for x in result:
#     password += x
# print(password)    

# While
# import random
# characters = ["Harry", "Hermiona", "Ron","Draco","Crabbe","Goyle","Albus"]
# position= random.randint(0,(len(characters)-1))
# character =characters[position]
# guess= ""
# count =0
# while character !=guess:
#     guess=input("Choose your character from Harry Potter movies\n")
#     count += 1
# print(f"You done it the name was {character}, number of tries is {count}")

#HANGMAN
# Generovanie nahodneho slova
# import random
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# words = ["harry", "hermiona", "ron","draco","crabbe","goyle","albus"]
# word = words[random.randint(0,(len(words)-1))]
# print(word)



# #generovanie _
# hidden_word=[]
# for one_letter in word:
#     hidden_word.append("_")

# #zivoty
# lives=6
# #vypsani slova s podrzitky v normalni podobe
# printed_word=""
# for x in hidden_word:
#     printed_word+=x
# print(printed_word)


# #input od pouzivatela
# while "_" in hidden_word:
#     guess=input("Enter your letter\n ").lower()
#     for index in range(0,len(word)):
#         if guess == word[index]:
#             hidden_word[index] = guess

#     if guess not in word:
#         lives-=1
#         print(f"Pocet zivot je {lives}")
#         print(stages[lives])     
       
#     if lives == 0:
#         print(f"Pocet zivot je {lives}")
#         print("You are dead")
#         break

#     printed_word=""
#     for x in hidden_word:
#         printed_word+=x
#     print(printed_word)         


# #vypsani slova s podrzitky v normalni podobe


# #kontrola vitezstvi
# if "_" not in hidden_word:
#     print("You won")

#vlastne funkcie
# def my_function():
#     print("Hello girls")
# my_function()

# def greet(name):
#     print(f"Hello {name}")
# greet("Samuel")

# def greet(name,location):
#     print(f"Hi, my name is {name} and I live in {location}")

# greet("Samuel", "Slovakia")
# import math
# height_wall = int(input("Enter height of wall: "))
# wide_wall = int(input("Enter wide of wall: "))
# coverage = 5
# def calculator(height,wide):
#     area= height * wide
#     cans = math.ceil(area / coverage)
#     print(f"For are {area}, you need {cans} cans ")

# calculator(height_wall, wide_wall)

#Prvocislo
# number = int(input("Enter your number: "))
# def prvocislo(number):
#     counter=0
#     for x in range(1,(number+1)):
#         if number % x == 0:
#             counter+=1

#     if counter > 2:
#         print("Nie je prvocislo")
#     else:
#         print("Je prvocislo")

# prvocislo(number=number)

#Dictionary
#key - value
# it_dictionary = {
#     "String":"Text",
#     "Integer":"Cele cislo",
#     "Float": "Desatine cislo",
#     "Boolean": "True or False"
# }
# print(it_dictionary["Float"])
# it_dictionary_2 = {
#     1:"Text",
#     2:"Cele cislo",
#     3: "Desatine cislo",
#     4: "True or False"
# }
# print(it_dictionary_2[3])
#  #pridanie
# it_dictionary_2[5] = "Ja neviem uz"
#  #prazdny dictionary
# empty_dictionary = {}
# #vyprazdenie
# it_dictionary = {}
# #cyklus
# for key in it_dictionary_2:
#     print (it_dictionary_2[key])

# students_results = {
#   "Harry": 85,
#   "Ron": 71,
#   "Hermione": 98,
#   "Draco": 69
# }

# # Stupnice
# # 91 až 100 = "Excelentní"
# # 81 až 90 = "Vynikající"
# # 71 až 80 = "Splněno"
# # méně jak 71 = "Nesplněno"
# students_marks = {}

# for key in students_results:
#     hodnotenie=int(students_results[key])
#     word=""
#     if hodnotenie>=91 and hodnotenie<=100:
#         word= "Excelentní"
#     elif hodnotenie>=81 and hodnotenie<=90:
#         word= "Vynikající"
#     elif hodnotenie>=71 and hodnotenie<=80:
#         word= "Splněno"
#     else:
#         word= "Nesplněno"
#     students_marks[key] = word

# for x in students_marks:
#     print(f"{x}: {students_marks[x]}")

#NEsting
cities = {
    "Spain": "Madrid",
    "France": "Paris"
}
#dictionary a list
# travel_diary = {
#     "Spain":["Madrid","Leon","Valencia"],
#     "France": ["Paris", "Nice", "Lyon" ]
# }
# print(travel_diary["France"][1])

#dictionary in dictionary
# travel_diary = {
#     "Spain":{"visited_cities": ["Madrid","Leon","Valencia"]},
#     "France": {"visited_cities":["Paris", "Nice", "Lyon" ]}
# }
# print(travel_diary["Spain"]["visited_cities"][0])

# travel_diary = [
#     {
#         "country": "Spain",
#         "visited_cities": ["Madrid", "Leon", "Valencia"],
#         "visits": 5
#     },
#     {
#         "country": "France",
#         "visited_cities": ["Paris", "Nice", "Rennes"],
#         "visits": 2
#     }
# ]
# print(len(travel_diary))
# print(travel_diary[0])
# def add(country,cities,visits):
#     position = len(travel_diary)
#     new_directory={}
#     new_directory["country"]= country
#     new_directory["visited_cities"]=cities
#     new_directory["visits"]=visits
#     travel_diary.insert(position,new_directory)
    
# add("Slovakia",["Bratislava","Nitra", "Trnava"], 5)
# print(travel_diary)
# 
# Funkce a return
# def sum(a,b):
#     sum = a + b
#     return sum 

# def better_name(first_name, second_name):
#     full_name = first_name + " " + second_name
#     return full_name.title()

# print(better_name("samuel","vrana"))
# 
# days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# def is_gap_year(year):
#     value="True"
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                  value="True"
#             else:
#                 value= "False"
#         else:
#              value="True"
#     else:
#         value= "False"
#     return value

# def get_days(month):
#     days = days_in_month[month-1]
#     return days

# year = int(input("Jaký rok chcete zkontrolovat? "))
# month = int(input("Zadajte mesiac "))
# hodnota = is_gap_year(year)
# days = get_days(month)
# if hodnota== "True":
#     if month == 2:
#         days = 29
#     print(f"Rok {year} je priestupny a pocet dni v mesiaci {month} je {days}")
# else:
#      print(f"Rok {year} je nepriestupny a pocet dni v mesiaci {month} je {days}")


#Globalne
# def getGlobal():
#     global my_name
#     my_name = "Sam"
#     print(my_name)
# getGlobal()
# print(my_name)

# #Konstanty
# PI = 3.14159

# Debugging (ladění, hladní chyb)


# Popiš problém
# def test_function():
#   for number in range(1, 11):
#     if number == 10:
#       print("Vše je správně")
# test_function()


# Občas funguje a občas ne
# import random
# all_dice_numbers = ["1", "2", "3", "4", "5", "6"]
# dice_number = random.randint(0, 5)
# print(all_dice_numbers[dice_number])


# Mysli jako počítač
# year = int(input("Jaký je váš rok narození?"))
# if year > 1980 and year < 1994:
#   print("Jste millenial.")
# elif year >= 1994:
#   print("Jste generace Z.")


# Oprav hned chyby
# age = input("Kolik je vám let?")
# if age > 18:
#     print(f"Ve věku {age} můžete kupovat alkohol.")
