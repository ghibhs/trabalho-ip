import show as sw, choice as chc, data as dt, state as stt
n = 1
while n != -1:
    dec = ""
    sw.show_status(dt.status)
    dec = sw.menu_decisions()
    print(dec)
    if dec == "1":
        dt.history(chc.choy1())
        print("do1")
    elif dec == "2":
        dt.history(chc.choy2())
        print("do2")
    elif dec == "3":
        dt.history(chc.choy3())
        print("do3")
    else:
        print("Invalid answerm")
    n = stt.check_status()
    sw.show_status(dt.status)