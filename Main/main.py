import Interface.interface
import Model.distance;
import CSVRead.hubDistance
import CSVRead.packages
import Model.package
import deliveringAlgorithm.deliveries
import hashMap.packageHash
import loadTrucks.trucks

CSVRead.hubDistance.createDisList()
pack = CSVRead.packages.setPackageList().copy()

h = hashMap.packageHash.packageHash()

for item in CSVRead.packages.packageList:
    h.add(item.pack, item)

truck1 = loadTrucks.trucks.load_truck(h, loadTrucks.trucks.truck1, loadTrucks.trucks.t1run1)
truck2 = loadTrucks.trucks.load_truck(h, loadTrucks.trucks.truck2, loadTrucks.trucks.t2run1)
deliveringAlgorithm.deliveries.closestNeighbor(truck1, 'HUB', h)
deliveringAlgorithm.deliveries.closestNeighbor(truck2, 'HUB', h)
truck1 = loadTrucks.trucks.load_truck(h, loadTrucks.trucks.truck1, loadTrucks.trucks.t1run2)
truck2 = loadTrucks.trucks.load_truck(h, loadTrucks.trucks.truck2, loadTrucks.trucks.t2run2)
deliveringAlgorithm.deliveries.closestNeighbor(truck1, 'HUB', h)
deliveringAlgorithm.deliveries.closestNeighbor(truck2, 'HUB', h)
Interface.interface.display(h, truck1, truck2)
option = Interface.interface.report()


def get_option(option):
    print(option)
    if option == '1':
        Interface.interface.display(h, truck1, truck2)
        option = Interface.interface.report()
        get_option(option)
    elif option == '2':
        print("In progress")
        option = Interface.interface.report()
        get_option(option)
    elif option == '4':
        exit()
    else:
        print("Error: Invalid Input")
        option = Interface.interface.report()
        get_option(option)


get_option(option)

