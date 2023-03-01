import Model.truck

pack1 = []
pack2 = []

truck1 = Model.truck.Truck(pack1)
truck2 = Model.truck.Truck(pack2)
t1run1 = ['1', '2', '4', '5', '6', '7', '12', '27', '29', '30', '33', '35', '39', '40']
t2run1 = ['13', '14', '15', '16', '18', '19', '20', '21', '22', '24', '31', '32', '34', '36', '37', '38']
t1run2 = ['25', '11', '17',  '23', '26']
t2run2 = ['3', '8', '9', '10', '28']

def load_truck(h, truck, run):
    truck.packages.clear()
    for item in run:
        truck.packages.append(h.get(item))
    return truck


