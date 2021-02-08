# let's do some coding!

"""
Last week:
print()
input()

4 basic data types:
    int, float, bool, str

    int = integer -10, -9, ..., 0, 1, 2, 3, 4, ... 2,981,123,123
            It's possible to store larger values than a standard int
            "4 byte integer" == standard

    float = anything with a decimal

    bool = True, False

    str = string of characters
        input always returns a string, if you need you have to cast it to a float or int
        dangerous to cast to a bool, doesn't always give what you expect.
"""

"""
This week:
if statements

talked about if statements last 
"""
x = 3
y = 5

if x < 5 and y < 10:
    print('both things are true')


s = input('Enter a string: ')
y = int(input('Enter an integer: '))

# at the end of every if statement you use a colon
if s == 'stream' and y == 5:
    # anything inside of the if statement gets tabbed in by one level.
    print('5x5 = 25')
    print('this is inside of the if statement')

print('this is not in the if statement')

# just because you have an if statement you don't need an else.

another_string = input('Enter another string: ')
# two equals in programming, there's assignment and there's conditional equality
# case sensitive == GO != go
if another_string == "go" or another_string == "GO":
    print('lets go')
# if you forget to do this, then you're in trouble.
if another_string != "go":
    print('lets not go')

# this is a little bit dangerous because... if you make a modification to the first if statement
# then it's not exactly the opposite of the second one anymore...

# is there a way to always execute the second condition whenever the first is false?
# yes!

x = int(input('Enter x: '))

# the first if statement executes when first condition is true
if x > 5:
    print('x is big enough')
# else is a keyword in python, else: <<-- colon at the end
# else evaluates whenever the first condition is false
else:
    print('x is too small')
# else is guaranteed to execute if the if statement doesn't execute.

# i decide to change this from x > 3 to say x > 5

if x == 2:
    print('x is two')
if x <= 3:
    print('x is three')

menu_select = int(input('Enter 1 to start game, 2 to load, 3 to save, 4 to quit'))
if menu_select == 1:
    print('time to play a game')

if menu_select == 2:
    print('time to load a game')

if menu_select == 3:
    print('save game time')

# this if statement is the only one connected to the else statement.
if menu_select == 4:
    print('quitting game')
else:
    print('thats not on the list')

# there has to be a way to fix this because otherwise coding would be horrible.
# elif == else if

# when you have elifs, they connect with the first if statement above

menu_select = int(input('Enter 1 to start game, 2 to load, 3 to save, 4 to quit'))
if menu_select == 1:
    print('time to play a game')
    # if this turns out to be false, it goes to the first elif
elif menu_select == 2:
    print('time to load a game')
    # if this turns out to be false, it goes to the next elif
elif menu_select == 3:
    print('save game time')
    # if this turns out to be false, it goes to the next elif
elif menu_select == 4:
    print('quitting game')
    # if this turns out to be false, it goes to the else
else:
    print('thats not on the list')

# here's the good news about elif statements: only one can ever execute

x = int(input('Enter an x variable: '))

# it only executes one of these, so it catches it on the x == 0 condition before x <= 0
if x == 0:
    print('x is zero')
elif x <= 0:  # get rid of that equal sign to make yourself not introduce bugs later
    print('x is negative')
else:
    print('x is positive')

# be careful because your if/elif/else statement order matters
if x <= 0:
    print('second x is negative')
elif x == 0:
    print('second x is zero')
else:
    print('second x is positive')
# this is a dumb example because you probably wouldn't include that equal sign (bug)

# you might be tempted to say.. hey wait, x < 0 to be negative, x == 0 neither negative nor positive

money = int(input('How much money do you have? '))
if money >= 10 ** 9:  # 1 billion dollarz
    print('you are a billionaire')
elif money >= 10 ** 6:
    print('you are a millionaire')
elif money >= 10 ** 3:
    print('You are a thousandaire')
else:
    print('sorry.  ')

print('Second test: ')
# backwards order, because it catches on lower amounts before higher amounts
if money >= 10 ** 3:
    print('You are a thousandaire')
elif money >= 10 ** 6:
    print('you are a millionaire')
elif money >= 10 ** 9:  # 1 billion dollarz
    print('you are a billionaire')
else:
    print('sorry.  ')

