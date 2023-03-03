import CSVRead.hubDistance


def closestNeighbor(truck, address, h):
    i = 0
    j = 0
    total_distance = 0
    while len(truck.packages) > 0:
        for address_index, name in enumerate(CSVRead.hubDistance.disList):
            if name.address == address:
                j = address_index

        distance = 100
        next_pack = 0
        if i == 16:
            break
        for pack, item in enumerate(truck.packages):

            for index, add in enumerate(CSVRead.hubDistance.disList):
                if item.address == add.address:
                    try:
                        if float(CSVRead.hubDistance.disList[index].miles[j]) < distance:
                            distance = float(CSVRead.hubDistance.disList[index].miles[j])
                            next_pack = pack
                    except:
                        if float(CSVRead.hubDistance.disList[j].miles[index]) < distance:
                            distance = float(CSVRead.hubDistance.disList[j].miles[index])
                            next_pack = pack

        total_distance = total_distance + distance
        hour = (distance / 18)
        minute = (hour % 1) * 60
        hour = int(hour) * 100
        time = int(hour + minute)
        ha = str(truck.packages[next_pack].pack)
        h.get(ha).delivered = time + truck.time
        if h.get(ha).delivered%100 > 60:
            h.get(ha).delivered = (h.get(ha).delivered + 100) - 60
        truck.time = truck.time + time
        if truck.time %100 > 60:
            truck.time = (truck.time + 100) - 60
        i = i + 1
        address = truck.packages[next_pack].address
        del truck.packages[next_pack]
    #print("total distance is: " + str(total_distance))
    for item in CSVRead.hubDistance.disList:
        if address == item.address:
            distance = item.miles[0]
    hour = (float(distance) / 18)
    minute = (hour % 1) * 60
    hour = int(hour) * 100
    time = int(hour + minute)
    truck.time = truck.time + time
    if truck.time % 100 > 60:
        truck.time = (truck.time + 100) - 60
