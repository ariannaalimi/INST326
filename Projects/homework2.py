"""A template for a python script deliverable for INST326.
Author: Arianna Alimi
Assignment: Homework #2 INST326
Date: 11_19_24
Challenges Encountered: Argument Parsers and List of Items
"""
from abc import ABC, abstractmethod
from argparse import ArgumentParser
import sys
import random
import string
# string.ascii_letters


# YOUR CODE HERE
class Battery():
# Class variable, you are not required to use this. I found it helpful
    battery_rules ={"nuclear":10000,"lithium_ion":200,"lithium_polymer":175,"nickel_hydride":150,"lead_acid":100}
    def __init__(self, battery_id, battery_type):
        """
        Initializes instance of class with attributes and sets attributes to values

        Arguments:
        battery_id (str): the unique id for the battery
        battery_type (str): the type of battery used
        battety_type_flag (bool): flags if the correct input for battery type
        battery_level (float): the amount of battery 


        Returns:
        None

        """
        self._battery_id = battery_id
        battery_type_flag = True #default battery flag as true
        
        if battery_type in ["lithium_ion", "lithium_polymer", "nickel_hydride", "lead_acid", "nuclear"]:
            self._battery_type = battery_type #sets battery type only if correct input
        else:
            self._battery_type = None
            battery_type_flag = False #if not correct input, sets battery type flag to false
        
        if(battery_type_flag):
            self._battery_level = (0.0) #if flag is true, set battery level to 0
        else:
            self._battery_level = None #if flag is false (not correct battery type), sets battery level to None



    def charge_battery(self, amount):
        """
        Charges the battery by the amount

        Arguments:
        amount (float): amount to charge battery by


        Returns:
        None

        """

        amount = float(amount)

        if(self._battery_type == "lithium_ion"):
            if((self._battery_level + amount) <= 200.0): #if when adding amount it is less than max amount
                self._battery_level += amount #add the amount
            else:
                self._battery_level == 200.0 #if else, max out the battery
        
        elif(self._battery_type == "lithium_polymer"):
            if((self._battery_level + amount) <= 175.0): #if when adding amount it is less than max amount
                self._battery_level += amount #add the amount
            else:
                self._battery_level == 175.0 #if else, max out the battery

        elif(self._battery_type == "nickel_hydride"):
            if((self._battery_level + amount) <= 150.0): #if when adding amount it is less than max amount
                self._battery_level += amount #add the amount
            else:
                self._battery_level == 150.0 #if else, max out the battery

        elif(self._battery_type == "lead_acid"):
            if((self._battery_level + amount) <= 100.0): #if when adding amount it is less than max amount
                self._battery_level += amount #add the amount
            else:
                self._battery_level == 100.0 #if else, max out the battery

        elif(self._battery_type == "nuclear"):
            if((self._battery_level + amount) <= 10000.0): #if when adding amount it is less than max amount
                self._battery_level += amount #add the amount
            else:
                self._battery_level == 10000.0 #if else, max out the battery
    
    #From template
    def consume_battery(self, amount):

        """
        Method to use the battery level

        Arguments:
        amount (float): amount of battery to use


        Returns:
        None

        """


        if (self._battery_level - amount) <= 0: #can't be a negative, if negative sets to 0
            self._battery_level = 0
        else:
            self._battery_level -= amount #else, subtract the amount
    
    @property
    def battery_id(self):
        """
        Returns the battery id

        Arguments:
        None

        Returns:
        self._battery_id(str)

        """

        return self._battery_id
    
    @battery_id.setter
    def battery_id(self, battery_id):
        """
        Sets the battery id

        Arguments:
        battery_id(str)

        Returns:
        None

        """

        self._battery_id = battery_id
    
    @property
    def battery_type(self):
        """
        Returns the battery type

        Arguments:
        None

        Returns:
        self._battery_type(str)

        """
        return self._battery_type
    
    @battery_type.setter
    def battery_type(self, battery_type):
        """
        Sets the battery type

        Arguments:
        battery_type(str)

        Returns:
        None

        """
        self._battery_type = battery_type
    
    @property
    def battery_level(self):
        """
        Returns the battery level

        Arguments:
        None

        Returns:
        self._battery_level(float)

        """
        return self._battery_level
    
    @battery_level.setter
    def battery_level(self, battery_level):
        """
        Sets the battery level

        Arguments:
        battery_level(float)

        Returns:
        None

        """
        self._battery_level = battery_level

    def __str__(self):

        """
        Returns a string containing the battery information

        Arguments:
        None

        Returns:
        String contianing the battery id, battery type, and battery_level

        """
        return f"battery_id ( {self._battery_id} ) battery_type ( {self._battery_type} ) battery_level ( {self._battery_level} )"
    

