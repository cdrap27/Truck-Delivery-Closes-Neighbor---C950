import CSVRead.hubDistance

"""
closestNeighbor function calculates which package to deliver next and delivers each package.
"""
def closestNeighbor(truck, address, h):
    """
    Closest neighbor is a self adjusting algorithm that calculates the closest package delivery address that still
    needs to be delivered.  The function delivers that package and calculates the next closest delivery address.
    This is repeated until every package has been delivered.
    The function uses a While loop to continue running until all packages have been delivered. O(n)
    A for loop is then used to find the current address in the list of distances. O(n)
    The distance is set to 100. In order to find the lowest distance, the initial distance is set at 100.
    A for loop then enumerates through the packages in the truck and a second for loop enumerates through the
    list of distances. O(n^2)
    Once a match of addresses is found, the algorithm checks the distance using the indices.
    Since the distance list is only half filled out, if there is no value for the indices given, the indices are
    reversed to find the distance.  If the distance is less than the current distance, that distance is set and the
    address of that package is also set.  The algorithm checks the remaining packages and the lowest distance remains.
    After exiting the for loop, the time is calculated using the distance.  The package is then set as delivered along
    with the time.  The trucks time is also updated.  The current package is deleted and the algorithm loops again
    until no packages remain. After all packages have been delivered, The distance to the hub is calculated and added
    to the truck using a for loop before exiting the function. O(n)
    Total time complexity O(n^3)
    Space complexity O(n^3)
    :param truck: a truck is passed in which has a list of packages to be delivered.
    :param address: an address is passed in as the current address where the truck is located.
    :param h: h is passed in as a hash map of packages.
    :return: return
    """
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
