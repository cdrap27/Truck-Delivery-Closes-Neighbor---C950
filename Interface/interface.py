

def display(h, truck1, truck2):
    for i in range(1, 41):
        i = str(i)
        hours = int(h.get(i).delivered / 100)
        minutes = int(h.get(i).delivered % 100)
        print(h.get(i).pack + " delivered: " + str(hours) + ":" + str(minutes).zfill(2) + " enroute: " + str(h.get(i).enroute))

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
    print("Enter a number to select from the following operations:\n")
    print("1. Display All")
    print("2. ")
    print("4. Exit")

    option = input('Enter a number: ')
    return option




