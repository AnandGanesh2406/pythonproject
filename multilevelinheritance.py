class grandfather:
    def ownhouse(self):
        print("House is mine")
class father(grandfather):
    def ownbike(self):
        print("Bike is mine")
class son(father):
    def ownbook(self):
        print("Love yourself")
o=son()
o.ownhouse()
o.ownbike()
o.ownbook()