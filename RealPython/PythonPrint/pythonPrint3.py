##################################################
# Printing with Style
##################################################

from pprint import pprint as pp
print(print)

print("pprint calls __repr__ by default rather than str()")
print()
print("""The difference starts to become clear when you give it different.
datestructures""")

data = {'powers': [x**10 for x in range(10)]}
pp(data)

# An example of a deeply nested heirachy being formatted
print()
cities = {'USA': {'Texas': {'Dallas': ['Irving']}}}
pp(cities,depth=3)

# Recursive data structures are normally represented with elipses
x = [1, 2, 3] 
x.append(x)
print(x)
print()
pp(x)
id(x)
print("The last item in the list is the same object as the entire list.")

##################################################
# How to correctly serialize a dictionary to JSON
##################################################
import json
data = {'username': 'jdoe', 'password': 's3cret'}
ugly = json.dumps(data)
pretty = json.dumps(data, indent=4, sort_keys=True)
print("Ugly \n", ugly)
print("Pretty \n", pretty)
