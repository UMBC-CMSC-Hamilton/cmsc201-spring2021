"""
    Local vs Global (a bit more on that)
    CONSTANTS - what are they?
    hex <-> dec <-> bin

    don't use global variables inside your functions

    THINGS IN ALL CAPS are constants

    "is there a feature for this thing that i want to do?"
        C++ - haha no
        Java - something.something.something.something.something.what_i_want()
            "verbose"
            GOOD IDE - java is almost a usable language.  <-- autocomplete
            1998 around there (notepad, wrong)
        Python - yep

    Recursion is when you call a function from within itself.  <-- now we can end the lecture.
"""

# constants are in capital SNAKE_CASE
# the rule for constants in this class at least is that constants should not change.

# just as a convention, as an agreement, a contract between you and me.  You're not going to change this list.
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
THE_CONSTANT_E = 2.7182818459
MR_PI = 3.1415926535897923280646
NUMBER_OF_THINGS_IN_DOZEN = 12
BAKERS_DOZEN = 13


# constants don't really exist in python.


def first_func(my_str):
    x = 3  # first local x, why is this ok
    # creating a variable in python means assigning it the first time.
    # x = 3 is creating a new local variable with a name x
    # python "forgets" about the global x while this function is running so that's ok

    # why is this different?
    print(my_str)  # don't do this, what's the problem with this? but this isn't ok?
    # it's not passed in as a parameter, and it's not a local variable
    # breaks the idea of what a function "is"
    # function should be some self-contained piece of code that works regardless of if you change some
    # variable somewhere else randomly in the code.
    # the parameter name / argument name makes sure that whatever we call the string outside,
    # it's going to have the same name inside the function
    # strings are immutable "it's a copy"

    print(x)


def second_func():
    x = 5  # second local x
    print(x)


def dec_to_hex(number):
    the_string = ''
    hex_digits = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a',
                  11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    # you could have also made a list.
    if number == 0:
        return '0x0'

    while number:
        # keys are integers!!! the values are strings!!!!
        print(number, number % 16, hex_digits[number % 16])
        the_string = hex_digits[number % 16] + the_string
        number //= 16

    return '0x' + the_string


if __name__ == "__main__":
    """
        Don't use global variables - Shorthand (not precise)
        
        What we really mean is don't use global variables inside of your functions.  Use parameters/arguments
            Reason: Makes sure that your function is independent of name changes, global code changes.
            Good coding style, good understanding of what the purpose of a function is...
            Functions should be "independent" of other functions/code in main.  "if we cut it out, it should still work"
                (Take the helpers too)
            
        CONSTANTS all caps, you can use those in your functions.  
    """

    x = 7  # global x
    floaty_mc_float_face = 3.2  # 3.2 is a literal
    booly_mc_boolface = True  # True is a literal
    happy_string = 'hello there'

    print(x)
    # literal is just a string, int, float, or bool that is "hard coded"

    first_func('this is a string literal now')
    print(x)
    second_func()
    print(x)
    # error if this is a "true" constant
    # in python world, you CAN "change" constants
    # what's up with that?
    # the reason that we do constants like this in python isn't because python has constants, it actually doesn't
    # its a social contract, if i see a variable in all caps, then it's a constant, so don't change it
    # that's really it.
    print(BAKERS_DOZEN)
    BAKERS_DOZEN = 14
    print(BAKERS_DOZEN)

    x = int(input('Tell me int: '))
    while x != -1:
        print(dec_to_hex(x))
        x = int(input('Tell me int: '))
