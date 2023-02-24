import Model.distance;
import CSVRead.hubDistance
import CSVRead.packages
import Model.package
import hashMap.packageHash

CSVRead.hubDistance.createDisList()
pack = CSVRead.packages.setPackageList().copy()

print(CSVRead.hubDistance.disList[1].name)
print(CSVRead.packages.packageList[2].specialNotes)

h = hashMap.packageHash.packageHash()

for item in CSVRead.packages.packageList:
    h.add(item.pack, item)

h.print()

yo =h.get('3')

print(yo.specialNotes)
