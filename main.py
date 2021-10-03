from random import randint
from random import choice
import sys

def randomInt(from_,to_):
    return randint(from_,to_)

def throwError(message):
    print(message)
    exit(1)

def mitWiederholung(from_,to_,anzahl):
    randomList = []
    for x in range(anzahl):
        randomList.append(randomInt(from_,to_))
    return randomList

def ohneWiederholung(from_,to_,anzahl):
    if(from_-to_ > anzahl):
        throwError("Error: Anzahl ist kleiner als die Auswahl")
    selectList = range(from_,to_)
    randomList = []
    for x in range(anzahl):
        randomList.append(choice(selectList))
    return randomList



# Argumente: 
#   <from>
#   <to>
#   <anzahl der Wiederholung>
#   Arten von Zufallsexperimenten
#       (-m)        Mit Wiederholung: Beispiel Würfel
#       (standart)  Ohne  Wiederholung: Beispiel Lose in der Lotterie

# Parse Commandline Arguments
commandlineArguments = sys.argv[1:]

from_ = int(commandlineArguments[0])
to_   = int(commandlineArguments[1])
anz   = int(commandlineArguments[2])
wid   = False

if(len(commandlineArguments) > 3):
    wid   = True

# ----------------------

if(wid):
    print(str(mitWiederholung(from_,to_,anz)))
else:
    print(str(ohneWiederholung(from_,to_,anz)))