import Model.truck

pack1 = []
pack2 = []

truck1 = Model.truck.Truck(pack1)
truck2 = Model.truck.Truck(None)
t1run1 = ['1', '2', '4', '5', '7', '12', '27', '29', '30', '33', '35', '39']
t2run1 = ['13', '14', '15', '16', '18', '19', '20', '21', '22', '24', '34', '36']

def load_truck1(h):
    for item in t1run1:
        truck1.packages.append(h.get(item))
    return truck1

def load_truck2(h):
    for item in t2run1:
        truck2.packages.append(h.get(item))
    return truck2
