class Robot:
    
    #constructor
    def __init__(self, baterie,delka_rukou) -> None:
        self.baterie = baterie
        self.delka_rukou= delka_rukou
        self.dny_do_opravy= 365
        self.ukony_do_kontroly=1000

    def krok_vpred(self):
        print("Robot udelal krok vpred")
        self.ukony_do_kontroly-=1
        print(f"Ukonu do kontroly je {self.ukony_do_kontroly}")

    def krok_vzad(self):
        print("Robot udelal krok vzad")
        self.ukony_do_kontroly-=1    
        print(f"Ukonu do kontroly je {self.ukony_do_kontroly}")   

#Tvorime  objekty cez classy
robot_1 = Robot(24,0.6)
robot_2 = Robot(22,0.7)
robot_3 = Robot(50,1.8)
robot_4 = Robot(100,10)

robot_1.krok_vpred()
robot_1.krok_vpred()
robot_1.krok_vpred()
robot_1.krok_vpred()
robot_1.krok_vzad()
robot_1.krok_vzad()
robot_1.krok_vzad()
# print(f"Vydrz baterie robota1: {robot_1.baterie}")
# print(f"Dlzka rukou robota1: {robot_1.delka_rukou}")
# print(robot_1.dny_do_opravy)
# robot_1.krok_vpred()
# robot_1.krok_vpred()
# robot_1.krok_vpred()
# robot_1.krok_vpred()
# robot_1.krok_vzad()
# robot_1.krok_vzad()
# robot_1.krok_vzad()
# robot_1.krok_vzad()
# robot_1.krok_vzad()
# print(robot_1.ukony_do_kontroly)
# print(f"Vydrz baterie robota2: {robot_2.baterie}")
# print(f"Dlzka rukou robota2: {robot_2.delka_rukou}")
# print(robot_2.dny_do_opravy)
# print(f"Vydrz baterie robota3: {robot_3.baterie}")
# print(f"Dlzka rukou robota3: {robot_3.delka_rukou}")
# print(robot_3.dny_do_opravy)
# print(f"Vydrz baterie robota4: {robot_4.baterie}")
# print(f"Dlzka rukou robota4: {robot_4.delka_rukou}")
# print(robot_4.dny_do_opravy)