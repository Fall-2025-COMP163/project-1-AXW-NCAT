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
    dict =  {"Name": name, "class": character_class, "level": 1, "strength": stats[0], "magic": stats[1], "health": stats[2], "gold": stats[3]}
    return dict
    
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    pass

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    if character_class == "Atttacker":
        strenght = 100
        magic = 5
        health = 350
        gold = 30
        return (strenght, magic, health, gold)
    if character_class == "Support":
        strength = 65
        magic = 15
        health = 200
        gold = 70
        return (strenght, magic, health, gold)
    if character_class == "Medic":
        strength = 40
        magic = 35
        health = 100
        gold = 95
        return (strenght, magic, health, gold)
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    pass

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
    filename = open(filename,"w")
    filename.write(f"Character Name: {character}\n"
    f"Class: {Character_class}\n" 
    f"Level: {level}Strength: {strenght}\n" 
    f"Magic: {magic}\n"
    f"Health: {health}\n"
    f"Gold: {gold}")
    filename.close()
    filename= open(filename,"r")
    character = filename.readlines()
    return character
    
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    pass

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
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
    print(create_character("Bobby", "Support"))
    
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
