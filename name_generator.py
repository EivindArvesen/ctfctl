#!/usr/bin/env python2

"""
WORK IN PROGRESS
"""

import sys

from random import choice

left_side = [
'armored',
'smart',
'childish',
'bespectacled',
'flying',
'unbuttoned',
'unhinged',
'deranged',
'proper',
'drowning',
'hopeless',
'chaotic',
'grilled',
'resident',
'evil',
'cursed',
'dank',
'defenestraded',
'petrified',
'cooky',
'undead',
'lollygagging',
'tweeting',
'classic',
'curious',
'boring',
'stoic',
'vibing',
'public',
'righteous',
'cool',
'dodgy',
'groovy',
'excellent',
'variable',
'drooling',
'weird',
'bumbling',
'laughing',
'corporate',
'enterprise',
'pretentious'
]

right_side = [
'idiot',
'genius',
'saint',
'clown',
'biker',
'guru',
'millionaire',
'superhero',
'fish',
'goblin',
'gnome',
'troll',
'nyancat',
'unicorn',
'afficionado',
'cheesemonger',
'dungeonmaster',
'npc',
'demon',
'techbro',
'containerista',
'vegetable',
'cosmopolitan',
'neophyte',
'chatbot',
'teenager',
'hacker',
'zombie',
'cybershark',
'codemonkey',
'hipster'
]

results =  []

try:
    number = int(sys.argv[1])
except Exception as e:
    #raise e
    number = 1

while len(results) < number:
    combination = (choice(left_side), choice(right_side))
    result = '-'.join(combination)

    results.append(result)
    results = list(set(results)) # Get unique entries

for result in results:
    print result