'''----- MOTOR'''
class Motor():
    motor_types = ["dc_motor","stepper_motor","servo_motor"]
    
    def __init__(self, motor_id, motor_type, current_rating, speed):
        """
        Initializes instance of class with attributes and sets attributes to values

        Arguments:
        motor_id (str): unique string of the motor
        motor_type (str): string of the type of motor
        current_rating (float): the rating of the type of motor
        speed (int): the speed of the motor
        state(int): the state the motor is in (on = 1, off = 0)

        Returns:
        None

        """

        self._motor_id = motor_id

        if motor_type in ["dc_motor", "stepper_motor", "servo_motor"]:
            self._motor_type = motor_type #initializes attribute if correct motor type was inputted
        
        if (current_rating > 0 and current_rating <= 5):
            self._current_rating = current_rating #initializes attribute if input is between 1 and 5

        if (speed > 0 and speed <= 8): 
            self._speed = speed #initializes attribute if input is between 1 and 8
     
        self._state = 0 #default set the state to 0


    def start_motor(self):
        """
        Method to start the motor

        Arguments:
        None

        Returns:
        None

        """

        self._state = 1

    def stop_motor(self):
        """
        Method to stop the motor

        Arguments:
        None

        Returns:
        None

        """

        self._state = 0


    def step_consumption_cost(self):
        """
        Method that contains the amount of energy to move for each motor

        Arguments:
        None

        Returns:
        If "dc_motor", returns 3
        If "stepper_motor", returns 2
        If "servo_motor", returns 1
        else, returns 0

        """

        match self._motor_type:
            case "dc_motor":
                return 3
            case "stepper_motor":
                return 2
            case "servo_motor":
                return 1
            case _:
                print("No motor type set!")
                return 0
            
    @property
    def motor_id(self):
        """
        Returns the motor id

        Arguments:
        None

        Returns:
        self._motor_id(str)

        """
        return self._motor_id
    
    @motor_id.setter
    def motor_id(self, motor_id):
        """
        Sets the motor id

        Arguments:
        motor_id(str)

        Returns:
        None

        """
        self._motor_id = motor_id

    @property
    def motor_type(self):
        """
        Returns the motor type

        Arguments:
        None

        Returns:
        self._motor_type(str)

        """
        return self._motor_type
    
    @motor_type.setter
    def motor_type(self, motor_type):
        """
        Sets the motor type

        Arguments:
        motor_type(str)

        Returns:
        None

        """
        self._motor_type = motor_type
    
    @property
    def current_rating(self):
        """
        Returns the current rating

        Arguments:
        None

        Returns:
        self._current_rating(float)

        """
        return self._current_rating
    
    @current_rating.setter
    def current_rating(self, current_rating):
        """
        Sets the current rating

        Arguments:
        current_rating(float)

        Returns:
        None

        """
        self._current_rating = current_rating
    
    @property
    def speed(self):
        """
        Returns the speed

        Arguments:
        None

        Returns:
        self._speed(int)

        """
        return self._speed
    
    @speed.setter
    def speed(self, speed):
        """
        Sets the speed of the motor

        Arguments:
        speed(int)

        Returns:
        None

        """
        self._speed = speed
    
    @property
    def state(self):
        """
        Returns the state of the motor

        Arguments:
        None

        Returns:
        self._state(int)

        """
        return self._state
    
    @state.setter
    def state(self, state):
        """
        Sets the state of the motor

        Arguments:
        state(int)

        Returns:
        None

        """
        self._state = state
    

    def __str__(self):
        """
        Returns a string containing the motor information

        Arguments:
        None

        Returns:
        String contianing the motor id, motor type, current rating, speed, and state

        """
        return f"motor_id ( {self._motor_id} ) motor_type ( {self._motor_type} ) current_rating ( {self._current_rating} ) speed ( {self._speed} ) state ( {self._state})"
    

