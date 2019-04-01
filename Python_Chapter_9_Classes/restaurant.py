class restaurant():
    """Restaurant class"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("This restaurant is "+str(self.restaurant_name))
        print("Cuisine is "+ self.cuisine_type)
    def open_restaurant(self):
        print(str(self.restaurant_name) + " is open")
class IceCreamStand(restaurant):
    """IceCreamStand"""
    def __init__(self,restaurant_name,cuisine_type,*flavors):
        """Constructor"""
        super().__init__(restaurant,cuisine_type)
        self.flavors=flavors
    def print_IceCream(self):
        print("Ice cream involved")
        for n in self.flavors:
            print(n)