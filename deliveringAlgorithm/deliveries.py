import CSVRead.hubDistance


def closestNeighbor(truck, address, h):
    i = 0
    j = 0
    while len(truck.packages) > 0:
        for address_index, name in enumerate(CSVRead.hubDistance.disList):
            if name.address == address:
                j = address_index
        print(j)

        distance = 100
        next_pack = 0
        if i == 16:
            break
        for pack, item in enumerate(truck.packages):

            for index, add in enumerate(CSVRead.hubDistance.disList):
                if item.address == add.address:
                    #print(index)
                    try:
                        if float(CSVRead.hubDistance.disList[index].miles[j]) < distance:
                            distance = float(CSVRead.hubDistance.disList[index].miles[j])
                            #print("distance = " + str(distance))
                            next_pack = pack
                    except:
                        #print("exception was executes")
                        if float(CSVRead.hubDistance.disList[j].miles[index]) < distance:
                            distance = float(CSVRead.hubDistance.disList[j].miles[index])
                            next_pack = pack
                        #print("distance = " + str(distance))
                    #print(distance, "miles")
                    #print("next package", pack)
        #print(distance)
        #print(address)
        hour = (distance / 18)
        minute = (hour % 1) * 60
        hour = int(hour) * 100
        print("distance is " + str(distance))
        print("" + str(hour) + str(minute))
        time = int(hour + minute)
        ha = str(truck.packages[next_pack].pack)
        h.get(ha).delivered = time + truck.time
        print(truck.time)
        print(time)
        truck.time = truck.time + time
        print(truck.time)
        i = i + 1
        print(truck.packages[next_pack].pack)
        #print(len(truck.packages))
        address = truck.packages[next_pack].address
        del truck.packages[next_pack]
        #print(len(truck.packages))
