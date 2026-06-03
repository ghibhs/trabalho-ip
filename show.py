import data as dt, state as stt

def show_status(view):
    print("#")
    print("||",view,"||")
    print("#")

def menu_decisions():
    print(dt.choy[0])
    print(dt.choy[1])
    print(dt.choy[2])
    inp = input("Type the number of the choice: ")
    print("#")
    if inp == "1":
        if stt.limit(1) == True:
            print("yes", inp)
            return inp
        else:
            return "this action cant be do"
    elif inp == "2":
        if stt.limit(2) == True:
            print("yes", inp)
            return inp
        else:
            return "this action cant be do"
    elif inp == "3":
        if stt.limit(3) == True:
            print("yes", inp)
            return inp
        else:
            return "this action cant be do"
    else:
        return "Invalid answer"