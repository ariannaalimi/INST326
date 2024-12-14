class DND_Class:
    """User chooses their character's class and based on their class,
        the user chooses their armor, weapon, tools, and skills
    """

    classes = {
        "Barbarian": "A fierce warrior of primitive background who can enter a battle rage",
        "Bard": "An inspiring magician whose power echoes the music of creation", 
        "Cleric": "A priestly champion who wields divine magic in service of a higher power",
        "Druid": "A priest of the Old Faith, wielding the powers of nature — moonlight and plant growth, fire and lightning — and adopting animal forms",
        "Fighter": "A master of martial combat, skilled with a variety of weapons and armor",
        "Monk": "A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection",
        "Paladin": "A holy warrior bound to a sacred oath",
        "Ranger": "A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization",
        "Rogue": "A scoundrel who uses stealth and trickery to overcome obstacles and enemies",
        "Sorcerer": "A spellcaster who draws on inherent magic from a gift or bloodline",
        "Warlock": "A wielder of magic that is derived from a bargain with an extraplanar entity",
        "Wizard": "A scholarly magic-user capable of manipulating the structures of reality"
    }

    artisan_tool = {"Alcehmist's supplies",
                        "Brewer's supplies",
                        "Calligrapher's supplies",
                        "Carpenter's tools",
                        "Cartographer's tools",
                        "Cobbler's tools",
                        "Cook's utensils",
                        "Glassblower's tools",
                        "Jeweler's tools",
                        "Leatherworker's tools",
                        "Mason's tools",
                        "Painter's supplies",
                        "Potter's tools",
                        "Smith's tools",
                        "Tinker's tools",
                        "Weaver's tools",
                        "Woodcarver's tools",

    }

    musical_instruments = {"Lyre",
                                "Drums",
                                "Kazoo"
    }

    def __init__(self, class_choice):
        """Attributes for character based on class chosen

        Args:
            class_choice (str): Character class

        """
        self.class_choice = class_choice
  
    @property
    def choose(self):
        return self.class_choice

    @choose.getter
    def choose(self, class_choice):
        self.class_choice = class_choice        
        
    def show_classes():
        """Presents the options for classes for the user
        """
        print("These are the classes: ")
        for dnd_class, description in DND_Class.classes.items():
            print(f"- {dnd_class}: {description}")

    def choose_class():
        """Prompts user to choose class

        Returns:
            class_choice: class choice
        """
        DND_Class.show_classes()
        while True:
            class_choice = input("Choose a class by typing it as shown: ").capitalize()

            if class_choice in DND_Class.classes: #validates the class
                print(f"You chose: {class_choice}.")
                confirm = input("Would you like to proceed? (Y/N) ").capitalize()
                if confirm == "Y":
                    return class_choice  # Proceed with the class choice
                elif confirm == "N":
                    print("Please choose a class again.")  # Let the user choose again
                    continue  # Loop back to the start of the class choice prompt
                else:
                    print("Invalid input. Please enter 'Y' or 'N'")  # Handle invalid confirmation input
            else:
                print("Invalid class. Please try again!")
            
    def barbarian_prof(self):
        """If user chooses barbarian class, this class prompts the user to choose their proficiences and also
        lets the user know if there is options for certain proficiencies

        Returns:
            f string: shows armor choice, shield choice, weapon choice, and tool choice

        """
        while self.class_choice == "Barbarian":
            # Armor choice
            while True:
                armor_choice = input("Your character can have light armor OR medium armor. Which one would you like? Please type 'light' or 'medium': ").strip().lower()
                if armor_choice in ["light", "medium"]: #validates that the armor is in this list
                    confirm = input(f"You chose {armor_choice} armor. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y": 
                        break
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please type 'light' or 'medium'.")
            
            # Shield option
            while True:
                shield_opt = input("Your character can also have a shield! Would you like a shield? (Y/N): ").capitalize()
                if shield_opt in ["Y", "N"]:
                    shield_choice = "a shield" if shield_opt == "Y" else "no shield" #changes the string dependent on if the user said yes or no to having a shield
                    confirm = input(f"You chose to have {shield_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        break
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please type 'Y' or 'N'.")
            
            # Weapon choice
            while True:
                weapon_choice = input("Your character can have simple OR martial weapons. Which one would you like? Please type 'simple' or 'martial': ").strip().lower()
                if weapon_choice in ["simple", "martial"]: #validates that weapon is in the list
                    confirm = input(f"You chose {weapon_choice} weapons. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        break
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please try again.")

            print(f"Your character uses {armor_choice} armor, {shield_choice}, {weapon_choice} weapons, and no tools.")
            return (f"Your character uses {armor_choice} armor, {shield_choice}, {weapon_choice} weapons, and no tools.")

    def barbarian_skill(self):
        """If user chooses barbarian class, this class prompts the user to choose their skills

        Returns:
            chose_skills: skills chosen and stored

        """
        skill_option = {"Animal Handling", 
                        "Athletics", 
                        "Intimidation", 
                        "Nature", 
                        "Perception", 
                        "Survival"
        }

        while self.class_choice == "Barbarian":
            print(f"You may choose two skills for your character from this list: {', '.join(skill_option)}") # used ChatGPT for the .join
            chose_skills = [] #skills chosen by user will be stored here 
            while len(chose_skills) < 2: #user can only choose skills if the list has less than 2 skills
                print(f"You may choose two skills for your character from this list: {', '.join(skill_option)}")
                skill_choice = input(f"Please choose skill {len(chose_skills) + 1}: ").strip()

                if skill_choice in chose_skills: #checks if there is duplicates
                    print("You already chose that skill earlier! Please choose a different one.") 
                elif skill_choice in skill_option:
                    confirm = input(f"Nice! You chose {skill_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        chose_skills.append(skill_choice)
                        if len(chose_skills) == 2: # checks to see if chose_skills is filled for that specific class
                            print(f"These are your skills: {', '.join(chose_skills)}")
                            return f"These are your skills: {', '.join(chose_skills)}"
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please choose a skill from the list.")

            print(f"These are your skills: {', '.join(chose_skills)}")
            return f"These are your skills: {', '.join(chose_skills)}"
            
    def bard_prof(self):
        """If user chooses bard class, this class prompts the user to choose their proficiencies and also
        lets the user know if there are options for certain proficiencies.

        Returns:
            f string: shows armor choice, shield choice, weapon choice, and tool choice
        """

        weapons = {"Simple weapons",
                "Hand crossbows",
                "Longswords",
                "Rapiers",
                "Shortswords"}

        musical_instruments = {"Lyre",
                            "Drums",
                            "Kazoo"}

        weapon_choice = None
        tool_choice = None

        while self.class_choice == "Bard":
            print("Your character can only have light armor.")
            print(f"Your character can choose from these weapons: {weapons}")

            while True:
                weapon_choice = input("Which one would you like? Please type it exactly as shown. ").capitalize()  # Ensure it's properly capitalized
                if weapon_choice in weapons:
                    confirm = input("Nice! Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        break  
                    elif confirm == "N":
                        continue  
                    else:
                        print("Invalid input. Please type (Y/N).")
                else:
                    print("Invalid input. Please try again!")

            while True:
                print(f"For your tools, your character can choose from these musical instruments: {musical_instruments}")
                tool_choice = input("Which one would you like? Please type it exactly as shown. ").capitalize() 
                
                if tool_choice in musical_instruments:
                    confirm = input("Nice! Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        break  
                    elif confirm == "N":
                        continue  
                    else:
                        print("Invalid input. Please type (Y/N).")
                else:
                    print("Invalid input. Please try again.")
            print(f"Your character has light armor with no shield. Your character uses {weapon_choice.lower()} and {tool_choice.lower()} as tools.")
            return f"Your character has light armor with no shield. Your character uses {weapon_choice.lower()} and {tool_choice.lower()} as tools."

    def bard_skill(self):
        """If user chooses bard class, this class prompts the user to choose their skills

        Returns:
           chose_skills: skills chosen and stored


        """

        skill_option = {"Acrobatics", 
                        "Animal Handling", 
                        "Arcana",
                        "Athletics",
                        "Deception",
                        "History",
                        "Insight", 
                        "Intimidation", 
                        "Investigation",
                        "Medicine",
                        "Nature", 
                        "Perception",
                        "Performance",
                        "Persuasion",
                        "Religion",
                        "Sleight of Hand",
                        "Stealth", 
                        "Survival"
        }

        while self.class_choice == "Bard":
            print(f"You may choose three skills for your character from this list: {', '.join(skill_option)}")
        
            chose_skills = []  # Stores the skills the player chose
        
        # Loop for first skill choice
            while len(chose_skills) < 3:
                print(f"You may choose two skills for your character from this list: {', '.join(skill_option)}")
                skill_choice = input(f"Please choose skill {len(chose_skills) + 1}: ").strip()

                if skill_choice in chose_skills:
                    print("You already chose that skill earlier! Please choose a different one.")
                elif skill_choice in skill_option:
                    confirm = input(f"Nice! You chose {skill_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        chose_skills.append(skill_choice)
                        if len(chose_skills) == 3:
                            print(f"These are your skills: {', '.join(chose_skills)}")
                            return f"These are your skills: {', '.join(chose_skills)}"
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please choose a skill from the list.")

            print(f"These are your skills: {', '.join(chose_skills)}")
            return f"These are your skills: {', '.join(chose_skills)}"
        
    def cleric_prof(self):
        """If user chooses cleric class, this class prompts the user to choose their proficiences and also
        lets the user know if there is options for certain proficiencies

        Returns:
            f string: shows armor choice, shield choice,  weapon choice, and tool choice

        """

        while self.class_choice == "Cleric":
        # Armor choice
            while True:
                armor_choice = input("Your character can have light armor OR medium armor. Which one would you like? Please type 'light' or 'medium': ").strip().lower()
                if armor_choice in ["light", "medium"]:
                    confirm = input(f"You chose {armor_choice} armor. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        break
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please try again.")
                
    
            while True:
                shield_opt = input("Your character can also have a shield! Would you like a shield? (Y/N): ").capitalize()
                if shield_opt in ["Y", "N"]:
                    shield_choice = "a shield" if shield_opt == "Y" else "no shield"
                    confirm = input(f"You chose to have {shield_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        break
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please type 'Y' or 'N'.")
                    
            return(f"Your character uses {armor_choice} armor with {shield_choice}. Your character uses all simple weapons and no tools.")
    def cleric_skill(self):
        """If user chooses cleric class, this class prompts the user to choose their skills

        Returns:
            chose_skills: skills chosen and stored

        """
        
        skill_option = {"History",
                        "Insight", 
                        "Medicine",
                        "Persuasion",
                        "Religion",
                        
        }

        while self.class_choice == "Cleric":
            print(f"You may choose two skills for your charaacter from this list: {skill_option}")
            chose_skills = [] 
            while len(chose_skills) < 2:
                print(f"You may choose two skills for your character from this list: {', '.join(skill_option)}")
                skill_choice = input(f"Please choose skill {len(chose_skills) + 1}: ").strip()

                if skill_choice in chose_skills:
                    print("You already chose that skill earlier! Please choose a different one.")
                elif skill_choice in skill_option:
                    confirm = input(f"Nice! You chose {skill_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        chose_skills.append(skill_choice)
                        if len(chose_skills) == 2:
                            print(f"These are your skills: {', '.join(chose_skills)}")
                            return f"These are your skills: {', '.join(chose_skills)}"
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please choose a skill from the list.")

            print(f"These are your skills: {', '.join(chose_skills)}")
            return f"These are your skills: {', '.join(chose_skills)}"
            
    def druid_prof(self):
        """If user chooses druid class, this class prompts the user to choose their proficiences and also
        lets the user know if there is options for certain proficiencies

        Returns:
            f string: shows armor choice, shield choice, weapon choice, and tool choice

        """

        weapons = {"Clubs",
                    "Daggers",
                    "Dart",
                    "Javelins",
                    "Maces",
                    "Quarterstaffs",
                    "Scimitars",
                    "Sickles",
                    "Slings",
                    "Spears"
        }

        while (self.class_choice == "Druid"):
            print(f"Your tool is an herbalism kit.")
            print(f"Your character can have light armor OR medium armor. Druids will not wear armor made of metal.")
            while True:
                armor_choice = input("Your character can have light armor OR medium armor. Which one would you like? Please type 'light' or 'medium': ").strip().lower()
                if armor_choice in ["light", "medium"]:
                    confirm = input(f"You chose {armor_choice} armor. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        break
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please try again.")
                
            
            while True:
                shield_opt = input("Your character can also have a shield! Druids will not use shields made of metal. Would you like a shield? (Y/N) ") 
                if shield_opt in ["Y", "N"]:
                    shield_choice = "a shield" if shield_opt == "Y" else "no shield"
                    confirm = input(f"You chose to have {shield_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        break
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please try again.")
                

            # Weapon choice
            while True:
                print(f"Your character can choose from these weapons: {weapons}")
                weapon_choice = input("Which one would you like? Please type it exactly as shown. ").capitalize()
                if weapon_choice in weapons:
                    confirm = input("Nice! Would you like to proceed? (Y/N) ").capitalize()
                    if confirm == "Y":
                        break  # Exit weapon choice loop
                    elif confirm == "N":
                        continue  # Restart loop for new weapon choice
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please try again.")
                
            
            print(f"Your character has {armor_choice} armor with {shield_choice}. Your character uses {weapon_choice.lower()} and an herbalism kit.")        
            return(f"Your character has {armor_choice} armor with {shield_choice}. Your character uses {weapon_choice.lower()} and an herbalism kit.")    
    
    def druid_skill(self):
        """If user chooses druid class, this class prompts the user to choose their skills

        Returns:
            chose_skills: skills chosen and stored

        """

        skill_option = {"Arcana",
                        "Animal Handling", 
                        "Insight",
                        "Medicine",
                        "Nature",
                        "Perception",
                        "Religion",
                        "Survival"
                        
        }

        while (self.class_choice == "Druid"):
            print(f"You may choose two skills for your character from this list: {skill_option}")
           
            chose_skills = []           
            while len(chose_skills) < 2:
                print(f"You may choose two skills for your character from this list: {', '.join(skill_option)}")
                skill_choice = input(f"Please choose skill {len(chose_skills) + 1}: ").strip()

                if skill_choice in chose_skills:
                    print("You already chose that skill earlier! Please choose a different one.")
                elif skill_choice in skill_option:
                    confirm = input(f"Nice! You chose {skill_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        chose_skills.append(skill_choice)
                        if len(chose_skills) == 2:
                            print(f"These are your skills: {', '.join(chose_skills)}")
                            return f"These are your skills: {', '.join(chose_skills)}"
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please choose a skill from the list.")

            print(f"These are your skills: {', '.join(chose_skills)}")
            return f"These are your skills: {', '.join(chose_skills)}"

    def fighter_prof(self):

        """If user chooses fighter class, this class prompts the user to choose their proficiences and also
        lets the user know if there is options for certain proficiencies

        Returns:
           f string: shows armor choice, shield choice, weapon choice, and tool choice
        """

        while (self.class_choice == "Fighter"):
            print(f"Your character can use all armor! This is the list of all armors: light, medium, or heavy")
            while True:
                armor_choice = input(" Which one would you like? Please type it as shown. ")
                if armor_choice in ["light", "medium", "heavy"]:
                    print(f"You chose: {armor_choice}.")
                    confirm = input("Would you like to proceed? (Y/N) ").capitalize()
                    if (confirm == "Y"):
                        break
                    elif (confirm == "N" or confirm =="n"):
                        print("Which one would you like? Please type it as shown. ")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please try again.")
                
        
            while True:
                shield_opt = input("Your character can also have a shield! Would you like a shield? (Y/N): ").capitalize()
                if shield_opt in ["Y", "N"]:
                    shield_choice = "a shield" if shield_opt == "Y" else "no shield"
                    confirm = input(f"You chose to have {shield_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        break
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please try again.")
                
            
            while True:
                weapon_choice = input("Your character can have simple OR martial weapons. Which one would you like? Please type 'simple' or 'martial'. ")
                if weapon_choice in ["simple", "martial"]:
                    print(f"You chose: {weapon_choice}.")
                    confirm = input("Would you like to proceed? (Y/N) ").capitalize()
                    if (confirm == "Y"):
                        break
                    elif (confirm == "N"):
                        print("Which one would you like? Please type 'simple' or 'martial'.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please try again.")
                
                
            print(f"Your character uses {armor_choice} armor, has {shield_choice}, a {weapon_choice} weapon, and no tools.")
            return(f"Your character uses {armor_choice} armor, has {shield_choice}, a {weapon_choice} weapon, and no tools.")
        
    def fighter_skill(self):
        """If user chooses fighter class, this class prompts the user to choose their skills

        Returns:
          chose_skills: skills chosen and stored

        """

        skill_option = {"Acrobatics",
                        "Animal Handling", 
                        "Athletics",
                        "History",
                        "Insight",
                        "Intimidation",
                        "Perception",
                        "Survival"
                        
        }

        while (self.class_choice == "Fighter"):
            print(f"You may choose two skills for your character from this list: {skill_option}")
            chose_skills = []           
            while len(chose_skills) < 2:
                print(f"You may choose two skills for your character from this list: {', '.join(skill_option)}")
                skill_choice = input(f"Please choose skill {len(chose_skills) + 1}: ").strip()

                if skill_choice in chose_skills:
                    print("You already chose that skill earlier! Please choose a different one.")
                elif skill_choice in skill_option:
                    confirm = input(f"Nice! You chose {skill_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        chose_skills.append(skill_choice)
                        if len(chose_skills) == 2:
                            print(f"These are your skills: {', '.join(chose_skills)}")
                            return f"These are your skills: {', '.join(chose_skills)}"
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please choose a skill from the list.")

            print(f"These are your skills: {', '.join(chose_skills)}")
            return f"These are your skills: {', '.join(chose_skills)}"

    def monk_prof(self):
        """If user chooses monk class, this class prompts the user to choose their proficiences and also
        lets the user know if there is options for certain proficiencies

        Returns:
           f string: shows armor choice, shield choice, weapon choice, and tool choice

        """
    
        while (self.class_choice == "Monk"):
            print("Your character have no armor and no shield.")

            while True:
                weapon_choice = input("Your character can have 'simple weapons' OR 'shortswords'. Which one would you like? Please type 'simple' OR 'shortswords'. ")
                if weapon_choice in ["simple weapons", "shortswords"]:
                    
                    print(f"You chose: {weapon_choice}.")
                    confirm = input(f"You chose {weapon_choice} weapons. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        break
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please try again.")
                    
            while True:
                print(f"Your character can choose ONE artisan tool or musical instrument. \nArtisan Tools: {DND_Class.artisan_tool} \nMusical Instruments: {DND_Class.musical_instruments}")
                tool_choice = input("Which tool would you like? Please type it exactly as shown. ").capitalize()
                if tool_choice in DND_Class.artisan_tool or DND_Class.musical_instruments:
                    print(f"You chose: {tool_choice}")
                    confirm = input("Would you like to proceed? (Y/N) ").capitalize()
                    if (confirm == "Y"):
                        break
                    elif (confirm == "N"):
                        print("Which one would you like? Please type it as shown. ").capitalize()

                    else:
                        print("Invalid input. Please type (Y/N). ")

                else:
                    print("Invalid input. Please try again.")
                
            
            print(f"Your character has no armor and no shield. Your character uses {weapon_choice} and {tool_choice.lower()} as a tool.")
            return f"Your character has no armor and no shield. Your character uses {weapon_choice} and {tool_choice.lower()} as a tool."
    
    def monk_skill(self):
        """If user chooses monk class, this class prompts the user to choose their skills

        Returns:
          chose_skills: skills chosen and stored

        """

        skill_option = {"Acrobatics",
                        "Athletics",
                        "History",
                        "Insight",
                        "Religion"
        }

        while (self.class_choice == "Monk"):
            print(f"You may choose two skills for your character from this list: {skill_option}")
           
            chose_skills = []           
            while len(chose_skills) < 2:
                print(f"You may choose two skills for your character from this list: {', '.join(skill_option)}")
                skill_choice = input(f"Please choose skill {len(chose_skills) + 1}: ").strip()

                if skill_choice in chose_skills:
                    print("You already chose that skill earlier! Please choose a different one.")
                elif skill_choice in skill_option:
                    confirm = input(f"Nice! You chose {skill_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        chose_skills.append(skill_choice)
                        if len(chose_skills) == 2:
                            print(f"These are your skills: {', '.join(chose_skills)}")
                            return f"These are your skills: {', '.join(chose_skills)}"
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please choose a skill from the list.")

            print(f"These are your skills: {', '.join(chose_skills)}")
            return f"These are your skills: {', '.join(chose_skills)}"
        
    def paladin_prof(self):
        """If user chooses paladin class, this class prompts the user to choose their proficiences and also
        lets the user know if there is options for certain proficiencies

        Returns:
            f string: shows armor choice, shield choice, weapon choice, and tool choice

        """

        while (self.class_choice == "Paladin"):
            print(f"Your character can use all armor! This is the list of all armors: light, medium, or heavy")
            while True:
                armor_choice = input(" Which one would you like? Please type it exactly as shown. ")
                if armor_choice in ["light", "medium", "heavy"]:
                    print(f"You chose: {armor_choice}.")
                    confirm = input("Would you like to proceed? (Y/N) ").capitalize()
                    if (confirm == "Y"):
                        break
                    elif (confirm == "N" or confirm =="n"):
                        print("Which one would you like? Please type it as shown. ").capitalize()
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please try again.")

            while True:
                shield_opt = input("Your character can also have a shield! Would you like a shield? (Y/N): ").capitalize()
                if shield_opt in ["Y", "N"]:
                    shield_choice = "a shield" if shield_opt == "Y" else "no shield"
                    confirm = input(f"You chose to have {shield_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        break
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please type 'Y' or 'N'.")
            
            while True:
                weapon_choice = input("Your character can have simple OR martial weapons. Which one would you like? Please type 'simple' or 'martial': ").strip().lower()
                if weapon_choice in ["simple", "martial"]:
                    confirm = input(f"You chose {weapon_choice} weapons. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        break
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please try again.")
            
            print(f"Your character uses {armor_choice} armor, has {shield_choice}, a {weapon_choice} weapon, and no tools.")
            return(f"Your character uses {armor_choice} armor, has {shield_choice}, a {weapon_choice} weapon, and no tools.")

    def paladin_skill(self):
        """If user chooses paladin class, this class prompts the user to choose their skills

        Returns:
            chose_skills: skills chosen and stored

        """

        skill_option = {"Athletics",
                            "Insight",
                            "Intimidation",
                            "Medicine",
                            "Persuasion",
                            "Religion"
        }

        while (self.class_choice == "Paladin"):
            print(f"You may choose two skills for your character from this list: {skill_option}")
           
            chose_skills = []           
            while len(chose_skills) < 2:
                print(f"You may choose two skills for your character from this list: {', '.join(skill_option)}")
                skill_choice = input(f"Please choose skill {len(chose_skills) + 1}: ").strip()

                if skill_choice in chose_skills:
                    print("You already chose that skill earlier! Please choose a different one.")
                elif skill_choice in skill_option:
                    confirm = input(f"Nice! You chose {skill_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        chose_skills.append(skill_choice)
                        if len(chose_skills) == 2:
                            print(f"These are your skills: {', '.join(chose_skills)}")
                            return f"These are your skills: {', '.join(chose_skills)}"
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please choose a skill from the list.")

            print(f"These are your skills: {', '.join(chose_skills)}")
            return f"These are your skills: {', '.join(chose_skills)}"

    def ranger_prof(self):
        """If user chooses ranger class, this class prompts the user to choose their proficiences and also
        lets the user know if there is options for certain proficiencies

        Returns:
            f string: shows armor choice, shield choice, weapon choice, and tool choice

        """

        while (self.class_choice == "Ranger"):
            while True:
                armor_choice = input("Your character can have light armor OR medium armor. Which one would you like? Please type 'light' or 'medium': ").strip().lower()
                if armor_choice in ["light", "medium"]:
                    confirm = input(f"You chose {armor_choice} armor. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        break
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please type 'light' or 'medium'.")
            
            while True:
                shield_opt = input("Your character can also have a shield! Would you like a shield? (Y/N): ").capitalize()
                if shield_opt in ["Y", "N"]:
                    shield_choice = "a shield" if shield_opt == "Y" else "no shield"
                    confirm = input(f"You chose to have {shield_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        break
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please type 'Y' or 'N'.")
            
            while True:
                weapon_choice = input("Your character can have simple OR martial weapons. Which one would you like? Please type 'simple' or 'martial': ").strip().lower()
                if weapon_choice in ["simple", "martial"]:
                    confirm = input(f"You chose {weapon_choice} weapons. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        break
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please try again.")
            
            print(f"Your character uses {armor_choice} armor, has {shield_choice}, a {weapon_choice} weapon, and no tools.")
            return(f"Your character uses {armor_choice} armor, has {shield_choice}, a {weapon_choice} weapon, and no tools.")

    def ranger_skill(self):
        """If user chooses ranger class, this class prompts the user to choose their skills

        Returns:
            chose_skills: skills chosen and stored
        """

        skill_option = {"Animal Handling",
                        "Athletics",
                        "Insight", 
                        "Investigation", 
                        "Nature", 
                        "Perception",
                        "Stealth", 
                        "Survival"
        }

        while (self.class_choice == "Ranger"):
            print(f"You may choose three skills for your character from this list: {skill_option}")
            chose_skills = []  
        
            while len(chose_skills) < 3:
                print(f"You may choose two skills for your character from this list: {', '.join(skill_option)}")
                skill_choice = input(f"Please choose skill {len(chose_skills) + 1}: ").strip()

                if skill_choice in chose_skills:
                    print("You already chose that skill earlier! Please choose a different one.")
                elif skill_choice in skill_option:
                    confirm = input(f"Nice! You chose {skill_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        chose_skills.append(skill_choice)
                        if len(chose_skills) == 3:
                            print(f"These are your skills: {', '.join(chose_skills)}")
                            return f"These are your skills: {', '.join(chose_skills)}"
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please choose a skill from the list.")

            print(f"These are your skills: {', '.join(chose_skills)}")
            return f"These are your skills: {', '.join(chose_skills)}"

    def rogue_prof(self):
        """If user chooses rogue class, this class prompts the user to choose their proficiences and also
        lets the user know if there is options for certain proficiencies

        Returns:
           f string: shows armor choice, shield choice, weapon choice, and tool choice
        """

        weapons = {"Simple weapons",
                    "Handcrossbows",
                    "Longswords",
                    "Rapiers",
                    "Shortswords"
        }

        while (self.class_choice == "Rogue"):
            print(f"Your character can only hav light armor.")
            print(f"Your character can choose from these weapons: {weapons}")
            while True:
                weapon_choice = input("Which one would you like? Please type it as shown. ").capitalize().capitalize()
                if weapon_choice in weapons:
                    confirm = input("Nice! Would you like to proceed? (Y/N): ").capitalize()
                    if confirm== "Y":
                        break  # Exit the loop once weapon choice is confirmed
                    elif confirm == "N":
                        print("Which one would you like? Please type it exactly as shown.")
                    else:
                        print("Invalid input. Please type (Y/N).")
                else:
                    print("Invalid input. Please try again!")
            
            print(f"Your character uses light armor and no shield, {weapon_choice.lower()}, and thieves' tools.")
            return(f"Your character uses light armor and no shield, {weapon_choice.lower()}, and thieves' tools.")
    def rogue_skill(self):
        """If user chooses rogue class, this class prompts the user to choose their skills

        Returns:
           chose_skills: skills chosen and stored

        """

        skill_option = {"Acrobatics",
                        "Athletics",
                        "Deception",
                        "Insight",
                        "Intimidation", 
                        "Investigation", 
                        "Perception", 
                        "Performance",
                        "Persuasion",
                        "Sleight of Hand", 
                        "Stealth"
        }

        while (self.class_choice == "Rogue"):
            chose_skills = []  
        
           
            while len(chose_skills) < 4:
                print(f"You may choose four skills for your character from this list: {', '.join(skill_option)}")
                skill_choice = input(f"Please choose skill {len(chose_skills) + 1}: ").strip()

                if skill_choice in chose_skills:
                    print("You already chose that skill earlier! Please choose a different one.")
                elif skill_choice in skill_option:
                    confirm = input(f"Nice! You chose {skill_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        chose_skills.append(skill_choice)
                        if len(chose_skills) == 4:
                            print(f"These are your skills: {', '.join(chose_skills)}")
                            return f"These are your skills: {', '.join(chose_skills)}"
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please choose a skill from the list.")

            print(f"These are your skills: {', '.join(chose_skills)}")
            return f"These are your skills: {', '.join(chose_skills)}"

    def sorcerer_prof(self):
        """If user chooses sorcerer class, this class prompts the user to choose their proficiences and also
        lets the user know if there is options for certain proficiencies

        Returns:
           f string: shows armor choice, shield choice, weapon choice, and tool choice

        """

        weapons = {"Daggers",
                    "Darts",
                    "Slings",
                    "Quarterstaffs",
                    "Light crossbows"
        }

        while (self.class_choice == "Sorcerer"):
            print(f"Your character has no armor and no shield.")
            print(f"Your character can choose from these weapons: {weapons}")
            while True:
                weapon_choice = input("Which one would you like? Please type it exactly as shown. ").capitalize()
                if weapon_choice in weapons:
                    confirm = input("Nice! Would you like to proceed? (Y/N): ").capitalize()
                    if confirm== "Y":
                        break  # Exit the loop once weapon choice is confirmed
                    elif confirm == "N":
                        print("Which one would you like? Please type it as shown. ")
                    else:
                        print("Invalid input. Please type (Y/N).")
                else:
                    print("Invalid input. Please try again!")

            print(f"Your character uses no armor and no shield, {weapon_choice.lower()}, and no tools.")  
            return(f"Your character uses no armor and no shield, {weapon_choice.lower()}, and no tools.")  

    def sorcerer_skill(self):
        """If user chooses sorcerer class, this class prompts the user to choose their skills

        Returns:
            chose_skills: skills chosen and stored

        """

        skill_option = {"Arcana",
                        "Deception",
                        "Insight", 
                        "Intimidation", 
                        "Persuasion", 
                        "Religion"
        }

        while (self.class_choice == "Sorcerer"):
            chose_skills = []           
            while len(chose_skills) < 2:
                print(f"You may choose two skills for your character from this list: {', '.join(skill_option)}")
                skill_choice = input(f"Please choose skill {len(chose_skills) + 1}: ").strip()

                if skill_choice in chose_skills:
                    print("You already chose that skill earlier! Please choose a different one.")
                elif skill_choice in skill_option:
                    confirm = input(f"Nice! You chose {skill_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        chose_skills.append(skill_choice)
                        if len(chose_skills) == 2:
                            print(f"These are your skills: {', '.join(chose_skills)}")
                            return f"These are your skills: {', '.join(chose_skills)}"
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please choose a skill from the list.")

            print(f"These are your skills: {', '.join(chose_skills)}")
            return f"These are your skills: {', '.join(chose_skills)}"

    def warlock_prof(self):
        """If user chooses warlock class, this class prompts the user to choose their proficiences and also
        lets the user know if there is options for certain proficiencies

        Returns:
           f string: shows armor choice, shield choice, weapon choice, and tool choice
        """

        while (self.class_choice == "Warlock"):
            print(f"Your character uses light armor and no shield, simple weapons, and no tools.") 
            return(f"Your character uses light armor and no shield, simple weapons, and no tools.")  

    def warlock_skill(self):
        """If user chooses warlock class, this class prompts the user to choose their skills

        Returns:
           chose_skills: skills chosen and stored


        """

        skill_option = {"Arcana",
                        "Deception",
                        "History", 
                        "Intimidation", 
                        "Investigation",
                        "Nature", 
                        "Religion"
        }

        while (self.class_choice == "Warlock"):
            chose_skills = []           
            while len(chose_skills) < 2:
                print(f"You may choose two skills for your character from this list: {', '.join(skill_option)}")
                skill_choice = input(f"Please choose skill {len(chose_skills) + 1}: ").strip()

                if skill_choice in chose_skills:
                    print("You already chose that skill earlier! Please choose a different one.")
                elif skill_choice in skill_option:
                    confirm = input(f"Nice! You chose {skill_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        chose_skills.append(skill_choice)
                        if len(chose_skills) == 2:
                            print(f"These are your skills: {', '.join(chose_skills)}")
                            return f"These are your skills: {', '.join(chose_skills)}"
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please choose a skill from the list.")

            print(f"These are your skills: {', '.join(chose_skills)}")
            return f"These are your skills: {', '.join(chose_skills)}"

    def wizard_prof(self):
        """If user chooses wizard class, this class prompts the user to choose their proficiences and also
        lets the user know if there is options for certain proficiencies

        Returns:
            f string: shows armor choice, shield choice, weapon choice, and tool choice
        """

        weapons = {"Daggers",
                    "Darts",
                    "Slings",
                    "Quarterstaffs",
                    "Light crossbows"
        }

        while self.class_choice == "Wizard":
            print(f"Your character can choose from these weapons: {weapons}")
            while True:
                    weapon_choice = input("Which one would you like? Please type it as shown. ").capitalize()
                    if weapon_choice in weapons:
                        confirm = input("Nice! Would you like to proceed? (Y/N): ").capitalize()
                        if confirm== "Y":
                            break  
                        elif confirm == "N":
                            continue  
                        else:
                            print("Invalid input. Please type (Y/N).")
                    else:
                        print("Invalid input. Please try again!")

            print(f"Your character has no armor and no shield, {weapon_choice.lower()}, and no tools.")  
            return(f"Your character has no armor and no shield, {weapon_choice.lower()}, and no tools.")  
    def wizard_skill(self):

        """If user chooses wizard class, this class prompts the user to choose their skills

        Returns:
            chose_skills: skills chosen and stored

        """

        skill_option = {"Arcana",
                        "History",
                        "Insight", 
                        "Investigation", 
                        "Medicine",
                        "Religion"
        }

        while (self.class_choice == "Wizard"):
            chose_skills = []           
            while len(chose_skills) < 2:
                print(f"You may choose two skills for your character from this list: {', '.join(skill_option)}")
                skill_choice = input(f"Please choose skill {len(chose_skills) + 1}: ").strip()

                if skill_choice in chose_skills:
                    print("You already chose that skill earlier! Please choose a different one.")
                elif skill_choice in skill_option:
                    confirm = input(f"Nice! You chose {skill_choice}. Would you like to proceed? (Y/N): ").capitalize()
                    if confirm == "Y":
                        chose_skills.append(skill_choice)
                        if len(chose_skills) == 2:
                            print(f"These are your skills: {', '.join(chose_skills)}")
                            return f"These are your skills: {', '.join(chose_skills)}"
                    elif confirm == "N":
                        print("Please choose again.")
                    else:
                        print("Invalid input. Please type 'Y' or 'N'.")
                else:
                    print("Invalid input. Please choose a skill from the list.")

            print(f"These are your skills: {', '.join(chose_skills)}")
            return f"These are your skills: {', '.join(chose_skills)}"
