import re
import sys

class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

class Recipe:
    def __init__(self, amounts):
        self.amounts = amounts
        self.calculateScore()

    def calculateScore(self):
        capacity_score = 0
        durability_score = 0
        flavor_score = 0
        texture_score = 0

        for index, amount in enumerate(self.amounts):
            capacity_score += (amount * ingredients[index].capacity)
            durability_score += (amount * ingredients[index].durability)
            flavor_score += (amount * ingredients[index].flavor)
            texture_score += (amount * ingredients[index].texture)

        if capacity_score < 0:
            capacity_score = 0
        if durability_score < 0:
            durability_score = 0
        if flavor_score < 0:
            flavor_score = 0
        if texture_score < 0:
            texture_score = 0

        total_score = (capacity_score * durability_score * flavor_score * texture_score)

        self.score = total_score


instruction_pattern = re.compile(r'^([A-Z][a-z]+): capacity (-?[0-9]+), durability (-?[0-9]+), flavor (-?[0-9]+), texture (-?[0-9]+), calories ([0-9]+)')

ingredients = []
for line in sys.stdin:
    results = re.match(instruction_pattern, line)

    name = results.group(1)
    capacity = int(results.group(2))
    durability = int(results.group(3))
    flavor = int(results.group(4))
    texture = int(results.group(5))
    calories = int(results.group(6))

    ingredients.append(Ingredient(name, capacity, durability, flavor, texture, calories))

def add_to_column(amts, index, total):
    if amts[index] == total - sum(amts[:index]):
        add_to_column(amts, index - 1, total)
        amts[index] = 0
    else:
        amts[index] += 1

def SummingGenerator(k=4, total=100):
    #k >= 2
    output = [0] * (k - 1)
    output.append(total - sum(output))

    while output[0] < total:
        yield output[:]

        if output[-1] == 0:
            add_to_column(output, -2, total)
            output[-1] = total - sum(output[:-1])
        else:
            output[-1] -= 1
            add_to_column(output, -2, total)

    yield output[:]
       
recipes = []
myRecipeGenerator = SummingGenerator()
for combination in myRecipeGenerator:
    recipes.append(Recipe(combination))

scores = [(recipe.score, recipe.amounts) for recipe in recipes]

scores = sorted(scores, key=lambda item: item[0])
print(scores[-1])
