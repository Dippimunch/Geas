import time
import random
from entity import Entity
from location import Location

weather = ["fair"]
#pace = 3 # miles per hour
terrain = {"rough": .75, "normal": 1, "easy": 1.5}

def describeScene(clock):
    print("A %s %s." % (checkWeather(), checkTime(clock)))

def checkTime(clock):
    timeOfDay = ["small hours", "morning", "afternoon", "night"]
    #               12-6          6-12        12-6      6-12

    #TODO: iterate
    if clock < 6:
        return timeOfDay[0]
    
    elif clock < 12:
        return timeOfDay[1]

    elif clock < 18:
        return timeOfDay[2]
    elif clock < 24:
        return timeOfDay[3]
    else:
        print("WE ARE  N O W H E N")
    # elif: clock > 24; clock -= 24
    # need clock function to reset

def clockUpdate(clock):
    if clock > 24:
        clock -= 24


def checkWeather():
    check = random.randint(0, 143)
    if check < 72:
        return "rain"
    else:
        return "clear"

def march(entity, pace, duration, clock):
    entity.location += (pace * duration)
    clock += duration

def main():
    player = Entity("Anu", 0)
    location = Location("Nirn")
    clock = 0
    
    distance = 0
    
    speedBase = 1.5
    
    play = True
    
    while play == True:
        clockUpdate(clock)
        # TODO weatherUpdate()
        print("\n")
        print("Time: %i\nLocation: %i" % (clock, player.location))
        choice = input("\nchoices: \n%s\n%s\n%s\n" % ("1- scene", "2- march", "3- pace")) #list choices
        time.sleep(.1)

        if choice == "1":
            describeScene(clock)
            input()

        elif choice == "2":
            clock += 1
            march(player, int(input("How fast? ")), 1, clock)

        elif choice == "quit":
            quit()

        else:
            print("ivalid input")

main()


