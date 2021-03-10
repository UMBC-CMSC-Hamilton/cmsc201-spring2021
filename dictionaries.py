"""
    * don't use dictionaries on the exam.  I don't think they'll help anyway, but don't use them.

    What is a dictionary?
        HashTable, HashMap, Hash, Hash <-- most languages will say Hash.
        Secretly it's a big list.

        But for us, to the end user programmer person, it looks kind of like a map - mathematical sense
"""

our_first_empty_dictionary = {}  # curly braces
# empty
our_first_dictionary = {'Eric': 17, 'Bender': 31, 'Fry': 22, 'Zoidberg': 99}
print(our_first_dictionary)
"""
    Key - Value Pairs
    
    Dictionary is accessed via "keys" and when you do that it gives you back a value
    Just in this example it's string (keys): int(values)
    
    Keys always come before the values in the {} declaration
"""
print(our_first_dictionary['Eric'])
print(our_first_dictionary['Fry'])
print(our_first_dictionary['Zoidberg'])
# basically a list, but not 100% entirely quite a list.
# not going to use these much.  It's ok but probably not the real reason you're using dictionaries.
print(our_first_dictionary.keys())
print(our_first_dictionary.values())
# keys and values can be any type, except that the keys must be IMMUTABLE (under the python definition)
#   str, int, bool, float, tuples, datetime object, etc.
# NO LISTS AS KEYS
# LISTS CAN BE VALUES
number_dictionary = {3: 15, 4: 17, 22: 31, 81: 5}
number_dictionary[3] = 21
print(number_dictionary)

# unhashable type!?! the type WAS mutable, so bad.
"""
a_list = [1, 2]
weird_thing = {a_list: 'hello there'}
a_list.append(3)
"""
# cannot modify the key's value,
# you can modify the value's value.

phone_book = {1233355: 'EricTheProf', 911: 'Emergency', 2233232: "Sam", 8675309: 'Who is this again? I Forget'}
# new person!
# Jill now has phone number 345-6789
# print(phone_book[3456789]) key error
phone_book[3456789] = 'Jill'
# adding something to a dictionary means that you just assign it.
print(phone_book)
# dictionaries/python can tell the difference between assignment and access
#   don't access it before you've assigned it, that gives key errors
#   phone_book['3456789'] also key error

# dictionaries aren't like lists, don't have a preferred order.
# same thing with the iteration question...
for phone_number in phone_book:
    print(phone_number)
# only the keys print out

# next question is, but wait, how do I access the value then?!?!?
for phone_number in phone_book:
    # this will give the key and the value
    print(phone_number, phone_book[phone_number])
# this gives both keys and values.

# names aren't really unique, James Smith probably more than one who graduated from UMBC since 1990 possibly.
# names == bad (you wouldn't be able to store both James Smiths.)
# student ID great UID (Unique IDentifier)
# what should the key be?  something unique
student_records = {'AB12345': ['James Smith', 'Computer Science'],
                   'CD22112': ['Will Smith', 'Drama'],
                   'EFG1234': ['John Smith', 'Naval Architect'],
                   'JH94389': ['James Smith', 'Art History']
                   }

print(student_records['EFG1234'])
# how to delete from a dictionary?

# del keyword
del student_records['CD22112']
print(student_records)
# del works on lists, variables

my_favorite_variable = 13
print(my_favorite_variable)
del my_favorite_variable  # most programming langauges DONT have this kind of feature where you can delete a variable
# python does!

student_records['EFG1234'][1] = 'Mechanical Engineering'
print(student_records['EFG1234'])
print(student_records)