print('Third test: ')
if money >= 10 ** 3:
    print('You are a thousandaire')
if money >= 10 ** 6:
    print('you are a millionaire')
if money >= 10 ** 9:  # 1 billion dollarz
    print('you are a billionaire')

# these are three disconnected (logically independent tests)

"""
Let's discuss mod

Remember last time, we talked about // integer division
"""
print(5//3, 17//21, 17//5)
# when a computer does an integer division it actually computes two things at once.
# the first thing it computes is the answer to the division, but second thing is the remainder
"""
    7 // 3 = 2 R 1 --> because 2 * 3 + 1 = 7
    q R r, q = quotient, r = remainder
    19 // 5 = 3 R 4 --> because 3 * 5 + 4 = 19
    -2 // 5 = -1 R 3 --> -1 * 5 + x = -2, x = 3
    

    In python and in C++, Java, Javascript, C#, Ruby, most languages
        remainder (mod) operation is %
"""
print(-2 // 5)
# why does python do this?
# answer: 0//5, 1//5, 2//5, 3//5, 4//5 all == 0
# we want only 5 numbers to get the same result when you divide by 5
# -1//5 ?= 0 actually -1
# -1//5, -2//5, -3//5, -4//5, -5//5 all == -1
# R >= 0 non-negative
# -1//5 == 0 R -1 <-- no
# -1//5 == -1 R 4 <-- yes, quotient can be negative, remainder must be positive
# elementary school math is being enforced by Python.
# i'm not going to harp too hard on the negative stuff, other languages dont' do this

print(7 % 3, 19 % 5, -2 % 5, 123 % 4)

x = int(input('Enter numerator: '))
d = int(input('Enter denominator: '))

if d != 0:
    # the number of times d goes into x, the remainder afterwards, puts it back together
    print(x // d, x % d, d * (x//d) + x % d)
else:
    print('Dont divide by zero.')

# 4 / 5 == 1 R -1 or 0 R 4 <<-- this one


degree = int(input('Enter spin degree'))
print(degree)
degree = degree % 360
print(degree)
if degree // 40 == 0:
    print('a')
elif degree // 40 == 1:
    print('b')
elif degree // 40 == 2:
    print('c')
elif degree // 40 == 3:
    print('d')
elif degree // 40 == 4:
    print('e')
elif degree // 40 == 5:
    print('f')
elif degree // 40 == 6:
    print('g')
elif degree // 40 == 7:
    print('h')
elif degree // 40 == 8:
    print('i')
else:
    print('huh?')

# what do we know about angles?  They repeat geometrically every 360 degrees... so...

"""
    Here's another interesting and very useful thing to do with mod
    parity == even/oddness of a number comes up a lot in computer science
    
    How can we use mod to check if a number is even or odd?
        our_number % 2
    What is the definition of an even number?
        number theory - integer n for which there is another integer k so that n = 2k
        simple "it is divisible by 2" <<-- we mean EVENLY divisible NO REMAINDER
        our_number % 2 == 0 then our_number was even
    What is the definition of an odd number?
        n = 2k + 1 for some integer k, then n is odd
        our_number % 2 == -1 or our_number == 1
        in Python: our_number % 2 == 1 <-- yay
    Trick: is 0 even or odd, both, neither?
        Python: 0 is even.  Everybody thinks: 0 is neither positive nor negative ==> 0 is neither even nor odd
        0 % 2 == 0 <-- even
        k = 0, 2(0) = 0 <-- even
        negative zero exists in some computer hardware, but thankfully not in the past 30 or so years...
        80x86, 80x64 architectures, arm don't have negative 0
"""

a_number = int(input('Tell me a number, i will tell you if its even or odd: '))
if a_number % 2 == 0:
    print(a_number, 'is even')
else:
    print(a_number, 'is odd')

"""
    You at this point shouldn't assume that we give you good numbers.
        Enter pos number:
            I may enter a negative number.
            
    But I will not enter a float, string, anything like that.  
        You don't have the ability to catch these exceptions.
        Assume that whenever you ask for input, we will give you the correct type.  
"""
entered_number = int(input('Enter a positive number: '))
if entered_number > 0:
    print('good')
else:
    print('bad')

# it still will crash on a string.