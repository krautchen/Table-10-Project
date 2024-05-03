# Purpose of each File in Directory
#### `main.py`
- 

#### `charcter.py`
- Contains the class for creating a Character object.

#### `driver.py`
- Selects which map and handles navigating the map.

#### `items.py`
- Contains the class for creating Item objects, including
Weapons, Armor, Consumables, and Bags.

#### `monster.py`
- Contains the class for creating a Monster object, which 
inherits most of its attributes from the Character object.

#### `puzzle.py`
- 

#### `fantasy_items.json`
- A dictionary with four lists of dictionaries for items 

#### `fantasy_monsters.json`
- A dictionary with two lists of dictionaries for monsters

#### `puzzles.json`
- 

#### `rooms.json`
- A dictionary with all of the rooms and valid carindal directions for movement
- Each room may or may not also have items

<br/>
<br/>

# How to run from cli

<br/>
<br/>

# How to use and interpret output

<br/>
<br/>

# Attribution

| Function/method | Primary Author | Techniques |
|----------|----------|----------|
|   argparse/commandline  |   Richard Salters   |   argumentParser   |
|   driver  |   Richard Salters   |   With statement   |
|   puzzle  |   Michelle Akem   |   json.load()   |
|   puzzle  |   Michelle Akem   |   Regex expressions   |
|   bag.organize()  |   Noah Hibbler   |   Lambda key function   |
|   Character class \__init__ |   Noah Hibbler   |   Composition of two classes   |

<br/>
<br/>

# Annotated Bibiolgraphy
- https://www.geeksforgeeks.org/underscore-_-python/ _ used as throwaway variable in the d6 function for loop