'''----- ITEM
'''

class Item():
    # Types: ["cube","cylinder","cone","sphere","pyramid"]
    def __init__(self, item_type, color):
        """
        Initializes instance of class with attributes and sets attributes to values

        Arguments:
        item_type (str): a string of the type of item
        color (str): the color of the item

        Returns:
        None

        """
        
        if item_type in ["cube","cylinder","cone","sphere","pyramid"]:
            self._item_type = item_type #initializes if item type is one of the specific types
        else:
            self._item_type = None #else, sets to none
        
        self._color = color

    @property
    def item_type(self):
        """
        Returns the item type

        Arguments:
        None

        Returns:
        self._item_type(str)

        """
        return self._item_type
    
    @item_type.setter
    def item_type(self, item_type):
        """
        Sets the item type

        Arguments:
        item_type(str)

        Returns:
        None

        """

        self._item_type = item_type
    
    @property
    def color(self):
        """
        Returns the color of the item

        Arguments:
        None

        Returns:
        self._color(str)

        """
        return self._color
    
    @color.setter
    def color(self, color):
        """
        Sets the color of the item

        Arguments:
        color(str)

        Returns:
        None

        """
        self._color = color


    def __str__(self):
        """
        Returns a string containing the item information

        Arguments:
        None

        Returns:
        String contianing the color and item type

        """
        return f"{self._color} {self._item_type}"
    

