import os
"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Aaron  Williams
Date: 10-26-25

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    stats = calculate_stats(character_class, level=1)
    dict =  {"name": name, "class": character_class, "level": 1, "strength": stats[0], "magic": stats[1], "health": stats[2], "gold": 33}
    return dict
    
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
# I used AI to help fix bugs specfically with my calculate_stats and character_creation functions
def calculate_stats(character_class, level = 1):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    if character_class == "Warrior":
        strength = 100
        magic = 7
        health = 350
        gold = 30
        return (strength, magic, health)
    elif character_class == "Mage":
        strength = 65
        magic = 15
        health = 200
        gold = 70
        return (strength, magic, health)
    elif character_class == "Rogue":
        strength = 40
        magic = 35
        health = 100
        gold = 95
        return (strength, magic, health)
    elif character_class == "Cleric":
        strength = 70
        magic = 21
        health = 50
        gold = 120
        return (strength, magic, health)
    else:
        return(2,2,2)
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
#AI assisted me in building this function's code
def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    with open(filename, "w") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}")
        file.close()
        file = open(filename,"r")
        character = file.readline()
        file.close()
        if character.strip():
            return True
        else:
            return False
    
    # TODO: Implement this function
    # Remember to handle file errors gracefully
#AI assisted me in building this function's code
def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # with open(filename, "r") as file:
    #     text = file.readlines()
    #     return text
    if not os.path.exists(filename):
        return None
    with open(filename, "r") as file:
        text = file.readlines()
        
        person = {}
        for line in text:
            if ":" in line:
                broken = line.strip().split(":", 1)
                key = broken[0].strip().lower()
                value = broken[1].strip()
                if key == "character name":
                    person["name"] = value
                elif key == "class":
                     person["class"] = value
                elif key in ["level","strength","magic", "health", "gold"]:
                    person[key] = int(value)
                    
    keys = ["name", "class", "strength", "level", "magic", "health", "gold" ]
    for key in keys:
        if key not in person:
            return None
    return person
    
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    player = create_character("Bobby", "Support")
    # dictionary = input()
    # if dictionary != "player":
    #     print("FileNotFoundError")
    # print(player)
    # for i in range(len(player)):
    for i in player:
        character_info = save_character(dictionary, "Character_Log2.txt")
        print(f"{i} {player[i]}")

    # load = load_character("Character_Log2.txt")
    # for i in load:
    #     print(i.strip())
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
