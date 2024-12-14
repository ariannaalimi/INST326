from dnd import DND_Class
from race import Race
from trait import Trait
def main():
    print("")
    print("Welcome to DnD! You are going to be creating your character by picking their Class, Race, and their Traits!")
    print("\nLet's first start with the class!")

    chosen_class_name = DND_Class.choose_class()
    dnd_class_instance = DND_Class(chosen_class_name) #ChatGPT to help with instance

    class_choice = dnd_class_instance.class_choice.capitalize()

    if (class_choice == "Barbarian"):
        print("You chose the Cleric Class!")
        dnd_class_instance.barbarian_prof()
        print("Now you will choose your skill:")
        dnd_class_instance.barbarian_skill()
    
    if (class_choice == "Bard"):
        print("You chose the Bard Class!")
        dnd_class_instance.bard_prof()
        print("Now you will choose your skill:")
        dnd_class_instance.bard_skill()

    if (class_choice == "Cleric"):
        print("You chose the Cleric Class!")
        dnd_class_instance.cleric_prof()
        print("Now you will choose your skill:")
        dnd_class_instance.cleric_skill()
    
    if (class_choice == "Druid"):
        print("You chose the Druid Class!")
        dnd_class_instance.druid_prof()
        print("Now you will choose your skill:")
        dnd_class_instance.druid_skill()

    if (class_choice == "Fighter"):
        print("You chose the Fighter Class!")
        dnd_class_instance.fighter_prof()
        print("Now you will choose your skill:")
        dnd_class_instance.fighter_skill()
    
    if (class_choice == "Monk"):
        print("You chose the Monk Class!")
        dnd_class_instance.monk_prof()
        print("Now you will choose your skill:")
        dnd_class_instance.monk_skill()

    if (class_choice == "Paladin"):
        print("You chose the Paladin Class!")
        dnd_class_instance.paladin_prof()
        print("Now you will choose your skill:")
        dnd_class_instance.paladin_skill()

    if (class_choice == "Ranger"):
        print("You chose the Ranger Class!")
        dnd_class_instance.ranger_prof()
        print("Now you will choose your skill:")
        dnd_class_instance.ranger_skill()
    
    if (class_choice == "Rogue"):
        print("You chose the Rogue Class!")
        dnd_class_instance.rogue_prof()
        print("Now you will choose your skill:")
        dnd_class_instance.rogue_skill()
    
    if (class_choice == "Sorcerer"):
        print("You chose the Sorcerer Class!")
        dnd_class_instance.sorcerer_prof()
        print("Now you will choose your skill:")
        dnd_class_instance.sorcerer_skill()

    if (class_choice == "Warlock"):
        print("You chose the Warlock Class!")
        dnd_class_instance.warlock_prof()
        print("Now you will choose your skill:")
        dnd_class_instance.warlock_skill()
    
    if (class_choice == "Wizard"):
        print("You chose the Wizard Class!")
        dnd_class_instance.wizard_prof()
        print("Now you will choose your skill:")
        dnd_class_instance.wizard_skill()

    print("Moving on to picking your race...")
    Race.show_races()

    race_instance = Race(None)
    chosen_race_name = race_instance.choose().title() #ChatGPT to help with instance
    
    if (chosen_race_name == "Dwarf"):
        race_instance.dwarf_type()

    if (chosen_race_name == "Elf"):
        race_instance.elf_type()

    if (chosen_race_name == "Halfling"):
        race_instance.halfling_type()

    print("Moving on to your character's traits...")
    print()

    Trait.show_traits()
    print()
    Trait.show_trait_bonuses()
    print()
    Trait.show_primary_abilities()
    print()

    trait_instance = Trait(None) #ChatGPT to help with instance

    Trait.roll_dice()

    trait_instance.print_class_choice(class_choice)
    print()
    print("Fantastic! Lets now add your bonus points!")
    trait_instance.print_race_choice(chosen_race_name)
    print()


    print("Great! These are your final points")
    print(Trait.abilities_points)


if __name__ == "__main__":
    main()