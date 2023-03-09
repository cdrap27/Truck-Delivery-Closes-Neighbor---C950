#Chad Draper 007131218
#Time Complexity O(n^3)
import Interface.interface
import Model.distance;
import CSVRead.hubDistance
import CSVRead.packages
import Model.package
import deliveringAlgorithm.deliveries
import hashMap.packageHash
import loadTrucks.trucks

"""
A function is created to get a user's input from the interface and perform an action.
"""
def get_option(option):
    """
    if a user presses 1, the final report is displayed.
    if a user inputs 2, the program asks for a time.  The function then checks if the time is valid.  If the
    time is not valid, an error message is displayed based on the issue.  IF the time is correct, an interface
    function is called to return package information.
    If a user input 3, the program asks for a package.  The function then checks if the package is valid.  If the
    package is not valid, an error message is displayed based on the issue.  IF the package is correct, an interface
    function is called to return package information.
    If a user inputs 4, the program asks for a truck.  the function then checks if the turck is valid.  If the truck
    is not valid, an error message is displayed based on the issue. IF the truck is correct, an interface
    function is called to return truck information.
    If a user inputs 5, the program closes.
    O(1)
    :param option: the fucntino takes an 'option' which is the user's input based on the interface.
    :return: return
    """
    if option == '1':
        Interface.interface.display(h, truck1, truck2)
        input("Press enter to continue")
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

            elif int(hour) > 23 or int(hour) < 0:
                print("Invalid Hour Input, hour must be between 0 and 23")
                del time_input

            else:
                Interface.interface.package_time(hour, minute, h)
        except:
            print("Error: Invalid Input")
            input("Press enter to continue")
            del time_input
            option = Interface.interface.report()
            get_option(option)
        input("Press enter to continue")
        option = Interface.interface.report()
        get_option(option)
    elif option == '3':
        print("Enter a package to lookup using the Package ID")
        package_select = input()
        try:
            if 0 < int(package_select) < 41:
                Interface.interface.get_package(package_select, h)
            else:
                print("Invalid package")
                del package_select
        except:
            print("Error: Invalid Input")
            input("Press enter to continue")
            del package_select
            option = Interface.interface.report()
            get_option(option)
        input("Press enter to continue")
        option = Interface.interface.report()
        get_option(option)
    elif option == '4':
        print("Select truck 1 or 2")
        truck = input()
        if truck == '1' or truck.lower() == 'truck 1':
            truck = 1
            Interface.interface.get_truck(truck1, truck)
        elif truck == '2' or truck.lower() == 'truck 2':
            truck = 2
            Interface.interface.get_truck(truck2, truck)
        else:
            print("Error: Invalid Input")
            del truck
        input("Press enter to continue")
        option = Interface.interface.report()
        get_option(option)
    elif option == '5':
        exit()
    else:
        print("Error: Invalid Input")
        input("Press enter to continue")
        option = Interface.interface.report()
        get_option(option)


"""
createDisList creates a list of addresses and distances using the provided Distance Table
converted to a CSV file and modified for easier readability
O(n^2)
"""
CSVRead.hubDistance.createDisList()
"""
pack is used to create a duplicate list of all packages
O(n^2)
"""
pack = CSVRead.packages.setPackageList().copy()
"""
a hashmap is created using the custom hash map
O(1)
"""
h = hashMap.packageHash.packageHash()
"""
the package list is passed through the for loop and each package is added to the created hashmap
Time complexity is O(n^2)
"""
for item in CSVRead.packages.packageList:
    h.add(item.pack, item)

"""
truck 1 and truck 2 are created using the hashmap, truck, and a list of packages.
Both have time complexity of O(n)
"""
truck1 = loadTrucks.trucks.load_truck(h, loadTrucks.trucks.truck1, loadTrucks.trucks.t1run1)
truck2 = loadTrucks.trucks.load_truck(h, loadTrucks.trucks.truck2, loadTrucks.trucks.t2run1)
"""
The packages are delivered on the trucks using a nearest neighbor algorithm. 
Both have time complexity of O(n^3)
"""
deliveringAlgorithm.deliveries.closestNeighbor(truck1, 'HUB', h)
deliveringAlgorithm.deliveries.closestNeighbor(truck2, 'HUB', h)
"""
After the initial run, the trucks are recreated using a second list of packages for the trucks second run
O(n)
"""
truck1 = loadTrucks.trucks.load_truck(h, loadTrucks.trucks.truck1, loadTrucks.trucks.t1run2)
truck2 = loadTrucks.trucks.load_truck(h, loadTrucks.trucks.truck2, loadTrucks.trucks.t2run2)
"""
The packages are delivered for the second run.
O(n^3)
"""
deliveringAlgorithm.deliveries.closestNeighbor(truck1, 'HUB', h)
deliveringAlgorithm.deliveries.closestNeighbor(truck2, 'HUB', h)
"""
A function is called to display all packages and truck mileage for a final report.
O(1)
"""
Interface.interface.display(h, truck1, truck2)
"""
The program pauses until the user presses enter for easier readability
"""
input("Press enter to continue")
"""
After the user presses enter, a function is called to display interface options.
O(1)
"""
option = Interface.interface.report()
"""
The get_option function is called with the user's input as a parameter.
O(1)
"""
get_option(option)

