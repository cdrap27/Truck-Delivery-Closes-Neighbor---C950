import C950.loadTrucks.trucks


def display(h, truck1, truck2):
    """
    Display function prints a list of every package along with the enroute and delivered time.  The results are
    displayed using a for loop.  Since there are 40 packages, the for loop runs a constant 40 times. O(1)
    The truck information is then displayed.  Finally, the time at which both trucks are back at the hub as well as the
    total mileage is displayed.
    :param h: hash map of packages
    :param truck1: truck 1
    :param truck2: truck 2
    :return: return
    """
    for i in range(1, 41):
        i = str(i)
        hours = int(h.get(i).delivered / 100)
        minutes = int(h.get(i).delivered % 100)
        enroute_hours = int(h.get(i).enroute / 100)
        enroute_minutes = int(h.get(i).enroute % 100)
        print(h.get(i).pack + " delivered: " + str(hours) + ":" + str(minutes).zfill(2) + " enroute: " + str(enroute_hours)
              + ":" + str(enroute_minutes).zfill(2))

    hours1 = int(truck1.time / 100)
    minutes1 = int(truck1.time % 100)
    time = truck1.time - 800
    miles = int(time/100 * 18)
    miles = float(miles + (((time % 100) / 60) * 18))
    temp = miles
    print("Truck 1 arrived back at the Hub at: " + str(hours1) + ":" + str(minutes1).zfill(2) + " and traveled "
          + str(miles) + " miles.")

    hours2 = int(truck2.time / 100)
    minutes2 = int(truck2.time % 100)
    time = truck2.time - 800
    miles = int(time / 100 * 18)
    miles = float(miles + (((time % 100) / 60) * 18))
    print("Truck 2 arrived back at the Hub at: " + str(hours2) + ":" + str(minutes2).zfill(2) + " and traveled "
          + str(miles) + " miles.")

    miles = temp + miles

    if truck1.time > truck2.time:
        print("All packages delivered at " + str(hours1) + ":" + str(minutes1).zfill(2))
    else:
        print("All packages delivered at " + str(hours2) + ":" + str(minutes2).zfill(2))

    print("Total miles traveled: " + str(miles))



def report():
    """
    This displays an interface of options to choose from and takes an option.
    :return: User's option is returned.
    """
    print("Enter a number to select from the following operations:\n")
    print("1. Display All")
    print("2. Show Package Status at Selected Time")
    print("3. Show Specific Package Detailed Information")
    print("4. Show Specific Truck Detailed Information")
    print("5. Exit")
    option = input('Enter a number: ')
    return option

def package_time(hour, minute, h):
    """
    Shows the status of all packages at a certain time.  Uses a for loop of a constant time since the number of packages
    is known. O(1)
    :param hour: User's hour input
    :param minute: User's minute input
    :param h: hashmap of packages
    :return: return
    """
    print("Package Status as of " + str(hour) + ":" + str(minute).zfill(2))
    time = hour * 100 + minute
    for i in range(1, 41):
        print("Package " + str(h.get(str(i)).pack) + " is: ", end=' ')
        if h.get(str(i)).delivered == time or h.get(str(i)).delivered < time:
            print("delivered.")
        elif h.get(str(i)).enroute == time or h.get(str(i)).enroute < time:
            print("enroute.")
        else:
            print("still at the hub.")

def get_package(id, h):
    """
    takes an id and returns all the package details for given id.
    :param id: package id
    :param h: hash map of packages
    :return: return
    """
    id = str(id)
    time = h.get(id).atHub
    hour = int(time / 100)
    minute = int(time % 100)
    print("Package " + id + " at hub: " + str(hour) + ":" + str(minute).zfill(2))
    time = h.get(id).enroute
    hour = int(time / 100)
    minute = int(time % 100)
    print("Package " + id + " enroute: " + str(hour) + ":" + str(minute).zfill(2))
    time = h.get(id).delivered
    hour = int(time / 100)
    minute = int(time % 100)
    print("Package " + id + " delivered: " + str(hour) + ":" + str(minute).zfill(2))
    print("Delivery deadline: " + h.get(id).delivery)
    print("Delivery address: " + h.get(id).address + ", " + h.get(id).city + ", UT " + str(h.get(id).zip))
    print("Package weight: " + str(h.get(id).mass) + " Kilos")
    print("Special notes: " + h.get(id).specialNotes)

def get_truck(truck, id):
    """
    Returns all truck information for given truck id.  Uses a for loop to display packages delivered. O(n)
    :param truck: truck for returning information
    :param id: id of truck
    :return: return
    """
    if id == 1:
        num1 = len(C950.loadTrucks.trucks.t1run1)
        num2 = len(C950.loadTrucks.trucks.t1run2)
    if id == 2:
        num1 = len(C950.loadTrucks.trucks.t2run1)
        num2 = len(C950.loadTrucks.trucks.t2run2)
    hour = int(truck.time / 100)
    minute = int(truck.time % 100)
    distance = (float(minute / 60) + float(hour - 8)) * 18
    distance = round(distance, 2)
    miles = int((truck.time - 800) / 100 * 18)
    miles = float(miles + ((((truck.time - 800) % 100) / 60) * 18))
    print("Truck " + str(id) + " delivered " + str(num1 + num2) + " packages total.")
    print("Truck " + str(id) + " made 2 runs.")
    print("Truck " + str(id) + " traveled a total of " + str(miles) + " miles.")
    print("Truck " + str(id) + " returned to the HUB after delivering all packages at " + str(hour) + ":" + str(minute).zfill(2))
    print("The first run delivered the following packages: \n" + "Package:", end=" ")

    if id == 1:
        for i, item in enumerate(C950.loadTrucks.trucks.t1run1):
            if i == len(C950.loadTrucks.trucks.t1run1) -1:
                print(str(item))
            else:
                print(str(item) + ",", end=' ')
        print("The second run delivered the following packages: \n" + "Package:", end=" ")
        for i, item in enumerate(C950.loadTrucks.trucks.t1run2):
            if i == len(C950.loadTrucks.trucks.t1run2) - 1:
                print(str(item))
            else:
                print(str(item) + ",", end=' ')

    if id == 2:
        for i, item in enumerate(C950.loadTrucks.trucks.t2run1):
            if i == len(C950.loadTrucks.trucks.t2run1) -1:
                print(str(item))
            else:
                print(str(item) + ",", end=' ')
        print("The second run delivered the following packages: \n" + "Package:", end=" ")
        for i, item in enumerate(C950.loadTrucks.trucks.t2run2):
            if i == len(C950.loadTrucks.trucks.t2run2) - 1:
                print(str(item))
            else:
                print(str(item) + ",", end=' ')
