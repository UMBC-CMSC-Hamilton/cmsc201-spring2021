"""
We talked about if statements
    elif
    else
"""
x = 3
s = 'something'

# start with the keyword if
# in Python they all must end with the colon:
# syntactic == feature that the compiler looks for in the grammar of the language.
if x == 3:
    print('x is three')

# not equal operator
if x != 3:
    print('something else')

"""
    Things to remember about elif:
        only AT MOST one elif ever gets executed, could be zero
        
"""
x = 3
if x == 1:
    print('hello')
elif x == 2:
    print('goodbye')
elif x == 3:
    print('robot')
    # doesn't continue to execute once it finds a true condition.
elif x == 4:
    print('daffodil')
elif x == 5:
    print('summation notation')
# i didn't add an else clause here it's possible that nothing will happen.
# even if you have else if clauses (elif) you don't need an else.

# what does else do?  else is like the "catch-all do this if nothing else works clause"

s = input('Enter your word of choice: ')

if s == 'happy':
    print('it is good to be happy')
elif s == 'sad':
    print('it is less good to be sad')
elif s == 'robot':
    print('robots do not have emotions, yet...')
else:
    # this executes when nothing else is true
    print('what other kinds of words are there? ')

"""
    That's all from last time.  
"""

"""
    Short Circuit Section
"""

x = int(input('Enter dividend (top thing): '))
y = int(input('Enter divisor: '))

# x / y less than or equal to 10
# safety checking before you let the division occur
# BAD : if x / y <= 10 and y != 0: (the reason its bad is that it divides first before checking)
if y != 0 and x / y <= 10:
    # the reason it didn't try to execute the division is called "short circuiting"
    # as python reads from left to right (in this case)
    # a and b and c
    # a is already False
    # then you don't need to evaluate anything more.
    # x / y won't be evaluated unless the first statement is already true.
    print('The condition is true. ')
else:
    print('You tried to divide by zero, naughty human.  ')


"""
    Short circuiting for or.
    
        For the and statement if the first condition was false, then the condition (expression)
        didn't check anything further, just returned False.
        
      
"""
a = True
b = False
if a or b:
    print('a or b or something')
else:
    print('neither a nor b')

# here it sees that the denominator is zero, and so it's happy, or statement is already true
# doesn't need any more "prongs"
# a or b or c or d...
if y == 0 or x / y == 2:
    print('one of those two things was true')
else:
    print('not that')


# evaluation of variables as either true or false.
# each of the standard types in python:
#   int, bool, float, str
# has a "is true" built into it

my_var = int(input('Enter my_var: '))
print(type(my_var))

# is my_var true?
if my_var:
    print('my_var is considered true')
else:
    print('my_var is considered false')
# is my_var == 0? or not.
# True == 1, False == 0, a boolean variable is one byte
# a byte == 8 bits
# each bit is a zero or one.
# -128 <= x < 127 signed
# 0 <= x < 255 = 2 ** 8 - 1
# notice that my_var is true even if my_var is negative, positive, really big, really small, etc.
# only thing it can't be is zero.

# for boolean types:
b = False
if b:
    print('b is true')
else:
    print('b is false')

# what about floats?
# floats borrow from integers.
my_float = 3.412341234
if my_float:
    print('floats follow the same logic as ints')
"""
    my_float is True / true in the evaluation as well when my_float is not zero
    my_float is False when my_float is entirely 0.0
"""

my_zero_float = 0.0
# type forbidden in this class
print(type(my_zero_float))
if my_zero_float:
    print('zero floats are true')
else:
    print('zero floats are false')


"""
    strings are the last data type:
        an empty string is false
        a non-empty string is true
"""

first_string = 'asdf'
if first_string:
    print('non empty strings are true')
else:
    print('non empty strings are false')

empty_string = ''
# empty_string = ""
# empty_string = str()
if empty_string:
    print('empty strings are true')
else:
    print('empty strings are false')

# tab escape sequences to get a tab, you use \t
# to get an endline you use \n
whitespace = '  \n \t\t    '
if whitespace:
    print('whitespace strings are true')
else:
    print('whitespace strings are false')


"""
    Nested If Statements
        When we say nesting what we mean is like Russian Nesting Dolls
"""

a = True
b = True
c = False

if a:
    print('a is true')
    # what does this do?
    # not inverts logic
    if not b:  # <-- nested
        print('b was false')
        if c:
            print('c is true')
else:
    if b:  # <-- nested
        print('a was false but b is true now')

if a and not b:
    print('a is true\nb was false')
# what is the difference?
# internal second if statement is tabbed in another level
# if a == True and b == True, then the first print will happen in the top code, but not in the
# bottom

""" 

    not a limit on the number of elifs you can have but if you have more than 20, you should 
    think about what you're doing
    
    not really a limit on nesting if statements, but nest more than 4 levels, maybe rethink.   
"""

