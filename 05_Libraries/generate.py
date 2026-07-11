"""
import random
coin = random.choice(["Heads", "Tails"])
print(coin)
"""
"""
from random import choice
coin = choice(["Heads", "Tails"]) # to choose b/w heads and tails
print(coin)
"""
"""
import random
number = random.randint(1, 10) # choose a number b/w 1 to 10
print(number)
"""
import random
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
