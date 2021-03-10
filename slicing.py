example = 'abcdefg'
print(example[3:6])
print(example[3:7])  # remember that 7 not an index

# print(example[7])

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # 9 elements in the list
# up to but doesn't include the last index.
s = input('Give me two numbers: ')
while s != 'quit' and False:
    split_string = s.split()
    x = int(split_string[0])
    y = int(split_string[1])
    print(my_list[x: y])
    s = input('Give me two numbers: ')


print(my_list[9: 2])  # just to show as an example.
"""
    Why is this an empty list rather than the 2 to 9 reversed, or something else like that maybe?
    
    two argument slice [x : y] this means that x < y because it steps up by size of 1 each.  
    
    there is a three argument slice.  
"""

# slicing examples
test_list = ['hello', 'rabbit', 'flavor', 'pants', 'excellent', 'tomorrow', 'sanguine', 'fortuitous']
# list of strings.

print(test_list[3:6])
# you can do the pig latin problem either with slices or without.
# Technically they're illegal / forbidden, after today they'll be legal.
# totally 100% possible to do just with for loops, if, while

"""
    Hint: how do you search for a substring?
"""
big_block_of_text = 'hello i am a big block of text, find something within me and you will profit'
look_for = 'text'

# play with indices... i == offset, gap of 2
for i in range(len(big_block_of_text)):
    # don't try to force this into your code, it'll not be happy
    if look_for[0] == big_block_of_text[i]:
        print('found t', i)
        if i + 1 < len(big_block_of_text) and look_for[1] == big_block_of_text[i + 1]:
            print('found e', i + 1)
            if i + 2 < len(big_block_of_text) and look_for[2] == big_block_of_text[i + 2]:
                print('found x', i + 2)
                if i + 3 < len(big_block_of_text) and look_for[3] == big_block_of_text[i + 3]:
                    print('found t, and the whole word', i + 3)


big_block_of_text = 'hello i am a big block of taeaxata, find something within me and you will profit'
look_for = 'text'

# play with indices... i == offset, gap of 2
for i in range(len(big_block_of_text)):
    # don't try to force this into your code, it'll not be happy
    if look_for[0] == big_block_of_text[i]:
        print('found t', i)
        if i + 2 < len(big_block_of_text) and look_for[1] == big_block_of_text[i + 2]:
            print('found e', i + 2)
            if i + 4 < len(big_block_of_text) and look_for[2] == big_block_of_text[i + 4]:
                print('found x', i + 4)
                if i + 6 < len(big_block_of_text) and look_for[3] == big_block_of_text[i + 6]:
                    print('found t, and the whole word', i + 6)

"""
    Efficiency isn't important
    Knuth-Morris-Pratt...
    don't even look up any of that... way to complex
    
    Reasonably efficient = it must run in the amount of time it takes for a grader to give up and hit CTRL+X/C
        Under 5 seconds runtime is "ok".  
        
    Now that i've done that bit of code, make it work for multi-length match string.
    Gaps, how do you do those?
        Don't bother with them until you get the string matching working with just offsets/no gaps.    
    
    Don't use slices on this problem.
        isn't that unfair?  yes a little.  most languages don't have them.  
    
    C++ won't have these features.
    Next HW will be with slices maybe theoretically...   
"""

"""
    Slice steps
        third argument, normally a kind of secret (default argument)
        default_step = 1
"""

a_string = 'asdfasdfasdfasdfasdfasdf'
print(a_string)
print(a_string[0:len(a_string): 4])

my_hundred = []
for i in range(100):
    my_hundred.append(i)

# default arguments in slicing
# if you don't fill the first argument in, it gets set to zero.
# if you don't fill the second argument in, it gets set to the len(the string or list)
# if you don't fill in the third argument, it gets set to step = 1
print(my_hundred[0:len(my_hundred):3])
print(my_hundred[0:len(my_hundred):1] == my_hundred[::])

# for now, don't use negative indices, or negative step in slices.
"""
    Rule about teaching slices:  slices end up confusing just about everybody.
        25-50% of the students end up saying "splice" <-- NOOOO
        25-50% of other students end up saying "what is a slice, we never learned that!"
        Slices, it's like I never said anything... 
            Play around with slices.  
            Just a little PSA: don't assume you know it because i knew it in lecture.

    Very Last Thing:
        Slices make copies.  They don't just make references to the old object
"""

my_list = ['a', 'b', 1, 2, 17, 21, 33, 91, 'c']
new_slice = my_list[4:7]
print(new_slice)
new_slice[0] = 25
print(new_slice)
print(my_list)
# slices make copies of lists AND strings (with strings since they're immutable we gotta say a bunch more nonsense).
# if you make a big enough string and you take 100,000 or 1,000,000 slices out of it, you may run out of ram.
# 201 problems you'll never see data that large* (* unless i'm losing my mind or something)
# 341 when you start to see LARGE data. (word i invented just now), "Big Data" - buzzword

# very very last part b part of what i want to say is this:
my_copy_list = list(my_list)  # constructor way
# this will make a copy
my_slice_list = my_list[:]  # the cute way, gimmicky way
# empty slice will also copy a list


