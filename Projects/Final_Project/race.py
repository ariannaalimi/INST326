class Race:
    """The user is shown the races and types regarding specific races and chooses the race

    Returns:
        race_choice: the race the user chose
    """
    
    races = {
        "Dwarf": "Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal",
        "Elf": "Magical people of otherworldly grace, living in the world but not entirely part of it", 
        "Halfling": "Falflings live out their days in remote agricultural communities, others form nomadic bands that travel constantly, lured by the open road and the wide horizon to discover the wonders of new lands and peoples",
        "Human": "Found throughout the multiverse, humans are as varied as they are numerous, and they endeavor to achieve as much as they can in the years they are given",
        "Dragonborn": "The dragonborn walk proudly through a world that greets them with fearful incomprehension. Shaped by draconic gods or the dragons themselves, dragonborn originally hatched from dragon eggs as a unique race, combining the best attributes of dragons and humanoids ",
        "Gnome": "Gonmes are magical folk created by gods of invention, illusions, and life underground",
        "Half-Elf": "Half-elves combine what some say are the best qualities of their elf and human parents: human curiosity, inventiveness, and ambition tempered by the refined senses, love of nature, and artistic tastes of the elves",
        "Half-Orc": "Some half-ores rise to become proud chiefs of orc tribes, their human blood giving them an edge over their full-blooded orc rivals. Some venture into the world to prove their worth among humans and other more civilized races, Many of these become adventurers, achieving greatness for their mighty deeds and notoriety for their barbaric customs. and savage fury",
        "Tiefling": "To be greeted with stares and whispers, to suffer violence and insult on the street, to see mistrust and fear in every eye: this is the lot of the ticfling"
    }

    dwarf_types = {
        "Hill dwarf": "As a hill dwarf, you have keen senses, deep intuition, and remarkable resilience",
        "Mountain dwarf": "As a mountain dwarf, you're strong and hardy, accustomed to a difficult life in rugged terrain. You're probably on the tall side (for a dwarf), and tend toward lighter coloration"
    }

    elf_types = {
        "High elf": "As a high elf, you haye a keen mind and a mastery of at least the basics of magic",
        "Wood elf": "As a wood elf, you have keen senses and intuition, and your fleet feet carry you quickly and stealthily through your native forests",
        "Dark elf": "Descended from an earlier subrace of dark-skinned elves, the drow were banished from the surface world for following the gaddess Lolth down the path to evil and corruption"
    }

    halfling_types = {
        "Lightfoot": "As a lightfoot halfling, you can easily hide from notice, even using other people as cover. You're inclined to be affable and get along well with others. Lightfoots are more prone to wanderlust than other halflings, and often dwell alongside other races or take up a nomadic life",
        "Stout": "As a stout halfling, you're hardier than average and have some resistance to poison. Some say that stouts have dwarven blood, " 
    }

    def __init__(self, race_choice):
        """Attributes for Race object

        Args:
            race_choice (str): _race choice

        """
        self.race_choice = race_choice

    @classmethod
    def show_races(cls):
        """Shows races to users
        """
        print("These are the races: ")
        for race, description in cls.races.items():
            print(f"- {race}: {description}")

    def show_type(self):
        """If the character's race is a dwarf, elf, or halfling, 
        the user can look at the types regarding which race they chose
        """
        if (self.race_choice == "Dwarf"):
            print("These are the types: ")
            for type, description in Race.dwarf_types.items():
                print(f"- {type}: {description}")

        elif (self.race_choice == "Elf"):
            print("These are the types: ")
            for type, description in Race.elf_types.items():
                print(f"- {type}: {description}")

        elif (self.race_choice == "Halfling"):
            print("These are the types: ")
            for type, description in Race.halfling_types.items():
                print(f"- {type}: {description}")
        else:
            print("No types available for this race.") #if the user selected something else, show that that race has no types

    def choose(self):
        """User chooses race
        """
        self.show_races()

        while True:
            self.race_choice = input("Choose a race: ").capitalize()

            if self.race_choice in Race.races: #validates the race
                print(f"You chose: {self.race_choice}.")
                confirm = input("Would you like to proceed? (Y/N) ").capitalize()
                if confirm == "Y":
                    break
                elif confirm == "N":
                    print("Please choose again.")
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.")
            else:
                print("Invalid race. Please try again!")
        
        print(f"This is your character's race: {self.race_choice}")
        return self.race_choice

    
    def dwarf_type(self):
        """If user chose dwarf, show the types of dwarfs and choose the type

        Returns:
            dwarf_choice: dwarf type
        """
        if self.race_choice != "Dwarf": #ensures that only users who chose dwarf can select type
            return None
            
        while True:
            print(f"You chose to be a dwarf!")
            self.show_type()
            dwarf_choice = input("Choose your type: ").capitalize() 

            if dwarf_choice in Race.dwarf_types: #validates type
                print(f"You chose: {dwarf_choice}.")
                while True:
                    confirm = input("Would you like to proceed? (Y/N) ").capitalize()
                    if confirm == "Y":
                        return f"Dwarf type: {dwarf_choice}"
                    elif confirm == "N":
                        print("Choose your dwarf type again.")  # Allow the user to choose again
                        break
                    else:
                        print("Invalid input. Please enter 'Y' or 'N'.")  # Invalid confirmation input
            else:
                print("Invalid type. Please try again!") 

           
    def elf_type(self):
        """If user chose elf, choose the type

        Returns:
            elf_choice: elf type
        """
        if self.race_choice != "Elf": #ensures that only users who chose elf can select type
            return None
        
        while True:
            print(f"You chose to be an elf!")
            self.show_type()
            elf_choice = input("Choose your type: ").capitalize()
        
            if elf_choice in Race.elf_types:
                print(f"You chose: {elf_choice}.")
                while True:
                    confirm = input("Would you like to proceed? (Y/N) ").capitalize()
                    if confirm == "Y":
                        return f"Elf type: {elf_choice}" 
                    elif confirm == "N":
                        print("Choose your elf type again.")  # Allow the user to choose again
                        break
                    else:
                        print("Invalid input. Please enter 'Y' or 'N'.")  # Invalid confirmation input
            else:
                print("Invalid type. Please try again!") 
            
            
            
    def halfling_type(self):
        """If user chose halfling, choose the type

        Returns:
            halfling_type: halfling type
        """
        if self.race_choice != "Halfling": #ensures that only users who chose halfling can select type
            return None
        while True:
            print(f"You chose to be a halfling!")
            self.show_type()
            halfling_choice = input("Choose your type: ").capitalize()
        
            if halfling_choice in Race.halfling_types:
                print(f"You chose: {halfling_choice}.")
                while True:
                    confirm = input("Would you like to proceed? (Y/N) ").capitalize()
                    if confirm == "Y":
                        return f"Halfling type: {halfling_choice}"  
                    elif confirm == "N":
                        print("Choose your halfling type again.")  # Allow the user to choose again
                        break  
                    else:
                        print("Invalid input. Please enter 'Y' or 'N'.")  # Invalid confirmation input
            else:
                print("Invalid type. Please try again!") 
            
            
            
