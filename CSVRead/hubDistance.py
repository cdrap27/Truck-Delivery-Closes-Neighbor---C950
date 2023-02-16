import csv
import Model.distance

disList = []
with open('hubDistance.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    line_count = 0
    mi = []
    for row in csv_reader:
        line_count = 0;
        for item in row:
            if(line_count == 0):
                nn = item
                line_count +=1
            elif(line_count == 1):
                aa = item
                line_count += 1
            elif(line_count > 1):

                mi.append(item)
                line_count += 1
        print(mi)
        dis = Model.distance.Distance(nn, aa, mi)
        disList.append(dis)
        #mi.clear()

print(disList[10].miles[0])

