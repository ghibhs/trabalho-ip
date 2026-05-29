import show as sw, data as dt

def choy1(answer):
    if answer == "true":
        sw.show_status("you won")
        dt.status["sanity"] -= 15
        dt.status["clean"] -= 1
        dt.status["money"] += 56
    else:
        pass

def choy2():
    if True:
        pass
    else:
        pass

def choy3():
    if True:
        pass
    else:
        pass