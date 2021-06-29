import string
import random
from tabulate import tabulate

N = 6   # dlugosc ciagu znaków w identyfikatorze
HOW_MANY_ROBOTS = 10
TYPE = ["AUV", "AFV", "AGV"]

class Robot:
    def build(self):
        self.identyfikator = ''.join(random.choice(string.ascii_letters) for x in range(N))
        self.typ = random.choice(TYPE)
        self.masa = random.randint(50, 2001)
        self.zasieg = random.randint(1, 1001)
        self.rozdzielczosc = random.randint(1, 31)

    def introduction(self, show):
        if show:
            try:
                print(f'self.identyfikator: {self.identyfikator}\n'
                      f'self.typ: {self.typ}\n'
                      f'self.masa: {self.masa}[dag]\n'
                      f'self.zasieg: {self.zasieg}[km]\n'
                      f'self.rozdzielczosc: {self.rozdzielczosc}[MP]\n')
            except AttributeError:
                print('Nie zbudowano robota')
            else:
                return {"id": self.identyfikator, "typ": self.typ, "masa": self.masa, "zasieg": self.zasieg, "rozdz": self.rozdzielczosc}
        else:
            try:
                return {"id": self.identyfikator, "typ": self.typ, "masa": self.masa, "zasieg": self.zasieg, "rozdz": self.rozdzielczosc}
            except AttributeError:
                print('Nie zbudowano robota')

    def raiseArmy(self, howManyRobots):
        army = []
        for i in range(howManyRobots):
            soldier = Robot()
            soldier.build()
            army.append(soldier.introduction(False))
        return army

    def showArmy(self, army, show):
        table = [['identyfikator', 'typ', 'masa', 'zasieg', 'rozdzielczosc']]
        for elem in army:
            table.append([elem["id"], elem["typ"], elem["masa"], elem["zasieg"], elem["rozdz"]])
        if show:
            print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        return(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

    def saveArmy(self, army):
        f = open("army.txt", "w")
        f.write(str(army))
        f.close()

    def openArmy(self):
        f = open("army.txt", "r")
        army = eval(f.read())
        f.close()
        return army


if __name__== "__main__":
    rob = Robot()
    rob.build()
    rob.introduction(False)
    robots = Robot()
    robotsArmy = robots.raiseArmy(HOW_MANY_ROBOTS)
    robotsArmyIntroduction = robots.showArmy(robotsArmy, True)
    robots.saveArmy(robotsArmy)
    print(robots.openArmy())
