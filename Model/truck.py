class Truck:
    """
    truck class
    """
    def __init__(self, packages):
        self.packages = packages
        self.distance = 0
        self.time = 800
        self.currLocation = 'HUB'
