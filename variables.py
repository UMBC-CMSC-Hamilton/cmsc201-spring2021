# Let's do a little bit of review. (pound-sign, hash tag) start a single-line comment
# the Python interpreter basically ignores the comment lines.

# Multiline comments are done like this:
"""
This is a multi-line comment (basically)
    we can use it for that purpose.

    Actually: A multi-line string

    Do I need to comment my code?
        Yes
    Do I need to comment nearly as much as these lecture files?
        no.
"""

"""

Review variables

    A variable is really an abstraction of a memory location (or multiple memory locations) 
        in RAM.
    We give these variables names so we can refer to them. 
    Rules for variable naming:
        1) has to start with underscore _ or letter (upper or lower case)
        2) has to be made up of numbers, letters, underscores

    Coding Standards for Python:
        1) snakecase: variables are lower case and underscores
        2) you should have meaningful variable names
        3) spell out words when it makes sense (when its not way way way too long)
        4) obvious abbreviations are ok.
        5) avoid single letter variables except as loop indices.  
        
        this_integer
        my_string
        favorite_number
        
        In this class, assume our coding standard is this one, snake_case

    camelCase
        No underscores, words spelled out, first word lower case, 
            all others first letter capitalized
        myInteger
        thisVariable

"""

pi = 3.1415926535

radius = 5
area_of_circle = pi * radius ** 2
# don't do this, no one will know what the heck this is...
x = 31 * radius + 2 * pi - area_of_circle ** 2
# you in a week or your TA won't know what this is...

# What are the four "primitive" variable types in python?
# integers (either positive or negative * whole number, 0)
my_integer = 5

# float is the second type of variable
# float == floating point
# there's a decimal in it.
my_float = 1.6789
also_a_float = 5.0  # if you ever need a float, but it's also an integer, put a .0
# last time people mentioned doubles.  Python doesn't have a double because its float is
# actually far more precise than the C++ float type.  (secretly it may even be a C++ double)
# converting from a float to integer is a pure truncation (rounding down)
print(int(5.9), int(5.2), int(5.0001), int(5.0))

# let's talk about strings!
a_string = 'you can use this kind of delimiter'  # single '
double_tick_string = "you can also use this delimiter"  # double "
print(type(a_string), type(double_tick_string))
# type you aren't going to use in this class.  But here i'm using it to show you that it's
# the same type.
# python doesn't really have characters, it does have length 1 strings
# you can add strings natively in python
first_string = 'hello'
second_string = "Python"
"""
    String Concatenation:  Two (or more) strings are put/added together into
     a single new string.
"""
addition = first_string + second_string
print(addition)

# boolean type
"""
    Boole Boolean logic = True, False, and, or, not.
"""
True
False
# flag variables are variables that wait until something happens, then you flip them
# when you flip them, you detect that in an if statement and do something about it.
server_connected = True
# if the "server" were ever disconnected, you'd set this to false and then try to fix that

continue_playing = True
# the game is going until this set to False then the game is over...

# python gives you the keywords and or not
"""
or is true when either one is true
or  A   T   F
B    
    T   T   T
    F   T   F
"""
print(True or True, True or False, False or True, False or False)

"""
Truth Tables
and is true when both are true
and A   T   F
B    
    T   T   F
    F   F   F
"""
print(True and True, True and False, False and True, False and False)
# && == logical and operator in C++ "and" is the logical and in Python

"""
Truth Tables
not is true when both are true
not is different from "and" and "or"
    Not "unary operator" = operator that eats a single argument
    and /or are "binary operators" = they eat two arguments. +, -, *, / , //, and, or
    ternary operator C++ a ? b : c;  tests a, if true, then b else c;
    hex operator would be 16 arguments... that's a lot
A       T   F
not A   F   T
"""
print(not True, not False)
"""
    not has higher precedence than and/or
    and/or have equal precedence
    
    precedence = which operation happens first
    
    Order of operations for and/or/not
    
    Potentially not what you mean without parens...
    3 + 2 * 5    
    (3 + 2) * 5
    3 + (2 * 5)
    PEMDAS = sorta right.,     PEDMSA,    PEMDSA,     PEDMAS, whatever
    PE(MD)(AS)
    Multiplication and division have equal precedence
    addition and subtraction have equal precedence.  
    
    PN(AO) - order of operations
    Please Never Attack Objects - order of operations for logic
    Please Never Order Asparagus - two equivalent nonsense bits.
"""

a = True
b = False

# i don't know what this is  going to do, unless we believe the OrderOfOps
print(not b or a, (not b) or a, not (b or a))

"""
Let's take a break from logic for a second and talk about integer division vs floating division.

in python, if you have two integers and you divide them, let's see what happens:
"""
print(5 / 3)
"""
    Hmmm.. a float popped out, that isn't right.
    Sometimes you definitely don't want this to happen.
    If you want the result to remain an integer, do this:
"""
print(5 // 3)
# this is extremely useful because sometimes you ABSOLUTELY need an integer
print(int(5 / 3))

# hmmm... the result here was -1, what the heck?
print(-1 // 3)
# 0, 1, 2 // 3 == 0, so -1, -2, -3 // 3 == -1
# the result is actually different for negative numbers... ugh...
print(int(-1/3))
# if you're dealing with negatives, just understand what it does, use the one you want

# double division symbol is integer division.
# integer division can actually take floats as well, it behaves weirdly sometimes...
print(3.2 // 1.6)
# this is extra nonsense that you should avoid using.

"""
Last 20 minutes will be about if statements... yay?

So far we've learned about printing, inputting, and variables...
if statements are the basic way that computers/programming languages make decisions.   
"""

a_word = input('Tell me a word: ')

"""
    Syntax - what is syntax?
        Structure formal grammar of a language
        it's where words go
        S-V
        
    In python:
        Each if statement "sentence" has an if at the start, colon at the end.
        everything between if and : needs to evaluate to True or False
"""
# notice here, this is not = (single) this is a double equals sign (==)
# programming languages have a different symbol for "test if this thing is equal" ==
#                                                     vs. assign  that <-- that
#                                                                   that = this
if a_word == 'robot':
    print('You have said robot, I accept this.')  # a-block
    # pretty good

print('The program is ending, goodbye.')  # b-block

x = int(input('Tell me an integer: '))
y = int(input('Tell me another integer: '))
if x < y:
    print('y is bigger')
if x > y:
    print('x is bigger')
if x == y:
    print('x is the same as y')

# this is an example of where we are using logical operator to chain two conditions
if a_word == 'salami' and x > 5:
    print('Some random thing happened to be true, also salami')

# flag variables
happy = False
# more code here
if a_word == "happy":
    happy = True
    # this remembers it for later
# much more code here
# later on in your code you can check if happy was set to true.
print(happy)
# a lot of times, happy then decide some later if statement/while loop
# determines how the program works from there.
