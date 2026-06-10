status = {
    "health": 100,
    "sanity": 100,
    "hungry": 100,
    "money": 1000,
    "clean": 5,
}

choy = ((1 ,"Você trabalhou! "), (2, "Você foi visitar sua namorada! "), (3, "Você estudou! "), (4, "Você ficou atoa! "))

hist = []

def history(choy):
    hist.append(choy)

def show_hist():
    for i in hist:
        print("\n",i)