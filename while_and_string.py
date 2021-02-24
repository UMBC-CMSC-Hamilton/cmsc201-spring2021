# while loops are like if statements on repeat
s = input('Tell me an integer or quit: ')
while s.lower() != 'quit':
    # discrete log calculator
    # rounding down-ish the log of a number.
    # if you enter something else, this will give a value error
    x = int(s)
    # this kind of thing is ok for you right now.
    count = 0
    while x > 0:
        count += 1
        x //= 2
    # this is going to be way way way way faster than actually calculating a log to various decimal digits requires
    # effort, taylor series, some other kind of method.

    print(count - 1)
    s = input('Tell me an integer or quit: ')

# what we notice is that each time we go up by a power of 2, the count increments by 1
# 2^6 = 64, -> 7

"""
    Strings Lecture
        strip() : converts a string to a new string without trailing and heading whitespace
        split() : converts a string to a list
        join() : convert a list of strings back into a single string with a separator
        in, not in keywords    
        using strings as lists
        concatenation of strings
"""

"""
    Method - function (i haven't defined) which has its own variables, code, and sometimes returns values to us.
        All we're doing is calling methods, we're not writing methods yet (next week).  
    What does strip do?
        strip will take a string and nibble off all of the whitespace before and after any characters.  
        leading or trailing whitespace, say good bye to that.
"""
test_string = "      \t\t\t\nhello\tthere     \n\n"
print(test_string, end="|")
print(test_string.strip(), end="|")
# didn't give a value error, so it worked.
thirty_four = int(' 34  ')
thirty_four_2 = int('34')

story = input('tell me a story: ')
# file input-output, there are going to be extra new line characters all over the place and you have to deal with them.
# when you read a line out a file, it doesn't strip the endline character out.  <-- lots of issues
print(test_string, end='|')
# the reason the string hasn't been modified is that .strip() will output a new string, you need to set
# it to a variable.
new_string = 'aaaaabaaaaabaaaa'.strip('a')  # the thing inside is called an argument/parameter
# weird example, but here it is.
print(new_string)

"""
    Split is the best one is that it reads characters and splits on whitespace blocks
"""
a_sentence = "A regular sentence, nothing special, nothing to see here."
words_from_this_sentence = a_sentence.split()
print(words_from_this_sentence)

# now you want to strip each word for the commas and periods at the end, convert it all to lower case.
for i in range(len(words_from_this_sentence)):
    # multiple characters in this strips for all of them
    words_from_this_sentence[i] = words_from_this_sentence[i].lower().strip('.,')

print(words_from_this_sentence)

# this is going to result in an empty string with no a's and no b's.
print('Here is the result:', 'aababcabababcababa'.strip('ab'))

print('helloathereafriend'.split('a'))
# best way is to play <-- definitely open up pycharm or emacs or whatever and try stuff out until you understand
# how it works.  Make yourself an example, try it and learn from it.

# the argument that we pass into strip looks at each character individually, whereas
# the argument in split takes an entire string and splits on that
print('tohellobehelloorhellonothellotohellobehellothathellois...'.split('hello'))
# the above thing is a pretty bizarre example, but that's what it does, so there it is.
# great for file IO
print('Eric\t443-343-3434\t1234 Somewhere Lane\tsomething@something.something'.split('\t'))

"""
    join is the opposite of split
        takes a list (of strings) and a separator and it joins them together.   

    separator.join(list of strings)
"""

# the string at the beginning is "the separator"
print("".join(["it", "may", "be", "counter-intuitive"]))
# i hate that, i want a space in between
print(" ".join(["it", "may", "be", "counter-intuitive"]))

my_list_of_strings = ['string', 'rope', 'bind', 'tie', 'wristband', 'scrunchy', 'jenga']
sep = input('What is the separator? ')
print(sep.join(my_list_of_strings))

# common 'trick'
print('.'.join('443-910-1234'.split('-')))
mary_had_a_little_lamb = 'Mary had a little lamb her fleece was white as snow.'
print(', '.join(mary_had_a_little_lamb.split()))
# what's the point of this? I don't know, but we need examples to use.

print('argle bargle'.join(['one things']))
print('argle bargle'.join(['two', 'things']))

"""
    python keyword in can be used both with lists and strings
    (technically dictionaries)
    in does "exactly what you think it should do"
    
    in "operator" is a boolean operator -> returns True / False
"""
print('c' in 'accept')
print('c' in 'failure')
# tests if a substring is in there
print('math' in 'mathematics')
print('math' in 'polymath')
print('math' in 'physics')
# what about this one?
print('abc' in 'absurdic')  # returns False, but why?, the letters a, b, c are all in there?
# it's not testing for individual characters, it's testing ONLY for substrings
print('abc' in 'abcdefg')

substring = 'asdf'
big_string = 'find test in me'

"""
    for strings, this is basically what in is doing
    
    very inefficient string matching
    KnuthMorrisPratt, more advanced string matching
"""
found = False
for i in range(len(big_string) - len(substring) + 1):
    sub_found = True
    for j in range(len(substring)):
        if big_string[i + j] != substring[j]:
            sub_found = False
    if sub_found:
        found = True

print('is found true? ', found)


"""
    How does it work for lists?
"""
a_list_of_numbers = [1, 54, 2, 9, 17, 18, 21399]
if 5 in a_list_of_numbers:
    print('five is in there')
else:
    print('five isn\'t in there')

a_random_list = [1, 2, 3, [4, 5, 6], [7, 8, 9], [5]]
# if you have a list within a list, it counts as one element of the bigger list
print(len(a_random_list))

# in doesn't unpack anything, it just checks exactly what it sees.
# {5} == 5? set containing 5 is not equal to the number 5.
# {{5}, 5} != {5, 5}
if 5 in a_random_list:
    print('five is in there')
else:
    print('five isn\'t in there')

if 5 == [5]:
    print('yep')
else:
    print('nope')

print(a_random_list[3][1], a_random_list[5][0])

# python is really doing us a favor here because this not in thing is both pythonic and also english-ic
if 5 not in [1, 2, 4, 8, 16, 32]:
    print('five is not a power of two')

animals = []
s = input('Tell me animal: ')
while s != 'quit':
    animals.append(s)
    s = input('Tell me animal: ')

print(animals)
animal = input('tell me an animal: ')
while animal in animals:
    print('You guessed something in our list, keep guessing! ')
    animal = input('tell me an animal: ')

"""
    Official notice:
        You can concatenate strings
        You can use + or += to add strings together
"""

total_string = ''
s = input('Tell me animal: ')
while s != 'quit':
    total_string += s
    print(total_string)
    s = input('Tell me animal: ')

my_name = 'Eric'

# print takes multiple arguments, whereas input takes exactly one string
print('What is your favorite color', my_name, '?')
# input takes EXACTLY one string


fav_color = input("What is your favorite color" + " " + my_name + "?")
least_fav_color = input(''.join(["What is your least favorite color ", my_name, "?"]))

"""
Next time:

Functions
"""