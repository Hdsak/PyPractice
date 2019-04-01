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
new_car=car('audi','a4',2016)
print(new_car.get_descriptive_name())
new_car.odometer_reading=23
new_car.read_odometer()
new_car.odometer_update(43)
new_car.read_odometer()