from dnd import DND_Class
from race import Race
import random
class Trait:

    #Traits and descriptions
    traits = {
        "Strength": "Physical Power",
        "Dexterity": "Agility, reflexes, balance",
        "Constitution": "Endurance and Health",
        "Intelligence": "Knowledge (Book Smart)",
        "Wisdom": "Perception/Insight (Street Smart)",
        "Charisma": "Personality and Social Skills"
    }

    #Bonus points for the race chosen
    race_bonuses = {
        "Dwarf": "+2 Constitution",
        "Elf": "+2 Dexterity",
        "Halfling": "+2 Dexterity",
        "Human": "+1 to all traits",
        "Dragonborn": "+2 Strength, +1 Charisma",
        "Gnome": "+2 Intelligence",
        "Half-Elf": "+2 Charisma, +1 to two other trait choices",
        "Half-Orc": "+2 Strength, +1 Constitution",
        "Tiefling": "+2 Charisma, +1 Intelligence",
    }

    #The primary abilities for the class chosen
    class_primary_abilities = {
        "Barbarian": "Strength",
        "Bard": "Charisma",
        "Cleric": "Wisdom",
        "Druid": "Wisdom",
        "Fighter": "Strength or Dexterity",
        "Monk": "Dexterity & Wisdom",
        "Paladin": "Strength & Charisma",
        "Ranger": "Dexterity & Wisdom",
        "Rogue": "Dexterity",
        "Sorcerer": "Charisma",
        "Warlock": "Charisma",
        "Wizard": "Intelligence"
    }

    #Points for the traits
    abilities_points = {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0,
    }


    def __init__(self, class_name):
        """Attributes for Trait object

        Args:
            class_name (str): name of the class
        
        Returns:
            None

        """
        self.dnd_class = DND_Class(class_name)
        self.primary_ability = None

    
    def roll_dice():
        """Rolls the dice for trait statistics

        Args:
            None
        
        Returns:
            None

        """
        print("We will first start with rolling stats for Strength, then we will do Dexterity, Constitution, Intelligence, Wisdom, and last Charisma")
        for trait in Trait.traits.keys(): #Loop through each trait
            total = 0 #Initialize/Reset total for each loop
            print(f"Rolling stats for {trait}") 


            while total < 10: #Loop once, if dice rolls are less than 10, roll again
                first_dice= random.randint(1,6) #randomly rolling a 6 sided die
                input(f"Lets roll your stats! Press Enter to begin rolling...")
                print(f"Your first roll is: {first_dice}")
                input("Press Enter to do your second roll...")
                second_dice= random.randint(1,6)
                print(f"Your second roll is: {second_dice}")
                input("Press Enter to do your third roll...")
                third_dice = random.randint(1,6)
                print(f"Your third roll is: {third_dice}")
                input("Press Enter to do your fourth roll...")
                fourth_dice = random.randint(1,6)
                print(f"Your last roll is: {fourth_dice}")
                print()

                dice_rolls = [first_dice, second_dice, third_dice, fourth_dice] #put each dice roll in a list

                lowest_roll = min(dice_rolls) #ChatGPT to help with sort, finding the minimum value
                print(f"Your lowest dice roll was {lowest_roll}, we will discard this roll")
                input("Press Enter to continue...")
                print()
                total = sum(dice_rolls) - lowest_roll #the total will be the sum of the 3 largest values
                
                if (total >= 10): #if total is greater than 10:
                    print(f"Great! Your total stat for {trait} is {total}, lets move on to the next trait") 
                    input("Press Enter to continue to move on...")
                    print()
                    Trait.abilities_points[trait] = total #Add the total to the trait

                else: #If dice roll were too low, loop again in while loop
                    print("Your dice rolls were too low, try again to get 10 or over")
                    input("Press Enter to try again...")
                    print()
        
        print("\nYour final points are:") #print final points of all traits
        for trait, points in Trait.abilities_points.items():
            print(f"{trait}: {points}")
        
    def show_traits():
        """Prints the traits and the description of them

        Args:
            None
        
        Returns:
            None

        """
        print("These are the traits: ")
        for trait, definition in Trait.traits.items(): #looping thorugh the traits
            print(f" {trait}: {definition}") #printing the trait and definition
    
    def show_trait_bonuses():
        """Prints the bonuses with the chosen race

        Args:
            None
        
        Returns:
            None

        """

        print("These are the trait bonuses depending on your race: ")
        for trait, bonus_points in Trait.race_bonuses.items(): #looping through trait bonuses
            print(f" {trait}: {bonus_points}") #printing each trait and assigned bonus
    
    def show_primary_abilities():
        """Prints the primary ability with chosen class

        Args:
            None
        
        Returns:
            None

        """
        print("These are the primary abilities depending on your class: ")
        for char_class, primary in Trait.class_primary_abilities.items(): #looping through each class
            print(f" {char_class}: {primary}") #printing the class and primary ability

    def print_class_choice(self,class_choice):
        """Prints the primary ability with chosen class

        Args:
            class_choice (str) : The chosen class of the DnD
        
        Returns:
            primary_ability (str): The primary ability of the class

        """

        #If statments to check user input. Prints out primary ability from user input
        if class_choice == "Barbarian":
            print("You chose Barbarian! Their primary ability is: Strength")
            self.primary_ability = "Strength"
            return self.primary_ability


        if class_choice == "Bard":
            print("You chose Bard! Their primary ability is: Charisma")
            self.primary_ability = "Charisma"
            return self.primary_ability


        if class_choice == "Cleric":
            print("You chose Cleric! Their primary ability is: Wisdom")
            self.primary_ability = "Wisdom"
            return self.primary_ability


        if class_choice == "Druid":
            print("You chose Barbarian! Their primary ability is: Wisdom")
            self.primary_ability = "Wisdom"
            return self.primary_ability

        if class_choice == "Fighter":
            flag = True
            confirm_flag = True
            while flag: #default true
                self.primary_ability = input("You chose Fighter! Please pick if you want your primary ability to be Strength or Dexterity: ").capitalize() #Capitalize
                if self.primary_ability == "Strength" or self.primary_ability == "Dexterity": #If user input Strength or Dexterity:
                    print(f"You chose: {self.primary_ability}.") #print chosen trait
                    while(confirm_flag): #default true
                        confirm = input("Would you like to proceed? (Y/N) ").capitalize()
                        if (confirm == "Y"):
                            return self.primary_ability #return and break out of both loops
                        
                        elif (confirm == "N"): #If user does not confirm, choose again
                            print("Please choose again.")
                            break #break out of inner loop and loops back to beginning
                        else: #If user did not put Y or N, invalid
                            print("Invalid input. Please enter 'Y' or 'N'") #loops back to confirmation page
                else: #If user did not put in one of the abilities, loop again
                    print(f"Invalid primary ability. Please try again!")  #loops back to beginning

        if class_choice == "Monk":
            print("You chose Monk! Their primary ability is: Dexterity & Wisdom")
            self.primary_ability = "Dexterity & Wisdom"
            return self.primary_ability

        if class_choice == "Paladin":
            print("You chose Paladin! Their primary ability is: Strength & Charisma")
            self.primary_ability = "Strength & Charisma"
            return self.primary_ability


        if class_choice == "Ranger":
            print("You chose Ranger! Their primary ability is: Dexterity & Wisdom")
            self.primary_ability = "Dexterity & Wisdom"
            return self.primary_ability


        if class_choice == "Rogue":
            print("You chose Rogue! Their primary ability is: Dexterity")
            self.primary_ability = "Dexterity"
            return self.primary_ability


        if class_choice == "Sorcerer":
            print("You chose Sorcerer! Their primary ability is: Charisma")
            self.primary_ability = "Charisma"
            return self.primary_ability


        if class_choice == "Warlock":
            print("You chose Warlock! Their primary ability is: Charisma")
            self.primary_ability = "Charisma"
            return self.primary_ability


        if class_choice == "Wizard":
            print("You chose Wizard! Their primary ability is: Intelligence")
            self.primary_ability = "Intelligence"
            return self.primary_ability



    def print_race_choice(self, race_choice):
        """Prints the race choice and the bonuses involved

        Args:
            race_choice (str): The race choice of the user
        
        Returns:
            None

        """

        if race_choice == "Dwarf":
            print("You chose Dwarf as your race. You get +2 Constitution bonus points!")
            Trait.abilities_points["Constitution"] += 2 #Add +2 bonus to the Constitution

        if race_choice == "Elf":
            print("You chose Elf as your race. You get +2 Dexterity bonus points!")
            Trait.abilities_points["Dexterity"] += 2 #Add +2 bonus to the Dexterity


        if race_choice == "Halfling":
            print("You chose Halfling as your race. You get +2 Dexterity bonus points!")
            Trait.abilities_points["Dexterity"] += 2 #Add +2 bonus to the Dexterity


        if race_choice == "Human":
            print("You chose Human as your race. You get +1 bonus points to all traits!")
            for trait in Trait.abilities_points:
                Trait.abilities_points[trait] += 1 #Add +1 bonus to the all traits


        if race_choice == "Dragonborn":
            print("You chose Dragonborn as your race. You get +2 Strength & +1 Charisma bonus points!")
            Trait.abilities_points["Strength"] += 2 #Add +2 bonus to the Strength
            Trait.abilities_points["Charisma"] += 1 #Add +1 bonus to the Charisma


        if race_choice == "Gnome":
            print("You chose Gnome as your race. You get +2 Intelligence bonus points!")
            Trait.abilities_points["Intelligence"] += 2 #Add +2 bonus to the Intelligence


        if race_choice.title() == "Half-Elf": #.title because it is hyphened

            print("You chose Half-Elf as your race! You get +2 Charisma points and +1 to any two traits. Please pick two traits to add 1 point to")
            Trait.abilities_points["Charisma"] += 2 #Add +2 bonus to the Charsima


            for trait, definition in Trait.traits.items(): #loop through all the traits and prints them
                print(f" {trait}: {definition}")

            flag_one = True

            while (flag_one): #do-while loop

                confirm_flag_one = True

                #intitalizing first_trait to capitalized first trait
                first_trait = input("Please choose your first trait: ").capitalize()
                
                #validates if inputted trait is actually in the list of traits
                if first_trait in Trait.traits and first_trait != "Charisma": #Ensuring user does not put charisma again
                    print(f"You chose the trait: {first_trait}.")

                    while(confirm_flag_one): #default true
                        confirm = input("Would you like to proceed? (Y/N) ").capitalize() 

                        #If confirm is yes:
                        if confirm == "Y":
                            print(f"Your trait {first_trait} has been selected.") #prints trait
                            Trait.abilities_points[first_trait] += 1 #adds 1 to selected trait
                            confirm_flag_one = False #breaks out of inner loop
                            flag_one = False #breaks out of outer loop


                        elif confirm == "N": #if confirm is no:
                            print("Choose a different trait.") #choose a different trait, loops back to beginning of while loop
                            break #breaks out of inner loop


                        else: #if user did not put Y or N, invalid input
                            print("Invalid Input, Please input either Y or N") #loops back to the confirmation
                
                elif(first_trait.capitalize() == "Charisma"): #if user did put charisma:
                    print("You can not select Charisma, please choose another trait") #loops back to beginning

                else: #If user input was not in list of traits
                    print(f"Your chosen trait: {first_trait}, is not in the list, please pick again") #loops back to beginning
             
            flag_two = True
            while (flag_two):
                confirm_flag_two = True

                #Initializes second_trait to user input
                second_trait = input("Great! Now please choose your second trait: ").capitalize()
                

                if second_trait in Trait.traits and second_trait != "Charisma": #validates if inputted trait is actually in the list of traits & not charisma
                    if second_trait != first_trait: #checks to make sure user didn't select the same trait
                        print(f"You chose the trait: {second_trait}.") 

                        while(confirm_flag_two): #default true
                            confirm = input("Would you like to proceed? (Y/N) ").capitalize()

                            #If confirm is yes:
                            if confirm == "Y":
                                print(f"Your trait {second_trait} has been selected.")  #print trait
                                Trait.abilities_points[second_trait] += 1 #add 1 point to trait
                                confirm_flag_two = False #breaks out of inner loop
                                flag_two = False #breaks out of outer loop

                            #if confirm is no
                            elif confirm == "N":
                                print("Choose a different trait.") #Choose a different trait, loop back to beginning
                                break #breaks out of inner loop
                            
                            #if user did not put Y or N, invalid input
                            else:
                                print("Invalid Input, Please input either Y or N") #loop back to confirmation
                    
                    #if user chose the same trait as the first
                    else:
                        print(f"You chose the same trait as the first trait, please pick another trait") #loop back to beginning
                
                elif(second_trait.capitalize() == "Charisma"):
                    print("You can not select Charisma, please choose another trait") #loops back to beginning

                #If user input an invalid trait
                else:
                    print(f"Your chosen second trait: {second_trait}, is not in the list, please pick again") #loop back to beginning
            
            #Prints two selected trait
            print(f"Fantastic! Your chosen traits for the race Half-Elf is {first_trait} and {second_trait}.")


        if race_choice.title() == "Half-Orc":
            print("You chose Half-Orc as your race. You get +2 Strength & +1 Constitution bonus points!")
            Trait.abilities_points["Strength"] += 2 #Add +2 bonus to Strength
            Trait.abilities_points["Constitution"] += 1 #Add +1 bonus to Constitution

        if race_choice == "Tiefling":
            print("You chose Tiefling as your race. You get +2 Charisma & +1 Intelligence bonus points!")
            Trait.abilities_points["Charisma"] += 2 #Add +2 bonus to Charisma
            Trait.abilities_points["Intelligence"] += 1 #Add +1 bonus to Intelligence