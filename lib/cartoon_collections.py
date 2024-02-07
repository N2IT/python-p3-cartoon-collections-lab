def roll_call_dwarves(dwarves):
    i = 1
    for dwarf in dwarves:
        print(f'{i}. {dwarf}')
        i += 1

# roll_call_dwarves(['Dopey', 'Grumpy', 'Bashful'])

def summon_captain_planet(calls):
    # returns a list with the same number it was given
    return [ c.capitalize() + "!" for c in calls ]

# summon_captain_planet(["axe", "earth", "wind", "fire"])

def long_planeteer_calls(words):
    # if any word in words is > 4 characters then return true else false
    # check each word for len(word).  If ANY word is > 4 ? true : false
    # return [true for word in words if len(word) > 4] 
    has_long_string = False
    for word in words:
        if len(word) > 4:
            has_long_string = True
    return has_long_string

# long_planeteer_calls(['wind', 'fire', 'tree', 'axe', 'code'])

def find_the_cheese(snacks):
    cheeses = ['cheddar', 'gouda', 'camembert']
    cheesy_snack = "".join([ snack for snack in snacks if snack == cheeses[0] or snack == cheeses[1] or snack == cheeses[2] ])
    if cheesy_snack:
        return cheesy_snack
    else:
        return None


# snacks = ["crackers", "false", "thyme"]
# find_the_cheese(snacks)
# #=> "gouda"

# soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
# find_the_cheese(soup)     

    # iterate the list of strings
    # identify the first occurence of a cheese
    # cheese is identified as 'cheddar', 'gouda', or 'camembert'
    # if a cheese is present in the list of strings return the first occurence of cheese
    # If it does not exist return None