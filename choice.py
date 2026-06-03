import data as dt

def choy1():
    answer = input(dt.choy[0][1])
    alter = []
    if answer == "true":
        print("cool job")
        alter.append(dt.choy[0])
        alter.append(["health", "-50"])
        dt.status["sanity"] -= 35
        alter.append(["sanity", "-15"])
        dt.status["clean"] -= 2
        alter.append(["clean", "-2"])
        dt.status["money"] += 56
        alter.append(["money", "+56"])
        return alter
    elif answer == "false":
        print("how brave")
        alter.append(dt.choy[3])
        dt.status["sanity"] -= 5
        alter.append(["sanity", "-5"])
        dt.status["clean"] -= 1
        alter.append(["clean", "-1"])
        dt.status["money"] -= 115
        alter.append(["money", "-115"])
        return alter
    else:
        return "Invalid answer"
    

def choy2():
    answer = input(dt.choy[1][1])
    alter = []
    if answer == "true":
        print("she is very happy")
        alter.append(dt.choy[1])
        dt.status["sanity"] += 15
        alter.append(["sanity", "+15"])
        dt.status["clean"] -= 1
        alter.append(["clean", "-1"])
        dt.status["money"] -= 210
        alter.append(["money", "-90"])
        return alter
    elif answer == "false":
        print("she got angry")
        alter.append(dt.choy[3])
        dt.status["sanity"] -= 5
        alter.append(["sanity", "-5"])
        dt.status["clean"] -= 1
        alter.append(["clean", "-1"])
        dt.status["money"] -= 115
        alter.append(["money", "-115"])
        return alter
    else:
        return "Invalid answer"

def choy3():
    answer = input(dt.choy[2][1])
    alter = []
    if answer == "true":
        print("you study")
        alter.append(dt.choy[2])
        dt.status["sanity"] -= 25
        alter.append(["sanity", "-15"])
        dt.status["clean"] -= 1
        alter.append(["clean", "-1"])
        dt.status["money"] -= 115
        alter.append(["money", "-115"])
        return alter
    elif answer == "false":
        print("you dumbass")
        alter.append(dt.choy[3])
        dt.status["sanity"] -= 5
        alter.append(["sanity", "-5"])
        dt.status["clean"] -= 1
        alter.append(["clean", "-1"])
        dt.status["money"] -= 115
        alter.append(["money", "-115"])
        return alter
    else:
        return "Invalid answer"