'''
----- ROBOT
'''
class Robot(ABC):
    
    def __init__(self, robot_id, battery, motor, x_pos = 0, y_pos = 0):
        """
        Initializes instance of class with attributes and sets attributes to values

        Arguments:
        robot_id (str): unique string of the robot id
        battery (Battery): type of battery for the Robot
        motor (Motor): type of motor for the Robot
        x_pos (int): x position of the robot
        y_pos (int): y position of the robot
        items (list): item objects that are collected

        Returns:
        None

        """
        
        # YOUR CODE. I included _items since I changed it to be a list versus a dictionary

        self._robot_id = robot_id
        self._battery = battery
        self._motor = motor
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._items = []


        # YOUR CODE - 4 move methods
        #Remember what we had to do for the Vehicle and checking fuel level one step at a time

    def move_forward(self, amount):
        """
        Moves the robot forward by adding to the y position

        Arguments:
        amount(int): the amount to move the robot

        Returns:
        None

        """
        for i in range(amount): #loops through the amount to move
            if self._battery.battery_level > 0: #checks to ensure battery level is above 0           
                self._y_pos += 1 #moves y position to move forward
                self._battery.consume_battery(self.motor.step_consumption_cost()) #consumes battery depending on type of motor
            else:
                self._battery.battery_level = 0.0 #if battery level is 0 or below, sets to 0.0
            
    def move_backward(self, amount):
        """
        Moves the robot backwards by subtracting to the y position

        Arguments:
        amount(int): the amount to move the robot

        Returns:
        None

        """

        for i in range(amount): #loops through the amount to move
            if self._battery.battery_level > 0: #checks to ensure battery level is above 0               
                self._y_pos -= 1 #moves y position to move backwards
                self._battery.consume_battery(self.motor.step_consumption_cost()) #consumes battery depending on type of motor
            else:
                self._battery.battery_level = 0.0 #if battery level is 0 or below, sets to 0.0
    
    def move_right(self, amount):
        """
        Moves the robot right by adding to the x position

        Arguments:
        amount(int): the amount to move the robot

        Returns:
        None

        """

        for i in range(amount): #loops through the amount to move
            if self._battery.battery_level > 0: #checks to ensure battery level is above 0                 
                self._x_pos += 1 #moves x position to move right
                self._battery.consume_battery(self.motor.step_consumption_cost()) #consumes battery depending on type of motor
            else:
                self._battery.battery_level = 0.0 #if battery level is 0 or below, sets to 0.0

    def move_left(self, amount):
        """
        Moves the robot left by subtracting to the x position

        Arguments:
        amount(int): the amount to move the robot

        Returns:
        None

        """

        for i in range(amount): #loops through the amount to move
            if self._battery.battery_level > 0: #checks to ensure battery level is above 0               
                self._x_pos -= 1 #moves x position to move left
                self._battery.consume_battery(self.motor.step_consumption_cost()) #consumes battery depending on type of motor
            else:
                self._battery.battery_level = 0.0 #if battery level is 0 or below, sets to 0.0

        
        # YOUR CODE - abstract methods collect_item, drop_item and print_items

    @abstractmethod
    def collect_item(self, item):
        """
        Collects the item objects

        Arguments:
        item (Item): the item to be collected

        Returns:
        None

        """
        pass
    
    @abstractmethod
    def drop_item(self, color, item_type):
        """
        Removes the item objects

        Arguments:
        color(str): the color of the object to removed
        item_type(str): the type of the item to be removed

        Returns:
        None

        """

        pass 


    @abstractmethod
    def print_items(self):
        """
        Prints the items in the items list

        Arguments:
        None

        Returns:
        None

        """
        
        pass


    def get_position(self):
        """
        Prints the x and y position of the robot

        Arguments:
        None

        Returns:
        Returns the x position and y position as a tuple

        """

        #print(f"({self._x_pos}, {self._y_pos})")
        return (self._x_pos, self._y_pos)


    def charge_battery(self,amount):
        """
        Charges the robot's battery by the amount attribute

        Arguments:
        amount (float): amount to charge battery by

        Returns:
        None

        """

        self._battery.charge_battery(amount)


    def get_battery_level(self):
        """
        Prints the battery level of the robot

        Arguments:
        None

        Returns:
        self._battery.battery_level(float)

        """

        #print(f"The {self._battery} battery is charged to {self._battery_level}")
        return self._battery.battery_level
    def reset_position(self):
        """
        Resets the position of the robot

        Arguments:
        None

        Returns:
        None

        """
        #sets x and y position to 0
        self._x_pos = 0
        self._y_pos = 0
    
    # YOUR CODE - setters and getters

    @property
    def robot_id(self):
        """
        Returns the robot id

        Arguments:
        None

        Returns:
        self._robot_id(str)

        """
        return self._robot_id
    
    @robot_id.setter
    def robot_id(self, robot_id):
        """
        Sets the robot id

        Arguments:
        robot_id(str)

        Returns:
        None

        """
        self._robot_id = robot_id
    
    @property
    def battery(self):
        """
        Returns the battery of the robot

        Arguments:
        None

        Returns:
        self._battery(Battery)

        """
        return self._battery
    
    @battery.setter
    def battery(self, battery):
        """
        Sets the battery of the robot

        Arguments:
        battery(Battery)

        Returns:
        None

        """
        self._battery = battery
    
    @property
    def motor(self):
        """
        Returns the motor of the robot

        Arguments:
        None

        Returns:
        self._motor(Motor)

        """

        return self._motor
    
    @motor.setter
    def motor(self, motor):
        """
        Sets the battery of the robot

        Arguments:
        battery(Battery)

        Returns:
        None

        """

        self._motor = motor
    
    @property
    def x_pos(self):
        """
        Returns the x position of the robot

        Arguments:
        None

        Returns:
        self._x_pos(int)

        """

        return self._x_pos
    
    @x_pos.setter
    def x_pos(self, x_pos):
        """
        Sets the x position of the robot

        Arguments:
        x_pos(int)

        Returns:
        None

        """

        self._x_pos = x_pos
    
    @property
    def y_pos(self):
        """
        Returns the y position of the robot

        Arguments:
        None

        Returns:
        self._y_pos(int)

        """
        return self._y_pos
    
    @y_pos.setter
    def y_pos(self, y_pos):
        """
        Sets the y position of the robot

        Arguments:
        y_pos(int)

        Returns:
        None

        """

        self._y_pos = y_pos

    @property
    def items(self):
        """
        Returns the item objects collected

        Arguments:
        None

        Returns:
        self._items(list)

        """

        return self._items
    
    @items.setter
    def items(self, items):
        """
        Sets the list of items

        Arguments:
        items(list)

        Returns:
        None

        """

        self._items = items

    def __str__(self):
        """
        Returns a string containing the robot's information

        Arguments:
        None

        Returns:
        Return string containing the robot id, battery, motor, x position, and y position

        """

        return f"Robot_id: {self._robot_id} \n\tbattery: {self._battery} \n\tmotor: {self._motor}" \
       f" \n\tx_pos: {self._x_pos} y_pos: {self._y_pos}"

    
    def __repr__(self):
        """
        Returns a string containing the robot's information

        Arguments:
        None

        Returns:
        Return string containing the robot id, battery, motor, x position, and y position

        """

        return (f"Robot_id: {self._robot_id} \n\tbattery: {self._battery} \n\tmotor: {self._motor}"
        f" \n\tx_pos: {self._x_pos} y_pos: {self._y_pos}")


