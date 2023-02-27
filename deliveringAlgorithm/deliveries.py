import CSVRead.hubDistance


def closestNeighbor(truck, address, h):
    i = 0

    while len(truck.packages) > 0:
        distance = 100
        next_pack = 0
        if i == 16:
            break
        for pack, item in enumerate(truck.packages):

            for index, add in enumerate(CSVRead.hubDistance.disList):
                if item.address == add.address:
                    print(index)
                    if float(CSVRead.hubDistance.disList[index].miles[0]) < distance:
                        distance = float(CSVRead.hubDistance.disList[index].miles[0])
                        next_pack = pack
                    print(distance, "miles")
                    print("next package", pack)
        hour = (distance / 18)
        minute = (hour % 1) * 60
        hour = int(hour) * 100
        print("" + str(hour) + str(minute))
        time = hour + minute
        ha = str(truck.packages[next_pack].pack)
        h.get(ha).delivered = time + truck.time
        truck.time = truck.time + time
        i = i + 1

        print(len(truck.packages))
        del truck.packages[next_pack]
        print(len(truck.packages))
