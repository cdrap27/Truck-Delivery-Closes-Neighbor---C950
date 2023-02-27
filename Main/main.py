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

truck1 = loadTrucks.trucks.load_truck1(h)

print(CSVRead.hubDistance.disList[0].address)
