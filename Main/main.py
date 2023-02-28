import Model.distance;
import CSVRead.hubDistance
import CSVRead.packages
import Model.package
import deliveringAlgorithm.deliveries
import hashMap.packageHash
import loadTrucks.trucks

CSVRead.hubDistance.createDisList()
pack = CSVRead.packages.setPackageList().copy()

#print(CSVRead.hubDistance.disList[1].miles[0])
#print(CSVRead.packages.packageList[2].specialNotes)

h = hashMap.packageHash.packageHash()

for item in CSVRead.packages.packageList:
    h.add(item.pack, item)

#h.print()
i = None

#print(h.get('19').address)

for item in CSVRead.hubDistance.disList:
    #print(h.get('13').address + "new one " +  item.address)
    if h.get('13').address == item.address:
        i = item
test = '40'
#print(h.get(test).delivered)
truck1 = loadTrucks.trucks.load_truck(h, loadTrucks.trucks.truck1, loadTrucks.trucks.t1run1)
truck2 = loadTrucks.trucks.load_truck(h, loadTrucks.trucks.truck2, loadTrucks.trucks.t2run1)
deliveringAlgorithm.deliveries.closestNeighbor(truck1, 'HUB', h)
deliveringAlgorithm.deliveries.closestNeighbor(truck2, 'HUB', h)
truck1 = loadTrucks.trucks.load_truck(h, loadTrucks.trucks.truck1, loadTrucks.trucks.t1run2)
truck2 = loadTrucks.trucks.load_truck(h, loadTrucks.trucks.truck2, loadTrucks.trucks.t2run2)
deliveringAlgorithm.deliveries.closestNeighbor(truck1, 'HUB', h)
deliveringAlgorithm.deliveries.closestNeighbor(truck2, 'HUB', h)
#deliveringAlgorithm.deliveries.closestNeighbor(truck2, 'HUB', h)
print("delivered at: " + str(h.get('17').delivered))
print(truck1.time)
#print(truck2.time)
#print(CSVRead.hubDistance.disList[2].address)

#print(CSVRead.hubDistance.disList[0].address)
