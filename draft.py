import random
with open('food.txt', encoding='utf-8') as file:
    food = [item.split('\n') for item in file]
