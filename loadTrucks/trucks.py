import C950.Model.truck
"""
creates 2 variables of type list
"""
pack1 = []
pack2 = []
"""
creates 2 trucks
"""
truck1 = C950.Model.truck.Truck(pack1)
truck2 = C950.Model.truck.Truck(pack2)
"""
list of packages for each run, manually loaded
"""
t1run1 = ['1', '2', '4', '5', '7', '12', '27', '29', '30', '33', '35', '39', '40']
t2run1 = ['13', '14', '15', '16', '18', '19', '20', '21', '22', '24', '31',  '34', '36', '37', '38']
t1run2 = ['6',  '25']
t2run2 = ['3',  '8', '9', '10', '11', '17',  '23', '26', '28', '32']

def load_truck(h, truck, run):
    """
    clears the trucks package list and adds packages to the truck using a for loop O(n)
    :param h: hash map of packages
    :param truck: truck to be loaded
    :param run: list of packages on each run
    :return: returns truck loaded with packages
    """
    truck.packages.clear()
    for item in run:
        truck.packages.append(h.get(item))
        h.get(item).enroute = truck.time
    return truck