class ServiceRobot(Robot):
    def __init__(self, robot_id, battery, motor, x_pos = 0, y_pos = 0):
        """
        Initializes the parent class

        Arguments:
        robot_id (str): unique string of the robot id
        battery (Battery): type of battery for the Robot
        motor (Motor): type of motor for the Robot
        x_pos (int): x position of the robot
        y_pos (int): y position of the robot
        items (list): item objects that are collected

        Returns:
        None

        """

        # YOUR CODE - initialize parent (super)
        super().__init__(robot_id, battery, motor, x_pos, y_pos)


    def collect_item(self,item):
        """
        Collects the item objects

        Arguments:
        item (Item): the item to be collected

        Returns:
        None

        """

        self._items.append(item)

    def drop_item(self,color, item_type):
        """
        Removes the item objects

        Arguments:
        color(str): the color of the object to removed
        item_type(str): the type of the item to be removed

        Returns:
        None

        """

        print("List size before drop:",len(self._items))
        # YOUR CODE -- drop an item from the list that matches the color and item_type

        for item in self._items:
            if item.color == color and item.item_type == item_type:
                self._items.remove(item)
        print("List size after drop:",len(self._items))

    def print_items(self):
        """
        Prints the items in the items list

        Arguments:
        None

        Returns:
        None

        """

        for k in self._items:
            print(f"{k}")

    def __str__(self):

        """
        Returns a string containing the robot's information

        Arguments:
        None

        Returns:
        Return a string of the robot id, batter, motor, x position and y position

        """
        return f"Robot_id: {self._robot_id} \n\tbattery: {self._battery} \n\tmotor: {self._motor}" \
       f" \n\tx_pos: {self._x_pos} y_pos: {self._y_pos}"

    
