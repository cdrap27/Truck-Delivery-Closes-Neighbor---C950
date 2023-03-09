import csv
import Model.package
"""
A variable is created as a list.
"""
packageList = []
"""
A function is created that creates a list of packages
"""
def setPackageList():
    """
    The function opens the list of packages as a CSV file and separates each value with a comma.
    The function then separates each line and row using 2 for loops.  Each line is stored using the package class.
    The package is then added the the packageList.
    The function has nested for loops and has a time complexity of O(n^2)
    :return: returns a list of packages.
    """
    with open('packages.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        for row in csv_reader:
            itemCount = 0
            for item in row:
                if(itemCount == 0):
                    pack = item
                    itemCount += 1
                elif(itemCount == 1):
                    address = item
                    itemCount += 1
                elif(itemCount == 2):
                    city = item
                    itemCount += 1
                elif(itemCount == 3):
                    itemCount += 1
                elif(itemCount == 4):
                    zipp = item
                    itemCount += 1
                elif(itemCount == 5):
                    delivery = item
                    itemCount += 1
                elif(itemCount == 6):
                    mass = item
                    itemCount += 1
                elif(itemCount == 7):
                    special = item
            package = Model.package.Package(pack, address, city, zipp, delivery, mass, special)
            packageList.append(package)
    return packageList
