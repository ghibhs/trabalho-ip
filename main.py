import show as sw, choice as chc, data as dt, state as stt
n = 1
while n != -1:
    sw.show_status(dt.status)
    dec = sw.menu_decisions()
    if dec == "1":
        dt.history(chc.choy1())
    elif dec == "2":
        dt.history(chc.choy2())
    elif dec == "3":
        dt.history(chc.choy3())
    else:
        print("Invalid answerm")
    n = stt.check_status()
    sw.show_status(dt.status)
    stt.recovery()

for i in range(len(dt.hist)):
    print(dt.hist[i])