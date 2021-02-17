if False:
    my_list = ['someone', 'should', 'have', 'checked', 'obs', 'before', 'he', 'talked', 'to', 'himself']
    # for each loop
    for word in my_list:
        if word[0] == 's':
            print(word)

    # 2-d array, basically operating like that
    print(my_list[0][0])

    # for i loop
    for i in range(len(my_list)):
        if my_list[i][0] == 's':
            print(my_list[i])

    list_of_things = []
    for i in range(5):
        list_of_things.append(input('Tell me a thing: '))

    print(list_of_things)

    for word in list_of_things:
        # supposedly we modified the list here
        word = 'happy'
        # it doesn't change the list.
        # well how do we change the list?

    # it didn't modify
    print(list_of_things)


    for i in range(len(list_of_things)):
        # supposedly we modified the list here
        list_of_things[i] = 'happy'
        # it doesn't change the list.
        # well how do we change the list?

    # will it work?
    print(list_of_things)

    """
        Moral of the story:
            If you need to modify elements, clearly you can't do that with a for each loop
            but you can do that with a for i loop.  
            
            For each loops make copies of "immutable objects" (int, float, bool, string)
            
            For i loops access a list at a particular place and allow assignment.
    """

    # my_string = 'happy'
    # my_string[3] = 'z' <-- error because it tries to modify an unmodifiable type
    # print(my_string)

    x = int(input('What is the maximum integer you want in your list? '))
    # if you want to make a list of integers from 1 to x
    # range(start=0, stop, step=1)
    my_int_list = list(range(1, x + 1))
    print(my_int_list)
    # this is how you take an "iterable" object and cast it to a list.
    # you can't cast ints, floats, bools to lists
    # I left one out... strings
    # YOU CAN CAST STRINGS INTO LISTS
    my_string = 'here is a string that is normally immutable'
    new_list = list(my_string)
    print(my_string, new_list)
    # split the string into its individual characters. nice.
    new_list[3] = '[this is a new string we are going to put into position 3]'

    print(new_list)
    # join will add all strings in a list together into one string, separated by the character/string that you have first.
    print(''.join(new_list))

# remove from a list
"""
    Either you can remove by index OR you remove by element.  
    
    Removing by element means that you're going to remove an element with a specific value
"""

test_list = [1, 2, 4, 9, 2, 13, 21, 2, 1679, 77]
print(test_list)
test_list.remove(21)
print(test_list)
# test_list.remove(91)

"""
Notice here two things happened:
    1) the error occurs after the print statements
    2) the error occurs sometime in the middle of the print statements
    3) the error occurs "entirely before" the line of code that removes
    
    What is happening here?
        It doesn't know that the error is going to occur.
        There is stdout (the standard output stream that print writes to/input)
        There is also stderr (a separate stream that is provided by the OS)
            They aren't synchronized.  
        Generally stdout is slightly slower than stderr.  
"""

# if you know the index you can always just do this:
test_list.remove(test_list[2])
print(test_list)

# removing by ELEMENT
test_list.remove(2)
print(test_list)
# it didn't remove all the twos, it removed exactly the first 2 it found.

x = int(input('Tell me x to remove'))

# in keyword is basically the same as this for loop

found = False
for element in test_list:
    if element == x:
        found = True
print(found)

# set notation epsilon symbol that means "is an element of"
if x in test_list:
    test_list.remove(x)
    print(test_list)
else:
    print(x, 'was not in the list, but we caught the error for you')

print(test_list)
for y in test_list:
    if y == x:
        test_list.remove(x)

print(test_list)


grid_size = int(input('how big the grid?'))
for i in range(grid_size):
    for j in range(grid_size * 3):
        print('({}, {})'.format(i, j), end=" ")
    print()

grid_width = int(input('grid width?'))
grid_height = int(input('grid height?'))
for i in range(grid_height):
    for j in range(grid_width):
        print('a', end=" ")
    print()
"""
    Answer: grids are the way to think about 2-d lists when we get to 2d-lists
        like right now
"""

my_string_grid = ['hello', 'robot', 'happy', 'would', 'fluff', 'five!', 'words']

for i in range(len(my_string_grid)):
    for j in range(len(my_string_grid[i])):
        if my_string_grid[i][j] in ['a', 'e', 'i', 'o', 'u', 'y']:
            print(' ', end=" ")
        else:
            print(my_string_grid[i][j], end=" ")
    # this is to print out the endline at the end of each row
    print()

# cheese:
print(
"""
   *
  * *
 *****
*     *
""")

"""
    Aside:
        Starting on HW3
        Nothing to do with for loops.  201
        
        NOT ON HW2
    if __name__ == '__main__':
"""

# imports are currently forbidden so dont' worry about them yet
import ifnamemain

# if you use multiple files rather than just one file
print(__name__)
if __name__ == '__main__':
    print('hello there main block')

"""
    Entry point, this is the file that we clicked "run" on.  We didn't click run on the ifnamemain.  
    
    changes the name of whatever the main entry-point file is to '__main__'
"""

# Let's talk about tuples.
# tuples are basically lists - we don't really require tuples in this class
new_tuple = ('a', 'b', 'c', 'd')
for x in new_tuple:
    print(x)
# what is the difference then? you definitely believe that a list and a tuple are basically the same.
# the only difference is you can't modify tuples.
# new_tuple[1] = 'z'
# TypeError: 'tuple' object does not support item assignment
# the same error that we got with strings.
# strings were immutable <-- cannot be changed
# tuples are immutable lists.
print(new_tuple)
