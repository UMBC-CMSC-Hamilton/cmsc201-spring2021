"""
    for loops - a way to execute code multiple times.
"""
if False:
    # for keyword, i is the index variable, in allows iteration through "range(5)" and range(5) is TBE...
    for i in range(5):
        print("hello there", i)

    # why does it start out at 0?  we'll get to that when we talk about lists
    # range(5) gives us 0, 1, 2, 3, 4
    # starts out at 0, 1, 2, 3, 4 (counts up to 5)
    # range(N) starts at 0 and gives us each integer up to N (not including N) or up-to AND including N - 1.

    n = int(input('Enter an integer: '))
    # add up all the integers less than n (bigger than or equal to zero)
    # n = 5, 0 + 1 + 2 + 3 + 4 = 10
    # n = 6, 0 + 1 + 2 + 3 + 4 + 5 = 15
    # etc

    # we need to initialize the variable:
    total = 0
    for i in range(n):
        # why total += n ? not right
        total = total + i
    print('the total is', total)
    # started at zero, gone up to 99 (whatever n is) added them all together.
    # Gauss Sum.

    for i in range(100):
        if i % 7 == 0 or i % 3 == 0:
            print(i, 'is divisible by three or seven')

    # ok that's a lot of pointless number crunching gibberish
    # what if we want to remember 5 different words?

# to declare a list, use the [] notation
    my_first_list = []
    # a list is a type of variable, not int, float, bool, str, something else.
    for i in range(5):
        word = input('Tell me a word: ')
        # append means 'add it to the end of this list'
        my_first_list.append(word)

    print(my_first_list)
    # we've made a list, but how do we access a list? you want one element at a time

    # for each loop:
    for my_string in my_first_list:
        print(my_string)

    # usually what you want

    # let's say that we want to get all the words that start with 'a'
    for my_word in my_first_list:
        # my_word is a string, each string is a collection of characters
        # to get the character at position "i" you access it like this:
        # my_word[i]
        # be careful: 0 <= i < len(my_word)
        if my_word[0] == 'a':
            print(my_word, 'starts with a')

    # in order to get the length of a list or string, use len built-in function
    print(len(my_first_list), len('robot attack'))

    # access a list in reverse order, not a bad example
    # we can't do a for each loop, only going forward through the list

    # for i[ndex] loop - other type of for loop.
    # for index loops
    # format of a for i loop in general
    # l = len(x) gives us the length of x
    # range(l) gives us indices starting at 0 ending at l - 1
    for i in range(len(my_first_list)):
        print(i, my_first_list[i])
        # not reverse yet, this is forward order.

    print(my_first_list[3], my_first_list[1], my_first_list[0], my_first_list[4])
    # index:   0 | 1 | 2 | 3 | 4
    #          -----------------
    # element: a | b | c | d | e

    # indicies a little bit, for i, for each, our goal is to print list in reversed order
    for i in range(len(my_first_list)):
        # hard coding of 4 is kinda bad
        # reason: maybe later on in your life you'll change the list to be 6 elements, 20, 200...
        # but len(my_first_list) == 5 right? I used 4 not 5...
        # we need an offset
        # this one is ok to hard code because no matter what len(my_first_list) is, -1 always correct
        print(my_first_list[len(my_first_list) - 1 - i])
        # Whenever you think "that will never need to change!"
        # next day/hour/min/microsecond: you/your boss says "change that"

    # yes there's another way to do it.
    # let's say you want to start out at 1 and go to 100, not 0 to 99.
    for x in range(100):
        # secret argument inside of print end=some_string replaces the endline with whatever that string is.
        print(x + 1, end="a")
    # there's another way to do it
    # if you have two arguments in range(start, stop) where to start, where to stop with a < sign. x < 101

    # if you need an extra endline, here's how to do it
    print()

    for x in range(1, 101):
        print(x, end=" ")

#
start = 1
while start != 1:
    start = int(input('Tell me where to start: '))
    stop = int(input('Tell me where to stop: '))
    step = int(input('Tell me how many to step: '))

    # step is secretly == 1 unless you set it differently <-- default
    # start == 0 <-- default
    # stop you have to set <-- can't avoid this one
    for t in range(start, stop, step):
        print(t)

    # what did we learn? stop - start is the same sign as step, then it'll work.
    # invalid range object
    # start at negatives, end at negatives, that's all ok, be careful with list indicies

my_word = input('Tell me yet another word: ')
# forward order (a string can be output using a for loop)
for c in my_word:
    print(c, end=" ")
print()

# also do range(len(my_word), 0, -1) BUT i - 1 in the index
for i in range(len(my_word) - 1, - 1, -1):
    # i just going to be indices, we want to access the element at that index
    print(my_word[i], end=" ")
    # why did we need all these -1's?
    # len(my_word) - 1 <-- what's with this one? len('word') == 4, but the last index is 3, shift down by 1
    # why is -1 == stop?  remember that stop never gets hit, if we use 0 then it's not going to hit zero
    # zero is an index, so we need to hit zero.
    # step == -1 because we're going backwards.

list_of_words = ['four', 'score', 'seven', 'years', 'ago', 'our', 'fathers', 'brought']
# i index is the position in the list
# j index is the position in the ith string
for i in range(len(list_of_words)):
    print(list_of_words[i])
    for j in range(len(list_of_words[i])):
        # gets the ith word, jth letter in that word
        print(list_of_words[i][j], end=":")
    print()

# general way to draw grids.
# nest if statements, here we nested loops:
width = int(input('What is the width? '))
height = int(input('What is the height? '))
for y in range(height):
    for x in range(width):
        # i used end = "" <-- empty string, not space
        print("*", end="")
    print()


"""
    talk about lists a little bit more

    lists can be of any type
    do the elements have to be of the same type ? no... but it is recommended
"""

another_list = [1, 2, 4, 8, 12]
float_list = [2.1, 3.2, 4.3, 5.4]
str_lists = ['a', 'b', 'c']
bool_list = [True, False, False, True, True, False, True]

mixed_list = [1, 'hello', 3.14, False, True, [2, 45, 98, 'happy'], False, 3]
#  here's the reason you don't do this often
#  it didn't crash.
#  generally you want everything in your lists to be the same "thing" so that you can operate on each element
#  in the same way

# for x in mixed_list:
#     print(x + 2)


# specific digit isolation
n = 1729
# we want the thing in the 100's place
hundreds_digit = (n // 100) % 10
print(hundreds_digit)
# can't do that n[2] <-- wouldn't that be nice

print(int(str(n)[len(str(n)) - 3]))  # <-- you have to know some extra stuff to make this trick work
# if this isn't tricky enough, then you're too tricky
# observation about python: python allows you to do A HUGE AMOUNT OF THINGS
# some are good, some are bad, some are weird
#
