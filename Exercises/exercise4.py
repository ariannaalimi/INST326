
"""A template for a python script deliverable for INST326.
Driver: Arianna Alimi
Navigator: None
Assignment: Template INST326
Date: 10_5_24
Challenges Encountered: Ensuring that the engine is set to the correct one
"""
# YOUR CODE HERE
# This is where you will create your Vehicle class and all of the methods and attributes
# CODE BELOW HERE IS HELPER CODE. It will not work until you create your class correctly so you may want to
# comment out some of the code below or start with your own script

class Vehicle:
    def __init__(self, make, model, year, engine, x_pos = 0, y_pos = 0):

        """
        Initializes instance of class with attributes

        Arguments:
        make(str): the make of the car
        model(str): the model of the car
        year(int): the year of the car
        engine(str): the type of engine in car
        x_pos(int): x-coordinate of vehicle position
        y_pos(int): y-coordinate of vehicle position

        Returns:
        None

        """


        self._make = make
        self._model = model
        self._year = year
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._engine = engine

        if(self._engine == "v6" or self._engine == "v8" or self._engine == "i4"):
            self.engine = engine
        else:
            self._engine = "Not Specified"


    def get_make(self):

        """
        Returns make of the car

        Arguments:
        None

        Returns:
        Make of the car

        """

        return self._make

    def set_make(self, make):

        """
        Sets the make of the car

        Arguments:
        make(str) : the make of the car

        Returns:
        None

        """


        self._make = make
    
    def get_model(self):

        """
        Returns model of the car

        Arguments:
        None

        Returns:
        Model of the car

        """

        return self._model
    
    def set_model(self, model):

        """
        Sets the model of the car

        Arguments:
        model(str): the model of the car

        Returns:
        None

        """


        self._model = model
    
    def get_year(self):

        """
        Returns year of the car

        Arguments:
        None

        Returns:
        Year of car

        """


        return self._year
    
    def set_year(self, year):

        """
        Sets the year of the car

        Arguments:
        year(int): the year of the car

        Returns:
        None

        """

        self._year = year
    

    def get_engine(self):

        """
        Returns engine of the car

        Arguments:
        None

        Returns:
        Engine of the car

        """

        return self._engine

    def set_engine(self, engine):

        """
        Sets the engine of the car if v6, v8 or i4

        Arguments:
        engine(str): the type of engine in car

        Returns:
        None

        """

        if(engine == "v6" or engine == "v8" or engine == "i4"):
            self._engine = engine
        else:
            self._engine = "Not Specified"

    def get_x_pos(self):

        """
        Returns x position of the car

        Arguments:
        None

        Returns:
        X position of car

        """

        return self._x_pos
    
    def set_x_pos(self, x_pos):

        """
        Sets the x position of the car

        Arguments:
        x_pos(int): x-coordinate of vehicle position

        Returns:
        None

        """


        self._x_pos = x_pos
    
    def get_y_pos(self):

        """
        Returns y position of the car

        Arguments:
        None

        Returns:
        Y position of the car

        """

        return self._y_pos
    
    def set_y_pos(self, y_pos):
        """
        Sets the x position of the car

        Arguments:
        y_pos(int): y-coordinate of vehicle position

        Returns:
        None

        """

        self._y_pos = y_pos

    def move_x(self, move_x):

        """
        Moves the car by the number of x positions

        Arguments:
        move_x(int): the umber of x positions to move

        Returns:
        None

        """


        self._x_pos += move_x

    def move_y(self, move_y):

        """
        Moves the car by the number of y positions

        Arguments:
        move_y(int): the umber of y positions to move

        Returns:
        None

        """


        self._y_pos += move_y

    def vehicle_info(self):

        """
        Returns the vehicles year, make, and model

        Arguments:
        None

        Returns:
        A string of the vehicles year, make, and model

        """


        return (f"{self._year} {self._make} {self._model}")
    
    def vehicle_position(self):

        """
        Returns the vehicles x and y position

        Arguments:
        None

        Returns:
        A string of the vehicles x position and y position

        """


        return (f"x_pos: {self._x_pos} y_pos: {self._y_pos}")
    
    def __str__(self):

        """
        Returns a string of the vehicles information

        Arguments:
        None

        Returns:
        A string of the vehicles year, make, model, and engine

        """


        return (f"Year: {self._year} Make: {self._make} Model: {self._model} Engine: {self._engine}")
    
    def __repr__(self):

        """
        Returns a string of the vehicles information

        Arguments:
        None

        Returns:
        A string of the vehicles year, make, model, and engine

        """


        return (f"Class(Year: {self._year} Make: {self._make} Model: {self._model} Engine: {self._engine})")
    


def main():
    vehicle1 = Vehicle("Toyota","Tundra",2022,"v6 hybrid")
    vehicle2 = Vehicle("BMW","328d",2014,"v6",5,10)
    vehicle3 = Vehicle("Nissan","Pathfinder",2015,"v6",3,-2)
    vehicle4 = Vehicle("Toyota","Prius",2011,"i4",15,8)
    str(vehicle1)
    print(vehicle1.vehicle_position() )
    vehicle1.move_x(2)
    vehicle1.move_y(3)
    print(vehicle1.vehicle_position() )
    str(vehicle2)
    print(vehicle2.vehicle_position() )
    vehicle2.move_x(2)
    vehicle2.move_y(3)
    print(vehicle2.vehicle_position() )
    print(vehicle1)
    print(repr(vehicle1))
    print(vehicle2)
    print(repr(vehicle2))
    print(vehicle3)
    print(repr(vehicle3))
    print(vehicle4)
    print(repr(vehicle4))
    vehicle4.set_make("Mazda")
    vehicle4.set_model("CX5")
    vehicle4.set_year("2021")
    vehicle4.set_x_pos(11)
    vehicle4.set_y_pos(33)
    vehicle4.set_engine("v6")
if __name__ == "__main__":
    main()
