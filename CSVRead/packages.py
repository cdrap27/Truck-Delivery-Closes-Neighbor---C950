import csv
import Model.package

packageList = []
def setPackageList():
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
