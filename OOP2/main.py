
# class WizzarPlayer:
#     def __init__(self,age,name="anonym"):
        
#         self.name = name
#         self.age = age

#     def attack(self):
#         print("Utok")

#     def age_checker(self):
#         if self.age >=18:
#             print("Muzete hra")
#         else:
#             print("Nemuzete hrat, vas vek je prilis nizky")        
#     @staticmethod
#     def test_function(a,b):
#         return a+b

#     @classmethod
#     def test_    
# #name = input("Zadajte sve jmeno: ")
# age = int(input("Zadajte svoj vek: "))       
# player1 = WizzarPlayer(age)
# print(player1.name)
# print(player1.age)
# player1.attack()
# player1.age_checker()
# print(WizzarPlayer.test_function(10,20))

# # Máte zadanou tuto classu
# class Dog:


#     def __init__(self, name, age):
#         self.name = name
#         self.age = age




# # Vytvořte 3 objekty (instance) podle classy
# # dokážete vysvětlit, jaký je vztah mezi classou a objektem?
# dog1 = Dog("Ron",10)
# dog2 = Dog("Harry", 13)
# dog3= Dog("Ivo", 10)
# dogs = [dog1,dog2,dog3]


# # Vytvořte funkci, která určí nejstaršího psa z vámi zadaných
# def the_oldest_one():
#     max_age = 0
#     the_oldest_dog = dogs[0]
#     for i in dogs:
#         actual_age = int(i.age)
#         if max_age < actual_age:
#             max_age =actual_age
#             the_oldest_dog = i
#     print(f"Pes s menom: {the_oldest_dog.name} a vekom {max_age} je najstarsi")

# the_oldest_one()
# # Vypište výslednou větu "Věk nejstaršího psa: X"

# 4 pilíře OOP
# Encapsulation = zapouzdření
# Abstraction = abstrakce = dáváme přístup pouze k tomu, co je zapotřebí
# Inheritance = dědění
# Polymorphism = mnoho forem


class WizardPlayer:


    def __init__(self, name="anonym", age=0):
            self.name = name
            self.age = age
   
    def attack(self):
        return "Útok 1. stupně!"




class HeadWizard(WizardPlayer):


    def attack(self):
        return "Útok 2. stupně!"


    def avada_kedavra(self):
        return "Avada Kedavra"


player1 = WizardPlayer("david", 25)
print(player1.attack())


print("--------------------")


player2 = HeadWizard("jana", 18)
print(player2.attack())


# print("--------------------")


# print(isinstance(player1, WizardPlayer)) # true
# print(isinstance(player1, HeadWizard))  # false
# print(isinstance(player2, WizardPlayer)) # true
# print(isinstance(player2, HeadWizard)) # true

