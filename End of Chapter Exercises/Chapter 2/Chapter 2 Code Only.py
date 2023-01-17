#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 13:12:41 2023

@author: alex
"""
"""
This chapter covers the basics of base Python programming including:
    Comments
    Variables
    Types
    Bools
    If Statements
    Lists
    Dicts
    Loops
    Comprehensions
    Functions
    etc.
    
Along with how each of those items can be used and methods of opperating on
them. This chapter also touches breifly on Librairies and that they will be
used more in later chapters.

Most of the exercieses in this chapter seem to attempt to ensure the reader 
grasps the basics of Python that will be built upon throughout the rest of the
book.
"""

# 2.1 Which of the following are valid Python variable names?

    # a) _throwaway_data
"""
        This is a valid variable name, the book mentions variable names with 
        an underscore are often used for short-term variables that will be 
        thrown away
        """
    # b) n_of_hrs
"""
        This is a valid variable name.
        """
    # c) 2nd_base_name
"""
        This is not a valid variable name as variable names cannot begin with
        a number.
        """
    # d) grandSlam
"""
        This is a valid variable name.
        """
    # e) strike3
"""
        This is a valid variable name, the names can contain numbers as long
        as they do not start with the number.
        """
    # f) starting pitcher
"""
        This is not a valid name as variable names cannot contain spaces.
        """
    # g) @home_or_away
"""
        This is not a valid variable name as the only symbol allowed to be 
        used in a variable name is an underscore.
        """
    # h) 'value_over_replacement'
"""
        This is not a valid variable name as it is a string, which cannot be
        a variable name.
        """
        
# 2.2 What is the value of runs at the end of the following code?

runs = 0
runs = runs + 2
runs = runs + 5

"""
    The value of runs at the end of this code will be 7, the value is initially
    0, then it has the value of 2, then 5 added to it. 2 + 5 = 7
    """

# 2.3 Write a function named announce_pitch that takes in the name of a player
#     and a pitch (e.g. 'Kershaw', 'slider') and returns a string of the form:
#     'Kershaw with the slider!'.

def announce_pitch(player, pitch):
    """
    Parameters
    ----------
    player : string
        Name of the pitcher.
    pitch : string
        Type of pitch.

    Returns
    -------
    announcement : string
        A string announcing the pitcher and pitch thrown.

    """
    
    assert isinstance(player, str), "Player names only!"
    assert isinstance(pitch, str), "Pitch names only!"
    player = player.title()
    pitch = pitch.lower()
    return f"{player} with the {pitch}!"

# 2.4 Without looking it up, what do you think the string method islower does?
#     What type of value does it return? Write some code to test your guess.

    """
    It will check if a string is lower-case and will return a boolean
    True / False if it is / isn't.
    
    """

prob4a = "lower"
prob4b = "Mixed"

prob4a.islower()
prob4b.islower()

# 2.5 Write a function is_travisd that takes in a player name and returns a
#     bool indicating whether the player's name is "Travis d'Arnaud" -
#     regardless of case or whether the user included the '.

def is_travisd(name):
    """
    Parameters
    ----------
    name : str
        Player name.

    Returns
    -------
    isTrav : bool
        True if player name is Travis d'Arnaud.

    """
    assert isinstance(name, str), "Player names only, must be a string!"
    
    return name.lower().replace("'","") == "travis darnaud"

# 2.6 Write a function, commentary, that takes in a batting average (without 
#     the decimal, e.g. 275 or 333) and returns a string '333 is a good ave'
#     if the number is >= 33 or "275's not that good" otherwise.

def commentary(BA : int):
    """
    Parameters
    ----------
    BA : int
        Batting avg without decimal.

    Returns
    -------
    comment : str
        Commentary.

    """
    assert isinstance(BA, int), "BA must be an int!"
    
    if BA >= 300:
        return f"{BA} is a good ave"
    else:
        return f"{BA}'s not that good"

# 2.7 Write a function, commentary_plus , that works like commentary above but
#     can also handle averages passed in decimal form (e.g. 0.275). Note it 
#     should still be able to handle non-decimal (275) too.

def commentary_plus1(BA):
    """
    This implementation handles both float and int numbers by itself.
    
    Parameters
    ----------
    BA : int or float
        batting avg.

    Returns
    -------
    comment : string
        commentary.

    """
    
    if (type(BA) is int and BA >= 300) or (type(BA) is float and BA >= 0.3):
        return f"{BA} is a good ave"
    else:
        return f"{BA}'s not that good"
    
def commentary_plus2(BA):
    """
    This implementation reuses the commentary function from the previous
    exercise for int values.

    Parameters
    ----------
    BA : int or float
        batting avg.

    Returns
    -------
    str
        commentary.

    """
    
    if type(BA) is int:
        return commentary(BA)
    elif BA >= .300:
        return f"{BA} is a good ave"
    else:
        return f"{BA}'s not that good"

# 2.8 Say we have a list:
    
dodgers_roster = ['clayton kershaw', 'cody bellinger', 'mookie betts']
    
#     List at least three ways you can to print the list without 'mookie betts'.
#     Use at least one comprehension.

print(dodgers_roster[:2])
print(dodgers_roster[:-1])
print([x for x in dodgers_roster if x != 'mookie betts'])

# 2.9 Say we have a dict:
    
pitcher_info = {'starter' : 'Kershaw', 'throws_right' : False}
    
# a) How would you change 'starter' to 'Joe Kelly'?

pitcher_info['starter'] = 'Joe Kelly'

# b) Write a function, toggle_throws , that takes pitcher_info , turns 
#    'throws_right' to the opposite of whatever it is, and returns the updated
#    settings dict.

def toggle_throws(pitcher_dict):
    
    pitcher_dict['throws_right'] = not pitcher_dict['throws_right']
    return pitcher_dict

# 2.10 Assuming we've defined our same dict:
    
pitcher_info = {'starter' : 'Kershaw', 'throws_right' : False}

#      Go through each line and say whether it'll work without error.

# a) pitcher_info['era']
"""
    No, there is no 'era' key defined in this dict.
    """
# b) pitcher_info[starter]
"""
    No, the value starter should be in quotes 'starter'.
    """
# c) pitcher_info['age'] = 32
"""
    Yes, this will create a new key / value entry in the dict of {'age' : 32}.
    """

# 2.11 Say we're looking at the list:
    
my_roster_list = ['clayton kershaw', 'mookie betts', 'cody bellinger']
    
# a) Write a loop that goes through and prints the last name of every player
#    in my_roster_list .

for i in my_roster_list:
    print(i.rsplit()[1])

# b) Write a comprehension that ues m_roster_list to make a dict where the 
#    keys are the player names and the values are the lenghts of the strings.

{player : len(player) for player in my_roster_list}

# 2.12 Say we're working with the dict:
    
my_roster_dict = {'p' : 'clayton kershaw',
                  'rf' : 'mookie betts',
                  '1b' : 'cody bellinger'}

# a) Write a comprehension that turns my_roster_dict into a list of just the
#    positions.

[position for position in my_roster_dict]

# b) Write a comprehension that turns my_roster_dict into a list of just
#    players whose last names start with 'b'.

[player for _, player in my_roster_dict.items()
     if player.split(' ')[-1][0] == 'b']

# 2.13 
#
# a) Write a function, mapper , that takes a list and a fucntion, applies the
#    function to every item in the list and returns it.

def mapper(l, f):
    
    return [f(x) for x in l]

# b) Assuming a 300 batting average, use mapper with an anonymous function to
#    get an expected hits from the following number of at bats. Use the round
#    function so your projections are even numbers.

list_of_atbats = [500, 410, 618, 288, 236]

mapper(list_of_atbats, lambda x : int(x*.300))

