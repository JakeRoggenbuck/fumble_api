from pymongo import MongoClient


fumble_data = [
    {"short": "melee", "type": "melee critical fumbles", "roll": (1, 2), "label": "Weapon Break", "desc": "The force of your blow, or parrying that of your opponent’s, causes your weapon to snap in two. (For magical weapons roll an additional d10, on a 1 they break)."},
    {"short": "melee", "type": "melee critical fumbles", "roll": (3, 4), "label": "Goodbye Fair Blade!", "desc": "Roll an Strength / Athletics check DC 15, or your weapon flies d12 feet out of your hand in a random direction. If you have any movement and a bonus action left you can go and pick it up. In doing so you provoke an opportunity attack from anyone in the area, starting with your most immediate opponent. (Otherwise you could simply draw a second weapon, if you have one, using a bonus action)."},
    {"short": "melee", "type": "melee critical fumbles", "roll": (5, 6), "label": "Wild Swing", "desc": "You overextend yourself going for the kill. Your opponent gains advantage on their next attack roll."},
    {"short": "melee", "type": "melee critical fumbles", "roll": (7), "label": "Stuck Weapon", "desc": "Your weapon gets stuck in your opponent’s shield, armour, hide, or else in a tree or wall, or the ground. Roll a Strength check to see if you can free it using a bonus action. The DC is 8 + your strength modifier. "},
    {"short": "melee", "type": "melee critical fumbles", "roll": (8), "label": "Ooops!", "desc": "You hit an unintended foe in combat. Randomise all combatants within 5 feet and roll a second attack roll, if you beat their armour class roll damage as if they were your intended target. (Discount sneak attack damage for Rogues)."},
    {"short": "melee", "type": "melee critical fumbles", "roll": (9), "label": "Self Inflicted wound", "desc": "You manage to slice yourself with your own blade, roll normal damage and half it. (Applies to combatants using slashing weapons and flails only. Other weapon types roll again. Discount sneak attack damage for Rogues)."},
    {"short": "melee", "type": "melee critical fumbles", "roll": (10, 11, 12, 13, 14), "label": "Slip Up", "desc": "You lose your footing. Roll Dexterity / Acrobatics check (DC15) or fall prone. Your turn has ended and melee attacks have advantage on you (see p292 of PH for conditions of being prone)."},
    {"short": "melee", "type": "melee critical fumbles", "roll": (15), "label": "Pulled Muscle (Arms)", "desc": "Roll a Constitution Saving Throw DC15 or the strain of your attack causes you to pull a muscle in your upper body. You have disadvantage in attack rolls and ability checks requiring upper body strength until you have completed three long rests, or received magical healing."},
    {"short": "melee", "type": "melee critical fumbles", "roll": (16), "label": "Pulled Muscle (Legs)", "desc": "Roll a Constitution Saving Throw DC15 or the strain of combat causes you to pull a muscle in your leg. Your movement is halved, and you lose your dex modifier to AC and initiative, and you have disadvantage on any ability checks that require lower body strength, until you have completed three long rests, or received magical healing."},
    {"short": "melee", "type": "melee critical fumbles", "roll": (17, 18), "label": "Loss of Nerve", "desc": "Man your opponent looks tough. Make a Wisdom Saving Throw with a base DC of 10 modified by +2 for every hit dice higher than you your opponent has (or -2 for every hit dice less). On a fail you are frightened (see p292 of Player’s Handbook). After one turn you can attempt the saving throw again."},
    {"short": "melee", "type": "melee critical fumbles", "roll": (19), "label": "Broken Item", "desc": "In the hurly burly of combat, something fragile – like a magic potion – you’re carrying breaks. Randomise fragile objects you have in your possession and roll to determine which. (Note, better to do this when the combat is over)."},
    {"short": "melee", "type": "melee critical fumbles", "roll": (20), "label": "A Little Accident", "desc": "Either through fear, excitement or simply needing to go, you soil yourself. 75 percent chance it’s only pee."},

    {"short": "shooting", "type": "shooting range critical misses", "roll": (1, 2), "label": "Weapon Break", "desc": "Your bow shaft or a mechanism in your crossbow breaks and is now useless. (For magical weapons roll an additional d10, on a 1 they break)."},
    {"short": "shooting", "type": "shooting range critical misses", "roll": (3, 4, 5), "label": "String Break", "desc": "Your bowstring snaps. Assuming you have a spare string, it requires 1 minute to replace it."},
    {"short": "shooting", "type": "shooting range critical misses", "roll": (6, 7, 8), "label": "Loose String", "desc": "Your string comes loose. You lose this attack. Starting next turn you can make a sleight of hand check DC15 to fix it. Each attempt takes one turn."},
    {"short": "shooting", "type": "shooting range critical misses", "roll": (9, 10, 11, 12, 13, 14, 15, 16), "label": "Ooops!", "desc": "You hit an unintended random target. Randomise all combatants within 10 feet (for a short range attack, or 30 feet for a long range attack) and roll a second attack roll, if you beat their armour class roll damage as if they were your intended target (discount sneak attack damage for Rogues)."},
    {"short": "shooting", "type": "shooting range critical misses", "roll": (17, 18), "label": "Ammo Accident", "desc": "Your quiver spills (50 percent strap broken, 50 percent you tilt it over by accident), and the remainder of your arrows / bolts fall to the floor. If you remain still you can use a bonus action to pick up one a round and still fire using your action. Otherwise you can use an action to pick up 2d8 and put them back in your quiver."},
    {"short": "shooting", "type": "shooting range critical misses", "roll": (19), "label": "Pulled Muscle (Upper Body)", "desc": "Roll a Constitution Saving Throw DC15 or the strain of your attack causes you to pull a muscle in your upper body. You have disadvantage in attack rolls and ability checks requiring upper body strength until you have completed three long rests, or received magical healing."},
    {"short": "shooting", "type": "shooting range critical misses", "roll": (20), "label": "Slip Up", "desc": "You lose your footing. Roll Dexterity / Acrobatics (DC15) or fall prone. Your turn has ended and melee attacks have advantage on you (see p292 of PH for conditions of being prone)."},
]


def setup_db():
    db = lambda x: x
    db.client = MongoClient()
    db.database = db.client["fumble_api"]
    db.critical_collection = db.database["critical_collection"]
    return db


def clear_data():
    db = setup_db()
    confirm = input("Drop critical_collection? [Y/n]: ")
    if confirm.upper() == "Y":
        db.database.drop_collection("critical_collection")
        print("Dropped critical_collection")
    else:
        print("critical_collection not dropped")


def upload_data(documents):
    db = setup_db()
    db.critical_collection.insert_many(documents)
