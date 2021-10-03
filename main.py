from random import randint
from random import choice
from functools import reduce
import sys

def printHelp():
    print("<repeat Experiment for x Times> ")
    print("<from>")
    print("<to>")
    print("<anzahl der Wiederholung>")
    print("Arten von Zufallsexperimenten")
    print("    (-m)        Mit Wiederholung: Beispiel Würfel")
    print("    (standart)  Ohne  Wiederholung: Beispiel Lose in der Lotterie")
    print("Verarbeitungsfunktion ")
    print("    (-f)        s  -> Summe (standart)")
    print("    (-f)        m  -> Minus")

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
#   <repeat Experiment for x Times>
#   <from>
#   <to>
#   <anzahl der Wiederholung>
#   Arten von Zufallsexperimenten
#       (-m)        Mit Wiederholung: Beispiel Würfel
#       (standart)  Ohne  Wiederholung: Beispiel Lose in der Lotterie
#   Verarbeitungsfunktion 
#       (-f)        s  -> Summe (standart)
#       (-f)        m  -> Minus with abs

# Parse Commandline Arguments
commandlineArguments = sys.argv[1:]
try:
    rep   = int(commandlineArguments[0])
    from_ = int(commandlineArguments[1])
    to_   = int(commandlineArguments[2])
    anz   = int(commandlineArguments[3])
    wid   = False
    func  = False
    funcT = "s"
except:
    printHelp()
    exit(1)

if(len(commandlineArguments) > 4):
    if(commandlineArguments[4] == "-m"):
        wid   = True
    if(commandlineArguments[4 + wid*1] == "-f"):
        func = True
        funcT = commandlineArguments[5 + wid*1]


# ----------------------

dic = {}
for x in range(rep):
    out = []

    if(wid):
        out = mitWiederholung(from_,to_,anz)
    else:
        out = ohneWiederholung(from_,to_,anz)

    if(func):
        if(funcT == "s"):
            if(sum(out) in dic):
                dic[sum(out)] += 1
            else:
                dic[sum(out)] = 1
        elif(funcT == "m"):
            if(abs(reduce(lambda a,b: a-b,out)) in dic):
                dic[abs(reduce(lambda a,b: a-b,out))] += 1
            else:
                dic[abs(reduce(lambda a,b: a-b,out))] = 1
    else:
        if(out in dic):
            dic[out]+=1
        else:
            dic[out]=1

print(dic)