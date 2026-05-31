import show as sw, choice as chc, data as dt, state as stt

while True:
    sw.show_status(dt.status)
    dt.history(chc.choy1(sw.show_choice(dt.choy1)))
    sw.show_status(dt.status)
    break