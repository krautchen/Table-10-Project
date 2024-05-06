# Purpose of each File in Directory
#### `main.py`
- Contains the overarching Game class, which handles the logic for room interaction, movement, and character state for a Game instance.

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
- Contains the puzzle function, which runs randomly to produce a puzzle for a locked room.

#### `fantasy_items.json`
- A dictionary with four lists of dictionaries for items 

#### `fantasy_monsters.json`
- A dictionary with two lists of dictionaries for monsters

#### `puzzles.json`
- Contains the puzzles for the game with prompt, correct code, and hints.

#### `rooms.json`
- A dictionary with all of the rooms and valid carindal directions for movement
- Each room may or may not also have items

<br/>
<br/>

# How to run from cli
- python(3) main.py fantasy
  or
- python(3) main.py scifi
     - but it's not implemented yet
<br/>
<br/>

# How to use and interpret output
- output runs on user input, so the choices that the program presents and the following response
- provides context for what the user can do next
- for instance, if you want to equip an item before moving into the next room, choosing yes
- will present the item options and choosing no will move you to the next room
<br/>
<br/>

# Attribution

| Function/method | Primary Author | Techniques |
|----------|----------|----------|
|   argparse/commandline  |   Richard Salters   |   argumentParser   |
|   room_description  |   Richard Salters   |   f-strings   |
|   Map class \__init__  |   Richard Salters   |   json.load()   |
|   puzzle  |   Michelle Akem   |   Regex expressions   |
|   bag.organize()  |   Noah Hibbler   |   Lambda key function   |
|   Character class \__init__ |   Noah Hibbler   |   Composition of two classes   |
|   equip   |   Michelle Akem   |    Sequence unpacking   |
|   \__str__ |   Noah Hibbler  |  Magic methods   |
|   has_items   |   Michelle Akem   |   Comprehensions   |
<br/>
<br/>

# Annotated Bibiolgraphy
- https://www.geeksforgeeks.org/underscore-_-python/ _ used as throwaway variable in the d6 function for loop
