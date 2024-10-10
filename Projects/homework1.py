from collections import defaultdict

"""A template for a python script deliverable for INST326.
Author: Arianna Alimi
Assignment: Homework #1 INST326
Date: 10_03_24
Challenges Encountered: The float variables printing out unwanted decimals, collecting items and adding the quantity,
reading the file and ensuring the strip and adding to collect item.
"""
# YOUR CODE HERE
class Robot:

    def __init__(self, robot_id, battery, motor, x_pos = 0, y_pos = 0):

        """
        Initializes instance of class with attributes and sets attributes to values

        Arguments:
        robot_id (str) : the robots id 
        battery (str) : the battery type of the robot
        motor (str) : the motor the robot uses
        x_pos (int) : x position of the robot
        y_pos (int) : y position of the robot
        items (defaultdict) : dictionary that holds robots items
        battery_level (float) : the amount of battery the robot has


        Returns:
        None

        """

        #Initialization of attributes
        self.robot_id = robot_id
        self.battery = battery
        self.motor = motor
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        #Verifying motor is either brushed_dc or burshless_dc
        if(motor != "brushed_dc" or motor != "brushless_dc"):
            print("Invalid Motor Input")

        #Sets the battery level to a value based on the battery
        if(battery == "lithium_ion"):
            self.battery_level = float(100)
        elif(battery == "nickel_metal_hydride"):
            self.battery_level = float(100)
        elif(battery == "lithium_polymer"):
            self.battery_level = float(100)
        elif(battery == "nuclear"):
            self.battery_level = float(10000)
        else:
            self.battery = None
            self.battery_level = float(0)

        #items dictionary
        self.items = defaultdict(int)

    def move_forward(self):

        """

        Moves the robot forward if battery level is greater than 0 by adding 1 to the y position

        Arguments:
        None

        Returns:
        None

        """
        #if there is battery left, decrease battery level and increase y position
        if(self.battery_level > 0):
            self.battery_level -= 1.0
            self.y_pos += 1
    
    def move_backward(self):

        """

        Moves the robot backward if battery level is greater than 0 by subtracting 1 to the y position

        Arguments:
        None

        Returns:
        None

        """

        #if there is battery left, decrease battery level and decrease y position
        if(self.battery_level > 0):
            self.battery_level -= 1.0
            self.y_pos -= 1
    
    def move_right(self):

        """

        Moves the robot to the right if battery level is greater than 0 by adding 1 to the x position

        Arguments:
        None

        Returns:
        None

        """

        #if there is battery left, decrease battery level and increase x position
        if(self.battery_level > 0):
            self.battery_level -= 1.0
            self.x_pos += 1
    
    def move_left(self):

        """

        Moves the robot to the left if battery level is greater than 0 by subtracting 1 to the x position

        Arguments:
        None

        Returns:
        None

        """


        #if there is battery left, decrease battery level and decrease x position
        if(self.battery_level > 0):
            self.battery_level -= 1.0
            self.x_pos -= 1

    def get_battery_level(self):
        """

        Returns the battery level of the robot


        Arguments:
        None

        Returns:
        the battery level as a float

        """
        #returns the battery level of the robot
        return float(self.battery_level)
    
    def reset_position(self):
        """

        Sets the x and y position to 0 to reset the position of the robot

        Arguments:
        None

        Returns:
        None

        """
        #sets x and y position to 0 to reset the position
        self.x_pos = 0
        self.y_pos = 0

    def charge_battery(self, amount):
        """

        Recharges the battery of the robot by adding the amount to battery level and checks to ensure
        it is not fully charged 


        Arguments:
        amount (float) : the number that you want to add to the robot's battery level

        Returns:
        None

        """

        #sets amount to float
        amount = float(amount)

        #If battery max is 100
        if(self.battery == "lithium_ion" or self.battery == "nickel_metal_hydride" or self.battery == "lithium_polymer"):
            if((self.battery_level + amount) <= 100.0): #if when adding amount it is less than max amount
                self.battery_level += amount #add the amount

        #if battery max is 10000
        elif(self.battery == "nuclear"):
            if((self.battery_level + amount) <= 10000.0): #if when adding amount it is less than max amount
                self.battery_level += amount #add the amount
    
    def get_position(self):
       """

        Returns the x and y position as a tuple


        Arguments:
        None

        Returns:
        A tuple of the x and y position

        """

       positionTuple =  self.x_pos, self.y_pos #create tuple attribute with x and y position
       return positionTuple

    def collect_item(self, item, num_items = 1):

        """

        Adds items to the dictionary by incrementing amount if already in dictionary or 
        adding a new item


        Arguments:
        item (str) : the item wanting to add
        num_items (int): the quanitity of the item

        Returns:
        None

        """

        if item in self.items: #ChatGPT to help
            self.items[item] += num_items #add the quantity of the item if it is already in dictionary
        else:
            self.items[item] = num_items #add the item to the dictionary

    def drop_item(self, item):

        """

        Decrease the quantity of the item if it is more than 1 or deletes the item if 1


        Arguments:
        item (str) : item wanting to drop

        Returns:
        None

        """
        #if the item is already in the dictionary
        if item in self.items:

            #if the item is more than 1
            if self.items[item] > 1:
                #decrease the quantity of the item by 1
                self.items[item] -= 1
            
            #if the item is not more than 1
            else:
                #delete the item from the dictionary
                del self.items[item]

    def read_file(self, filename):

        """
        Reads a file in and adds the item to the items dictionary


        Arguments:
        filename (str) : the file name to read in

        Returns:
        Returns a FileNotFoundError exception if file name is not found

        """


        try:
            with open(filename, 'r') as f:
                for line in f: #looping through each line of the file
                    item, num_items = line.strip().split(':') #ChatGPT to help with strip
                    self.collect_item(item, int(num_items)) #call collect_item method to add file items
        except FileNotFoundError: #throw exception if file was not found
            return f"File {filename} does not exist"

    def print_items(self):

        """
        Prints the items that the robot contains

        Arguments:
        None

        Returns:
        None

        """

        for item in self.items: #loops through items in dictionary
            print(f"{self.items[item]} {item}") #ChatGPT to help print

    
    def __str__(self):

        """
        String method that returns the robot's id and charge level


        Arguments:
        None

        Returns:
        Returns string with robot id and charge level

        """

        return f"Robot_id: {self.robot_id} charge level: {self.battery_level}"
    
    def __repr__(self):

        """
        Returns a string of the robot object

        Arguments:
        None

        Returns:
        Returns string of the robot's id, battery, battery level, motor, x position, and y position

        """

        return f"Robot_id: {self.robot_id} battery: {self.battery} battery level: {self.battery_level} motor: {self.motor} x_pos: {self.x_pos} y_pos: {self.y_pos}"



# END OF YOUR CODE (but feel free to add to main() in order to run more tests)
def main():
# Note, the following is not what I have in the unit tests. I have different values.
# This code should cover most of the cases that you are required to test.
    robot1 = Robot("123ABX", "lithium_ion", "brushless_dc",0,0)
    print(robot1)
    print(repr(robot1))
    robot1.collect_item("green block")
    robot1.collect_item("green block")
    robot1.collect_item("red block")
    robot1.collect_item("red block")
    robot1.collect_item("red block")
    robot1.print_items()
    robot1.drop_item("green block")
    print("---------")
    robot1.print_items()
    robot1.move_forward()
    robot1.move_left()
    robot1.move_left()
    robot1.move_left()
    robot1.move_forward()
    print(robot1)
    robot1.charge_battery(5)
    for i in range(0,50):
        robot1.move_forward()
    print(repr(robot1))
    robot1.charge_battery(7)
    print(repr(robot1))
    robot1.reset_position()
    print(repr(robot1))
    robot1.charge_battery(50)
    print(repr(robot1))
    robot1.read_file("items.txt")
    robot1.print_items()
if __name__ == "__main__":
    main()
