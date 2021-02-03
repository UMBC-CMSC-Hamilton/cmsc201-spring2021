# let's do an mad-lib!!!

a_noun = input('Enter a noun: ')
an_adjective = input('Enter an adjective: ')
a_verb = input('Enter a verb: ')

print('Once upon a time there was a {} which had a {} toy and liked to {}'
      .format(a_noun, an_adjective, a_verb))

"""
    Let me talk about variables a little bit...

    variables store data in RAM... 

    Hard drive, RAM = Random Access Memory = grid of temporary storage
        "memory address"

    what about python variables?
        must start with either _ or a letter, can't start with a number

        2_cool isn't cool not a legal variable name
        _2_cool
        variable names can be made of upper case, lower_case letters, numbers, and underscores

        PEP8 = general coding standard of this class.   
"""

a_variable_is_like_this = 3
# variable names should be meaningful

radius = float(input('Enter a radius: '))
PI = 3.14
circumference = 2 * PI * radius
print('if the radius is', radius, 'then the circumference is', circumference)

# remember that you have to declare a variable before you use it.
"""
This is a problem because diameter doesn't exist on the first line
bigger_diameter = diameter + 2
diameter = 15
"""
diameter = 15
# let me explain this
diameter *= 2
# for every operation, +, *, -, /, **
print(diameter)
# remember that code always interprets the RHS first and evaluates it, then it sticks the result
# in the left hand side.
# = assignment only goes one way LHS <-- RHS
# diameter * 2 = diameter not legal
diameter = diameter * 2
print(diameter)

"""
    What have we learned on the show tonight Craig?

    We've learned how to print
    We've learned how to do input
    We've learned how to cast string <-> int, float
    We've learned a bit about variables, how their names work
    We've learned about *=, +=, -=, **= operators shorthand for x = x * 2

    WINSCP will get your file from YOUR computer to the GL server.
    Cyberduck is a free GUI based SCP program for mac

    # we can only see what you've submitted...    remember to submit

    # next time: if statements
"""