def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as
    arguments
    Args:
    args_list (list) : the list of strings from the command prompt
    Returns:
    args (ArgumentParser)
    """
    # YOUR CODE HERE
    # parse and validate arguments


    parser = ArgumentParser(description = "Parsing and Validating arguments")

    parser.add_argument('--numservicerobots', type = int, default = 0)

    #Uncomment the following after you write the above code
    args = parser.parse_args(args_list)
    if args.numservicerobots <= 0:
        raise ValueError("numservicerobots must be greater than 0")
    return args


def main(numservicerobots):
    # Note, the following is not what I have in the unit tests. I have different values.
    # This code should cover most of the cases that you are required to test; however,
    # you may see a few additional test cases.
    battery1 = Battery("1234abyz","lithium_ion")
    motor1 = Motor("M1A2B","servo_motor",3,4)
    servicerobot1 = ServiceRobot("123ABX", battery1, motor1,0,0)
    print(servicerobot1)
    print(repr(servicerobot1))
    item1 = Item("cylinder","blue")
    servicerobot1.collect_item(item1)
    print("----********----")
    random.seed(5)

    myrobotlist = []
    for x in range(0, numservicerobots):
        # TODO randomly choose battery and motor parameters
        batteryrulekeys = list(Battery.battery_rules.keys())
        rbatindex = random.randint(0,(len(batteryrulekeys)-1))
        print("----rbatindex----",rbatindex)
        batterytype1 = batteryrulekeys[rbatindex]
        print("----batterytype1----",batterytype1)
        randlet1 = random.choice(string.ascii_letters)
        randlet2 = random.choice(string.ascii_letters)
        randnum1 = random.randint(0,9)
        randnum2 = random.randint(0,9)
        batteryid1 = randlet1 + randlet2 + str(randnum1) + str(randnum2)
        battery1 = Battery(batteryid1,batterytype1)
        randlet1 = random.choice(string.ascii_letters)
        randlet2 = random.choice(string.ascii_letters)
        randlet3 = random.choice(string.ascii_letters)
        randnum1 = random.randint(0,9)
        randnum2 = random.randint(0,9)
        randnum3 = random.randint(0,9)
        motorid1 = randlet1 + randlet2 + str(randnum1) + str(randnum2) + randlet3 + str(randnum3)
        mtypeindex = random.randint(0,(len(Motor.motor_types)-1))
        motortype = Motor.motor_types[mtypeindex]

        motor1 = Motor(motorid1,motortype,3,4)

        randlet1 = random.choice(string.ascii_letters)
        randlet2 = random.choice(string.ascii_letters)
        randlet3 = random.choice(string.ascii_letters)
        randlet4 = random.choice(string.ascii_letters)
        randnum1 = random.randint(0,9)
        randnum2 = random.randint(0,9)
        randnum3 = random.randint(0,9)
        randnum4 = random.randint(0,9)
        robotid1 = randlet1 + randlet2 + str(randnum1) + str(randnum2) + randlet3 + str(randnum3)+ randlet4 + str(randnum4)
        service_robot = ServiceRobot(robotid1, battery1, motor1,0,0)
        myrobotlist.append(service_robot)
        print(service_robot)

    print("----LENGTH OF THE ROBOT LIST----")
    print(len(myrobotlist))

    item1 = Item("cone","blue")
    item2 = Item("cone","blue")
    item3 = Item("cube","green")

    myrobotlist[0].collect_item(item1)
    myrobotlist[0].collect_item(item2)
    myrobotlist[0].collect_item(item3)

    print(myrobotlist[0])
    print(myrobotlist[0].print_items())
    myrobotlist[0].drop_item("blue","cone")
    myrobotlist[0].drop_item("yellow","cone")

    myrobotlist[0].move_forward(5)
    # Should not have moved because we did not charge it yet
    assert myrobotlist[0].x_pos == 0.0, ("Robot moved but we did not charge it yet")
    myrobotlist[0].charge_battery(100)
    myrobotlist[0].move_forward(5)
    myrobotlist[0].move_right(4)
    myrobotlist[0].move_backward(2)
    myrobotlist[0].move_left(2)
    print(myrobotlist[0])
    myrobotlist[0].move_forward(500)
    print(myrobotlist[0])
if __name__ == "__main__":
    try:
        arguments = parse_args(sys.argv[1:])
        main(arguments.numservicerobots)
    except ValueError as e:
        #sys.exit(str(e))
        main(1) # This is a 'hack' to be able to run it from within VisualStudio
