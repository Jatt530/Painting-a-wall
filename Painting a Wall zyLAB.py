import math

# Dictionary of paint colors and cost per gallon
paintColors = {
   'red': 15,
   'blue': 18,
   'green': 22
}

# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
wallHeight = float(input('''Enter wall height (feet):
'''))
wallWidth = float(input('''Enter wall width (feet):
'''))
wallArea= wallHeight * wallWidth
print('Wall area:',int(wallArea), 'square feet')
   
# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
paintNeeded=  wallArea/350
print('Paint needed:', '%.6f' %paintNeeded, 'gallons')

# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
cansNeeded = math.ceil(paintNeeded)
print('Cans needed:', cansNeeded, '''can(s)
''')

# FIXME (4): Calculate and output the total cost of paint can needed depending on color
pickColor = input('''Choose a color to paint the wall:
''')
cost = cansNeeded * paintColors[pickColor]
print(f"Cost of purchasing {pickColor} paint: ${cost}")

# FIXME (5): Calculate and output the other supplies needed.
scaffoldPrice= cost + 30
dropClothCalc= int(wallWidth * 2 + cost)
if wallHeight > 20:
    print(f"Scaffold rental needed at $30. Total cost: ${scaffoldPrice}")
if wallHeight > 30:
    print(f"Fall protection needed at $20. Total cost: ${scaffoldPrice +20}")
if wallHeight < 20:
    print(f"Drop cloth needed at $2 per foot. Total cost: ${dropClothCalc}")
if wallHeight > 30 and wallArea > 500:
        print(f"Spray gun needed at $50. Total cost: ${scaffoldPrice+50+20}")
