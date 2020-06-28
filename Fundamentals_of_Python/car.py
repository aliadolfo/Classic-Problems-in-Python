class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # Return a neatly formatted descriptive name
        long_name = "Factory {0} model: {1} and year: {2} ".format(self.make, self.model, self.year)
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        return "This car has {0} miles on it".format(self.odometer_reading)

    def update_odometer(self, mileage):
        """ 
        Set the odometer reading to the given value.
        Reject the change if attemps to roll the odometer back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """
        add given amount to the odometer reading
        """
        self.odometer_reading += miles

class Battery:
    # attempt to a model battery for an electric car

    def __init__(self, battery_size = 75):
        # Initialize the Battery's  attributes
        self.battery_size = battery_size

    def describe_battery(self):
        return "This car has a {0}-KWh battery.".format(self.battery_size)

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        return "This car can go about {0} miles on a full charge".format(range)


class ElectricCar(Car):
    """
    Represent aspects of a car, 
    specific to electric vehicles
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes  of the parent class
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Return a statement describing the battery size."""
        return "this car has a {0}-KWh battery.".format(self.battery_size)

    """
    The super() function allows you to call a method
    from the parent class.
    The name super comes from a convention of calling
    the parent  class a superclass and child
    class a subclass
    """


if '__main__'==__name__:
    
    # My new car object
    my_new_car = Car('audi', 'a4', 2019)
    print(">>>> ", my_new_car.get_descriptive_name())
    print("<<<< odometer : ", my_new_car.read_odometer())
    
    # Used Car Object
    my_used_car = Car('subaru', 'outback', 2015)
    print("Used Car >>> : ", my_used_car.get_descriptive_name())
    print("Update odometer <<<< : ", my_used_car.update_odometer(23500))
    my_used_car.increment_odometer(100) # increment odometer
    print("read odometer >>>>> : ", my_used_car.read_odometer())

    # Electric Car
    my_tesla = ElectricCar('tesla', 'model s', 2019)
    print(" # Tesla >>> : ", my_tesla.get_descriptive_name())
    print(" # Tesla battery : ", my_tesla.battery.describe_battery())
    print(" # Tesla battery range : ", my_tesla.battery.get_range())
