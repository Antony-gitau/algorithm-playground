# Following this MIT Lecture -> https://youtu.be/C1lhuz6pZC0?list=PLUl4u3cNGP619EG1wp0kT-7rDE_Az5TNd 
# with comments of my understanding of the implementation
# greedy algorithm to chose what to eat from a menu contains a variety of food and their calorie value 
# while staying true to your calorie budget of 1000
# this program will help us order the most appropriate combination of food from the menu

class Food(object):
    """

    Define a food class that holds the name, calorie and string representation of the output order
    value will be the numerical representation of the name of the specific food like "apple" can be "90"
    
    """
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'

def buildMenu(names, values, calories):
    """
    
    names, values, calories lists of same length.
       name a list of strings
       values and calories lists of numbers
       returns list of Foods"""
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                          calories[i]))
    return menu

def greedy(items, maxCost, keyFunction):
    """
    Assumes items a list, maxCost >= 0,
    keyFunction maps elements of items to numbers
         
         """
         #sorts the items in descending order 
    itemsCopy = sorted(items, key = keyFunction,
                       reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):

        """
        iterate over all the items on our menu
        if the cost from our selection added to our current choice is less than the total cost which is the max limit,
        then add the new item's cost and its value (which is the numerical representation of the food name) 
        This allows the loop to consider the next item and repeat the process until all items are considered or until the maxCost constraint is violated.
        If adding the current item would exceed the maxCost, the loop simply moves on to the next item without adding it to the result. 
        
        """
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)

def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits,
               lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.density)


names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 1000)
