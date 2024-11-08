"""A template for a python script deliverable for INST326.
Driver: Arianna Alimi
Navigator: None
Assignment: Exercise 6
Date: 11_7_24
Challenges Encountered: Argument Parsers
"""
import argparse

class Calculator:
    def add(self, x, y):

        """
        Returns sum of two values

        Arguments:
        x(float): first float value
        y(float): second float value

        Returns:
        sum of x and y

        """

        return x + y
    
    def subtract(self, x,y):

        """
        Returns difference of two values

        Arguments:
        x(float): first float value
        y(float): second float value

        Returns:
        difference of x and y

        """

        return x - y
    
    def multiply(self, x,y):

        """
        Returns product of two values

        Arguments:
        x(float): first float value
        y(float): second float value

        Returns:
        product of x and y

        """

        return x * y
    
    def divide(self, x,y):

        """
        Returns quotient of two values

        Arguments:
        x(float): first float value
        y(float): second float value

        Returns:
        quotient of x and y

        """

        try:
            return x / y
        except ZeroDivisionError: #raises value error if division by 0 is found
            raise ValueError

def main():

    #parser set up
    parser = argparse.ArgumentParser(
        description = 'Helps calculate values'
    )

    #adds call, x, and y arguments
    parser.add_argument('call', choices =['add', 'subtract', 'multiply', 'divide']) #ChatGPT to help with choices
    parser.add_argument('x', type = float)
    parser.add_argument('y', type = float)

    args = parser.parse_args()

    #initializes calculator class
    calc = Calculator()

    
    try:
        if args.call == "add":
            result = calc.add(args.x, args.y)
        elif args.call == "subtract":
            result = calc.subtract(args.x, args.y)
        elif args.call == "multiply":
            result = calc.multiply(args.x, args.y)
        elif args.call == "divide":
            result = calc.divide(args.x, args.y)
        print(result)

    except ValueError:
        print("Error")


if __name__ == "__main__":
    main()
