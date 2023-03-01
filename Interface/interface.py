def display(h):
    for i in range(1, 41):
        i = str(i)
        hours = int(h.get(i).delivered / 100)
        minutes = int(h.get(i).delivered % 100)
        print(h.get(i).pack + " delivered: " + str(hours) + ":" + str(minutes).zfill(2) + " enroute: " + str(h.get(i).enroute))
