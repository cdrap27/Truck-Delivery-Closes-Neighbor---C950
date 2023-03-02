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

x = 0

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
    if option == '1':
        Interface.interface.display(h, truck1, truck2)
        option = Interface.interface.report()
        get_option(option)
    elif option == '2':
        print("Enter a time to return all package information.\n" +
              "Please use military time i.e. 3:00 is 3:00 A.M.\n" +
              "Format X:XX")
        time_input = input()
        try:
            time = time_input.split(':')
            hour = int(time[0])
            minute = int(time[1])
            if int(minute) > 59 or int(minute) < 0:
                print("Invalid Minutes Input, minutes must be between 0 and 59.")
                del time_input
                option = Interface.interface.report()
                get_option(option)
            elif int(hour) > 23 or int(hour) < 0:
                print("Invalid Hour Input, hour must be between 0 and 23")
                del time_input
                option = Interface.interface.report()
                get_option(option)
            else:
                Interface.interface.package_time(hour, minute, h)
        except:
            print("Error: Invalid Input")
            del time_input
            option = Interface.interface.report()
            get_option(option)
    elif option == '3':
        print("in progress")
    elif option == '5':
        exit()
    else:
        print("Error: Invalid Input")
        option = Interface.interface.report()
        get_option(option)


get_option(option)

