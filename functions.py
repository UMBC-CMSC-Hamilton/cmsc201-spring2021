"""
How do we define a function?
"""


# def <name of your function>( <-- open paren ) <-- closed parenthesis : <-- colon required
# everything under the function must be tabbed in, just like if, for, while, elif, else
# functions should be declared outside of the if __name__ statement.
# naming conventions for functions, yes use snake case, lowercase separated by underscores

# definition
def my_function():
    # function "body"
    print('Hello there I am a function')
    eggs = int(input('How many eggs do you need in your omelet?'))
    print('You said', eggs, 'eggs')


if False:
    # function call
    my_function()
    print('second ')
    my_function()
    print('third ')
    my_function()
    print('fourth')
    my_function()
    print('fifth ')
    my_function()
    for i in range(5):
        my_function()
    draw_grid(5, '*')
    print()
    draw_grid(12, 'a')
    print()
    draw_grid(7, '&')

"""
    This is "kinda" pointless, is there any way to communicate with a function?
    Hey I want to send some data into the function that will change its behavior.  
    
    Draw grid function

    "pass", "send" some variable into the function
    
"""

# size is a "parameter" of the draw_grid function
"""
    One of the benefits of a function is that you don't have to repeat this code, you can just reuse the same 
    code multiple times.
    
    You can have multiple parameters
    Variables declared inside of the function, size, the_char are called "local"
        A local variable only exists as long as the function exists, and then it's erased/forgotten/deleted
"""


def draw_grid(size, the_char):
    # you can declare new variables inside of a function
    print(ord(the_char))
    for i in range(size):
        for j in range(size):
            print(the_char, end="")
        print()


# here is the end of the function, once we get to the end, a few things happen.
# 1) all the local variables die

# x^2 - x - 1
def compute_poly(x):
    """
    Standard function documentation
    Computes x^2 - x - 1
    :param x: float or int, value to be computed
    :return: the value of the computation.

    Whatever is in return replaces the function call, and allows you to save some data that comes back
    from the function itself.

    s = input('enter number or quit: ')
    while s != "quit":
        print(compute_poly(float(s)))
        s = input('enter number or quit: ')
    """
    return x ** 2 - x - 1


def get_name():
    """
        first_name, last_name are local scope as soon as their scope dies (the lifetime of the function)
        they go away too
    :return:
    """
    first_name = input('What is your first name? ')
    last_name = input('What is your last name? ')
    return [first_name, last_name]
    # no more variables after the return statement.


def square_root(x, error):
    """
    You don't have to understand exactly what is going on in someone else's function.
        You don't have to worry about the specifics of their implementation if you understand how the function
        works, and if their code doesn't have bugs.
    :param x: value we take the square root of
    :param error: maximum possible error between two estimates
    :return: our estimated square root.
    """
    if x < 0:
        print('You cannot take the square root of a negative!')
        return -1  # if this line executes, we are out of this function, no code will execute after it.

    # yes you can just return x**0.5 <-- definitely
    current = x
    previous = -1
    while abs(current - previous) >= error:
        previous = current
        current = (1 / 2) * (previous + x / previous)

    return current


"""
    Yes, let's write our own version of .lower()
"""


def lower(the_string):
    new_string = ''
    for c in the_string:
        if 'A' <= c <= 'Z':
            # chr(number) ->> character
            # ord(character) ->> number (ascii value)
            # always memorize that upper case starts at 65, 97.
            new_string += chr(ord(c) + 32)
        else:
            new_string += c
    return new_string


def my_split(a_string):
    """
        2 good reasons, 100 bad reasons
        You "can" but DONT EVER IN THIS CLASS declare a function inside of a function.
        Very very very very very strange examples why this feature exists.
    """
    # splits it up by whitespace
    # what is this pass keyword?


def blah_function():
    a = 1
    b = 2
    c = 3
    # returning multiple values:
    return [a, b, c]


if __name__ == '__main__':
    # user_name = get_name()
    # print(user_name)
    # after you print it, that data is lost "forever"
    # we never saved it.
    # once we save it to the user_name variable, we can use the returned value over and over again.
    # we didn't lose it anymore.
    # "".lower() <-- definitely a function
    # strip, split, join (class methods)

    print(square_root(5, 0.001), 5 ** 0.5)
    print(square_root(17, 0.001), 17 ** 0.5)
    print(square_root(23, 0.001), 23 ** 0.5)
    print(square_root(23, 0.1), 23 ** 0.5)
    print(square_root(-5, 0.2))
    s = input('Enter string to be lowered: ')
    while s != 'quit':
        print(lower(s))
        # if you don't return the value, python returns the special None object for you.
        s = input('Enter string to be lowered: ')
    # abstraction classes? not yet
    # it is abstraction because you can "hide functionality"  from another programmer
    # all they need to understand is the input and the output of the function.
