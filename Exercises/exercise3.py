"""A template for a python script deliverable for INST326.
Driver: Arianna Alimi
Navigator: None
Assignment: Exercise 3
Date: 9_25_2024
Challenges Encountered: The move_x and move_y was a challenge because I was not adding theX to the self position, however I was able to overcome this issue.
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

        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def move_x(self, theX):

        """
        Move initial x position user input amount

        Arguments:
        theX(int): user input amount of positions to move the vehicle x position

        Returns:
        None

        """

        self.x_pos += theX

    def move_y(self, theY):

        """
        Move initial y position user input amount

        Arguments:
        theY(int): user input amount of positions to move the vehicle y position

        Returns:
        None

        """

        self.y_pos += theY
    
    def vehicle_position(self):

        """
        String builder for x and y positions

        Arguments:
        None

        Returns:
        A string with the x and y position of vehicle

        """

        return f"x_pos: {self.x_pos} y_pos: {self.y_pos}"
    
    def __str__(self):
        
        """
        String builder for the information of the vehicle

        Arguments:
        None

        Returns:
        A string with the year, make, model, engine, x and y positions

        """

        return f"{self.year} {self.make} {self.model} {self.engine} ({self.x_pos}, {self.y_pos})"
        


def main():
    vehicle1 = Vehicle("Toyota","Tundra",2022,"V6 Hybrid")
    vehicle2 = Vehicle("BMW","328d",2014,5,10)
    print(vehicle1 )
    print(vehicle1.vehicle_position() )
    vehicle1.move_x(2)
    vehicle1.move_y(3)
    print(vehicle1.vehicle_position() )
    print(vehicle2 )
    print(vehicle2.vehicle_position() )
    vehicle2.move_x(2)
    vehicle2.move_y(3)
    print(vehicle2.vehicle_position() )


if __name__ == "__main__":
    main()
