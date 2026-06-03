import show as sw, data as dt

def check_status():
    if dt.status["health"] <= 0:
        print("You are dead")
        return -1
    if dt.status["money"] >= 5000:
        print("You won")
        return -1
    if dt.status["money"] <= 0:
        print("you are failed, here's your debit: ", dt.status["money"])
    else:
        print("Continue, he are always wachting")

def limit(opt):
    if opt == 1 and dt.status["health"] >= 40 and dt.status["hungry"] >= 20:
        return True

    elif opt == 2 and dt.status["health"] >= 30 and dt.status["hungry"] >= 20 and dt.status["sanity"] >= 15:
        return True

    elif opt == 3 and dt.status["health"] >= 40 and dt.status["hungry"] >= 35 and dt.status["sanity"] >= 30:
        return True
    
    else:
        return False
