import csv
import C950.Model.distance
"""
A variable is created as a list.
"""
disList = []

"""
A function is created that creates a list of distances
"""
def createDisList():
    """
    The function opens the list of distances as a CSV file and separates each value with a comma.
    The function then separates each line and row using 2 for loops.  Each line is stored using the distance class.
    The distance is then added the the disList.
    The function has nested for loops and has a time complexity of O(n^2)
    Space complexity O(n^2)
    :return: A list of distances is returned.
    """
    with open('hubDistance.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        line_count = 0
        mi = []
        for row in csv_reader:
            line_count = 0;
            for item in row:
                if (line_count == 0):
                    nn = item
                    line_count += 1
                elif (line_count == 1):
                    aa = item
                    line_count += 1
                elif (line_count > 1):

                    mi.append(item)
                    line_count += 1
            # print(mi)
            dis = C950.Model.distance.Distance(nn, aa, mi.copy())
            disList.append(dis)

            mi.clear()
    return disList

