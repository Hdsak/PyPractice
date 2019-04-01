class car():
    """Simple  car class"""
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """Return best formatted name"""
        long_name=str(self.model).title()+" "+str(self.year).title()+" "+str(self.make).title()
        return long_name
    def odometer_update(self,value):
        self.odometer_reading=value
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it")
class battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=265
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class electric_car(car):
    def __init__(self,make,model,year):
        """Constructor for electric car"""
        super().__init__(make,model,year)
        self.battery_size=battery()
    

my_electric_car=electric_car("AUdi",'a4',2016)
print(my_electric_car.get_descriptive_name())
my_electric_car.battery_size.describe_battery()
my_electric_car.battery_size.get_range()
