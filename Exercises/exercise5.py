"""A template for a python script deliverable for INST326.
Driver: Arianna Alimi
Navigator: None
Assignment: Exercise 5
Date: 10_25_24
Challenges Encountered: Initializing parent class and ensuring that the _init_ arguments were inputted correctly
"""
# YOUR CODE HERE

class Vehicle:

    def __init__(self, make, model, year, x_pos = 0, y_pos = 0):

        """
        Initializes instance of class with attributes

        Arguments:
        make(str): the make of the car
        model(str): the model of the car
        year(int): the year of the car
        x_pos(int): x-coordinate of vehicle position
        y_pos(int): y-coordinate of vehicle position

        Returns:
        None

        """

        #initialize attributes
        self._make = make
        self._model = model
        self._year = year
        self._x_pos = x_pos
        self._y_pos = y_pos
        

    @property
    def make(self):

        """
        Returns make of the car

        Arguments:
        None

        Returns:
        Make of the car

        """

        return self._make

    @make.setter
    def make(self, make):

        """
        Sets the make of the car

        Arguments:
        make(str) : the make of the car

        Returns:
        None

        """


        self._make = make
    
    @property
    def model(self):

        """
        Returns model of the car

        Arguments:
        None

        Returns:
        Model of the car

        """

        return self._model
    
    @model.setter
    def model(self, model):

        """
        Sets the model of the car

        Arguments:
        model(str): the model of the car

        Returns:
        None

        """


        self._model = model
    
    @property
    def year(self):

        """
        Returns year of the car

        Arguments:
        None

        Returns:
        Year of car

        """


        return self._year
    
    @year.setter
    def year(self, year):

        """
        Sets the year of the car

        Arguments:
        year(int): the year of the car

        Returns:
        None

        """

        self._year = year
    

    
    @property
    def x_pos(self):

        """
        Returns x position of the car

        Arguments:
        None

        Returns:
        X position of car

        """

        return self._x_pos
    
    @x_pos.setter
    def x_pos(self, x_pos):

        """
        Sets the x position of the car

        Arguments:
        x_pos(int): x-coordinate of vehicle position

        Returns:
        None

        """


        self._x_pos = x_pos
    
    @property
    def y_pos(self):

        """
        Returns y position of the car

        Arguments:
        None

        Returns:
        Y position of the car

        """

        return self._y_pos
    
    @y_pos.setter
    def y_pos(self, y_pos):
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

        #adds move_x to current x position
        self._x_pos += move_x

    def move_y(self, move_y):

        """
        Moves the car by the number of y positions

        Arguments:
        move_y(int): the umber of y positions to move

        Returns:
        None

        """

        #adds move_y to current y-position
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
        A string of the vehicles year, make, and model

        """


        return (f"Year: {self._year} Make: {self._make} Model: {self._model}")
    
    def __repr__(self):

        """
        Returns a string of the vehicles information

        Arguments:
        None

        Returns:
        A string of the vehicles year, make, and model

        """


        return (f"Vehicle(Year: {self._year} Make: {self._make} Model: {self._model})")
     
class Bicycle(Vehicle):

    def __init__(self, make, model, year, bicycle_type, frame_material, gears, x_pos = 0, y_pos = 0):

        """
        Initializes instance of class with attributes

        Arguments:
        make(str): the make of the car
        model(str): the model of the car
        year(int): the year of the car
        bicycle_type(str): the type of bicycle
        frame_material(str): the frame material of the bike
        gears(int): the number value gear on a bike
        x_pos(int): x-coordinate of vehicle position
        y_pos(int): y-coordinate of vehicle position
        current_gear(int): the current gear the bike is set at

        Returns:
        None

        """

        #initialize parent class
        super().__init__(make, model, year, x_pos, y_pos)

        #initialize attributes
        self._bicycle_type = bicycle_type
        self._frame_material = frame_material
        self._gears = gears
        self.current_gear = 1
    
    @property
    def bicycle_type(self):

        """
        Returns the bicycle type

        Arguments:
        None

        Returns:
        A string of the bicycle type (road, mountain, hybrid)

        """


        return self._bicycle_type
    
    @bicycle_type.setter
    def bicycle_type(self, bicycle_type):

        """
        Sets the bicycle type

        Arguments:
        bicycle_type(str): the type of bicycle (road, mountain, hybrid)

        Returns:
        None

        """

        #checks if user inputed either road, mountain, or hybrid for bicycle type
        if((bicycle_type == "road") or (bicycle_type == "mountain") or (bicycle_type == "hybrid")):
            self._bicycle_type = bicycle_type
    

    @property
    def frame_material(self):

        """
        Returns the frame material of bicycle

        Arguments:
        None

        Returns:
        A string of the frame material (carbon, steel, aluminum, alloy)

        """


        return self._frame_material
    
    @frame_material.setter
    def frame_material(self, frame_material):

        """
        Sets the frame material of the bicycle

        Arguments:
        frame_material(str): the frame material of the bicycle (carbon, steel, aluminum, alloy)

        Returns:
        None

        """

        #checks if user input valid string (carbon, steel, aluminum, alloy)
        if((frame_material == "carbon") or (frame_material == "steel") or (frame_material == "aluminum") or (frame_material == "alloy")):
            self._frame_material = frame_material

    @property
    def gears(self):

        """
        Returns the gear of the bicycle

        Arguments:
        None

        Returns:
        An integer of the bicycle's gear

        """


        return self._gears
    
    @gears.setter
    def gears(self, gears):
       
        """
        Sets the gear of the bicycle

        Arguments:
        gears(int): the gear value of the bicycle (0-30)

        Returns:
        None

        """
       
        #checks if user input the gear number between 0 and 30
        if (gears > 0 and gears <= 30):
            self._gears = gears

    

    def pedal(self, move_x):

        """
        Moves the x-position of the bicycle
        
        Arguments:
        move_x(int): the x position of the bicycle

        Returns:
        None

        """

        #adds move_x to current x-position
        self._x_pos += move_x

    def brake(self):

        """
        Pass method
        
        Arguments:
        None

        Returns:
        None

        """


        pass

    def change_gears(self, gear):

        """
        Changes the gear value of the bicycle
        
        Arguments:
        gear(int): the gear value to be changed

        Returns:
        None

        """

        #checks if gear value is between 0 and 30
        if(gear > 0 and gear <= 30):
            self.current_gear = gear

    def __str__(self):

        """
        Returns a string of the bicycle's information

        Arguments:
        None

        Returns:
        A string of the bicycle's year, make, model, bicycle type, frame material, and gears

        """

        return (f"Year: {self._year} Make: {self._make} Model: {self._model} "
            f"BicycleType: {self._bicycle_type} FrameMaterial: {self._frame_material} Gears: {self._gears}")

    def __repr__(self):

        """
        Returns a string of the bicycle's information

        Arguments:
        None

        Returns:
        A string of the bicycle's year, make, model

        """

        return(f"Bicycle(Year: {self._year} Make: {self._make} Model: {self._model})")


class Car(Vehicle):

    def __init__(self, make, model, year, car_type, number_doors, engine, x_pos = 0, y_pos = 0):

        """
        Initializes instance of class with attributes

        Arguments:
        make(str): the make of the car
        model(str): the model of the car
        year(int): the year of the car
        car_type(str): the type of car
        number_doors(int): the number of doors on the car
        engine(str): the engine type of the car
        x_pos(int): x-coordinate of vehicle position
        y_pos(int): y-coordinate of vehicle position
        engine_state(int): if the engine is off (0) or on (1)

        Returns:
        None

        """


        #initialize parent class
        super().__init__(make, model, year, x_pos, y_pos)

        #initialize attributes
        self._car_type = car_type
        self._number_doors = number_doors
        self._engine = engine
        self.engine_state = 0

        #checks if engine is v6, v8, or i4
        if(self._engine == "v6" or self._engine == "v8" or self._engine == "i4"):
            self.engine = engine

        #set to "Not Specific" if not any of those engines
        else:
            self._engine = "Not Specified"

    @property
    def car_type(self):

        """
        Returns the type of car

        Arguments:
        None

        Returns:
        A string of the type of car

        """

        return self._car_type
    
    @car_type.setter
    def car_type(self, car_type):

        """
        Sets the car type

        Arguments:
        car_type(str): the type of car (sedan, sport, hatchback, convertible)

        Returns:
        None

        """

        #checks if user input valid car type (sedan, sport, hatchback, convertible)
        if(car_type == "sedan" or car_type == "sport" or car_type == "hatchback" or car_type == "convertible"):
            self._car_type = car_type

    @property
    def number_doors(self):

        """
        Returns the number of doors on the car

        Arguments:
        None

        Returns:
        An integer of the number of doors on the car

        """


        return self._number_doors
    
    @number_doors.setter
    def number_doors(self, number_doors):

        """
        Sets the number of doors on car

        Arguments:
        number_doors(int): the number of doors on car (1-5)

        Returns:
        None

        """

        #checks if number of doors is between 1 and 5
        if(number_doors > 0 and number_doors <= 5):
            self._number_doors = number_doors

    @property
    def engine(self):

        """
        Returns the type of engine in the car

        Arguments:
        None

        Returns:
        A string of the type of engine in car

        """


        return self._engine
    
    @engine.setter
    def engine(self, engine):

        """
        Sets the type of engine in car

        Arguments:
        engine(str): the type of engine in car (i4, v6, v8)

        Returns:
        None

        """

        #checks if inputted engine type is v6, v8, or i4.
        if(engine == "v6" or engine == "v8" or engine == "i4"):
            self._engine = engine

        #If not, sets engine to Not Specific
        else:
            self._engine = "Not Specified"

    def honk(self):

        """
        Returns the string "Honk"

        Arguments:
        None

        Returns:
        A string "Honk!"

        """


        return "Honk!"
    
    def start(self):

        """
        Sets the engine to 1 (Turns it on)

        Arguments:
        None

        Returns:
        None

        """

        #sets engine to 1 to turn it on
        self.engine_state = 1
    
    def stop(self):

        """
        Sets the engine to 0 (Turns it off)

        Arguments:
        None

        Returns:
        None

        """

        #sets engine to 0 to turn it off
        self.engine_state = 0

    def __str__(self):

        """
        Returns a string of the car's information

        Arguments:
        None

        Returns:
        A string of the car's year, make, model, car type, number of doors, and engine type

        """

        return (f"Year: {self._year} Make: {self._make} Model: {self._model} "
            f"CarType: {self._car_type} Doors: {self._number_doors} Engine: {self._engine}")

    def __repr__(self):

        """
        Returns a string of the car's information

        Arguments:
        None

        Returns:
        A string of the car's year, make, model

        """

        return(f"Car(Year: {self._year} Make: {self._make} Model: {self._model})")



# END YOUR CODE
def main():
    vehicle1 = Vehicle("Toyota","Tundra",2022)
    vehicle2 = Vehicle("BMW","328d",2014,5,10)
    vehicle3 = Vehicle("Nissan","Pathfinder",2015,5,10)
    vehicle4 = Vehicle("Toyota","Prius",2011,5,10)
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
    vehicle4.make ="Mazda"
    vehicle4.model = "CX5"
    vehicle4.year = "2021"
    vehicle4.x_pos = 11
    vehicle4.y_pos = 33
    #vehicle4.engine("v10")
    print(vehicle4)
    print(repr(vehicle4))
    bicycle1 = Bicycle("Specialized","Allez", 2023,"road","carbon",12) # you should test wth x and y positions as well
    print(bicycle1)
    bicycle1.make = "Huffy"
    bicycle1.model = "Model II"
    bicycle1.gears = 20
    bicycle1.pedal(3) # x_pos should equal 3 after pedalling. We will change this behavior in subsequent exercises
    bicycle1.brake() # doesn't do anything currently
    bicycle1.change_gears(5) # bicylce.current_gear should equal 5, originally it was 1.
    print(f"Bicycle: {bicycle1}")
    car1 = Car("Ford","Mustang",2019,"sport",2,"v8") # you should test wth x and y positions as well
    print(car1)
    print(f"Engine state a: {car1.engine_state}") # should equal 0
    car1.start()
    print(f"Engine state b: {car1.engine_state}") # should equal 0
    car1.stop()
    print(f"Engine state c: {car1.engine_state}") # should equal 0
    print(car1.honk()) # should equal "Honk!"

if __name__ == "__main__":
    main()
