import Model.distance;
import CSVRead.hubDistance
import CSVRead.packages
import Model.package
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

truck1 = loadTrucks.trucks.load_truck(h, loadTrucks.trucks.truck1, loadTrucks.trucks.t1run1)
truck2 = loadTrucks.trucks.load_truck(h, loadTrucks.trucks.truck2, loadTrucks.trucks.t2run1)
print(len(truck1.packages))
print(len(truck2.packages))
truck1 = loadTrucks.trucks.load_truck(h, loadTrucks.trucks.truck1, loadTrucks.trucks.t1run2)
truck2 = loadTrucks.trucks.load_truck(h, loadTrucks.trucks.truck2, loadTrucks.trucks.t2run2)
print(len(truck1.packages))
print(len(truck2.packages))

print(CSVRead.hubDistance.disList[0].address)
