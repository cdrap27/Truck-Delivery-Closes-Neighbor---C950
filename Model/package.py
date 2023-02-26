class Package():
    def __init__(self, pack, address, city, zip, delivery, mass, specialNotes):
        self.pack = pack
        self.address = address
        self.city = city
        self.zip = zip
        self.delivery = delivery
        self.mass = mass
        self.specialNotes = specialNotes
        self.delivered = None
        self.enroute = None
        self.atHub = 800



