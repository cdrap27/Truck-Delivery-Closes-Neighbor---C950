import Model.truck

pack1 = []
pack2 = []

truck1 = Model.truck.Truck(pack1)
truck2 = Model.truck.Truck(pack2)
t1run1 = ['1', '2', '4', '5', '7', '12', '27', '29', '30', '33', '35', '39']
t2run1 = ['13', '14', '15', '16', '18', '19', '20', '21', '22', '24', '34', '36']
t1run2 = ['25', '11', '17', '6', '23', '26', '40']
t2run2 = ['3', '8', '9', '10', '28', '37', '38']

def load_truck(h, truck, run):
    truck.packages.clear()
    for item in run:
        truck.packages.append(h.get(item))
    return truck


