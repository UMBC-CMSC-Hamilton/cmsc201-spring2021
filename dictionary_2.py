"""
    Dictionaries:
        What is a dictionary?

        Like a list in this one sense: it stores multiple pieces of information.
        Unlike a list:
            indices are not ordered 0 -> len(list) - 1
            "indices == keys"
            keys can be anything that is immutable (bool, int, float, str, datetime, etc)
                keys cannot be mutable (lists, dictionaries, classes usually, etc)
            values can be anything.
        What are the keys?
            keys are put into the [key] brackets.

        "a data structure" - a way to organize data
        Underlying name of the structure : Hash Table

"""

# curly braces are for the definition of the dictionary
my_words = {'rabbit': 7, 'fox': 2, 'bear': 13, 'gremlin': 299}
# {key: value, key: value, key: value}
# access values using the keys
# accessing uses [] for lists and dictionaries.
print(my_words['fox'])
print(my_words['rabbit'])
print(my_words['gremlin'])

# remember that stderr and stdout aren't synchronized
# print(my_words['horse'])
# two ways to avoid the key error
# .get(key, default_value)
print(my_words.get('horse', 0))
# slight "philosophical" problem with this: what if 'horse': 0 could you tell the difference? technically no
# unless 0 is not possible as a value

if 'horse' in my_words:
    print(my_words['horse'])
else:
    print('horse is not in the dictionary but this isn\'t a KeyError')

print(my_words)

# here's how to add things to the dictionary (assign them for the first time)
my_words['cow'] = 17
my_words['chicken'] = 3
print(my_words)

# remove chicken
del my_words['chicken']
print(my_words)

for animal in ['turtle', 'hawk', 'pigeon', 'salmon', 'wolverine']:
    # works kind of like append
    my_words[animal] = len(animal)

print(my_words)

"""
Inverse problem:
    Given a value, can we find a key that matches?
"""

# in a dictionary it only ever searches the keys never the values.
print(my_words.get(17))  # gives None
# how would you do this then?  find a key who has value 17, 3, 6 whatever

test_value = 6
for key in my_words:
    if my_words[key] == test_value:
        print(key, my_words[key])

# a key is unique
my_words['rabbit'] = 14
# does this create a new value in the dictionary? or does it overwrite 7?... overwrites
print(my_words)
# if you modify something at a certain key which already exists in the dictionary, then it'll modify the value
# if you add a key then it creates (only the first time per key).
three_dict = {'a': 3, 'b': 3, 'c': 3, 'd': 3}
print(three_dict)

grades_dict = {'Eric': [], 'Sammie': [], 'Brian': [], 'Ben': []}
# this is a list
print(grades_dict['Eric'])
grades_dict['Eric'].append(47)
for i in range(10):
    grades_dict['Eric'].append(i)
print(grades_dict['Eric'])

grades_dict['Sammie'].append(99)
grades_dict['Sammie'].append(95)
print(grades_dict)
# 2d "thing" where you have a dictionary of lists
# you can also have lists of dictionaries
# all kinds of things are possible.
dict_of_dict = {}
# create 'robot' and 'people' keys
dict_of_dict['robot'] = {'turducken': 'yuck', 'the robot from lost in space': 'danger will robinson', 'bender': 'bender is great'}
dict_of_dict['people'] = {'Abe Lincoln': 'Four score and seven years ago', 'George Washington': "I never tell a lie", 'Nixon': "I am not a crook"}
# access it
print(dict_of_dict)
print(dict_of_dict['people']['Abe Lincoln'])
print(dict_of_dict['robot']['bender'])

non_type_dict = {'hello': 3, 'goodbye': None, 'peace': 'peace out yall', 'else': [1, 2, 3]}
print(non_type_dict)
# don't generally do this.
# basically gives you a list of the keys / values
my_words.keys()
my_words.values()
# rare you need these

# keys are the id's
for key in non_type_dict:
    print(key)
    # to access the value, you need
    print(non_type_dict[key])
