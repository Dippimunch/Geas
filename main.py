import time
import random
from entity import Entity

weather = ["fair"]
timeOfDay = ["morning", "day", "night"]
pace = 3
terrain = {"rough": .75, "normal": 1, "easy": 1.5}
duration = 0

def describeScene():
    print("A %s %s." % (weather[0], timeOfDay[1]))

def checkWeather():
    check = random.randint(144)
    if check < 72:
        return "rain"
    else:
        return "clear"

def march(entity, pace, duration):
    entity.location += (pace * duration)

def main():
    player = Entity("Anu", 0)
    
    distance = 0
    distanceMax = 100
    
    speedBase = 1.5
    
    play = True
    
    while play == True:
        choice = input("\nchoices: \n%s\n%s\n" % ("1 - scene", "2 - march")) #list choices
        #distance += speedBase
        time.sleep(.1)
        #print(distance)

        if choice == "1":
            describeScene()

        elif choice == "2":
            march(player, terrain["normal"], 24, time)
            print(checkWeather())

        elif choice == "quit":
            quit()

        else:
            pass

        #if distance >= distanceMax:
            #play = not play

main()


