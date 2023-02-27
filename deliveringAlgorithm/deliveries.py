def closestNeighbor(truck):
    address = 'HUB'
    i = 0
    for item in truck.packages:
        if i == 16:
            break
