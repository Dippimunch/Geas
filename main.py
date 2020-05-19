import time
import random
from entity import Entity
from location import Location

#pace = 3 # miles per hour
terrain = {"rough": .75, "normal": 1, "easy": 1.5}

def describeScene(clock, location):
    print("A %s %s." % (checkWeather(location), checkTime(clock, location)))

def checkTime(clock, location):
    timeOfDay = ["small hours", "morning", "afternoon", "night"]
    #               12-6          6-12        12-6      6-12

    #TODO: iterate
    if clock < 6:
        weatherUpdate(location)
        return timeOfDay[0]
    elif clock < 12:
        weatherUpdate(location)
        return timeOfDay[1]
    elif clock < 18:
        weatherUpdate(location)
        return timeOfDay[2]
    elif clock < 24:
        weatherUpdate(location)
        return timeOfDay[3]
    else:
        print("WE ARE  N O W H E N")
    # elif: clock > 24; clock -= 24
    # need clock function to reset

def clockUpdate(clock):
    # % it up
    if clock > 24:
        clock -= 24


def checkWeather(location):
    #check = random.randint(0, 143)
    if location.weather < 72:
        return "precipitation"
    else:
        return "clear"
    
def weatherUpdate(location):
    location.weather = random.randint(0, 143)

def march(entity, pace, duration, clock):
    distance_travelled = (pace * duration)
    entity.location += distance_travelled
    entity.resource_a -= distance_travelled
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
        print("\n")
        print("Time: %i\nLocation: %i\nresource_a: %i" % (clock, player.location, player.resource_a))
        choice = input("\nchoices: \n%s\n%s\n%s\n" % ("1- scene", "2- march", "3- pace")) #list choices
        time.sleep(.1)

        if choice == "1":
            describeScene(clock, location)
            #input()

        elif choice == "2":
            # Change to Action menu?
            clock += 1
            march(player, int(input("How fast? ")), 1, clock)

        elif choice == "quit":
            quit()

        else:
            print("ivalid input")

main()


