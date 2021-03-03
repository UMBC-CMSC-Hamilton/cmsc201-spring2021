"""
    Let's talk about lower(my_string)
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
    takes a string, splits it on whitespace

    :param a_string: string that we input to split by whitespace
    :return: "   list of strings result of splitting"
    """

    split_list = []
    current_string = ''  # using temporary variable to store parts of an answer
    in_string = False  # flag variables

    for index in range(len(a_string)):
        # how can we tell that we have whitespace?
        # if it strips to nothing, then it's whitespace
        # splitting into cases
        if in_string:
            if a_string[index].strip():  # not whitespace
                current_string += a_string[index]
            else:  # whitespace
                # we did encounter whitespace
                split_list.append(current_string)
                current_string = ''
                in_string = False
        else:
            #  if the value of a_string.strip() is True, a_string[index] was NOT whitespace
            # so we set in_string to True and add the character to a new string
            if a_string[index].strip():
                current_string += a_string[index]
                in_string = True
    # if we were in a string at the end, we may not actually save it...
    if in_string:
        split_list.append(current_string)

    return split_list


def test_split():
    # CTRL + ALT + L <-- re-formats to fix pep-8 problems
    s = input('Tell me a string to split: ')
    while s != 'quit':
        print(my_split(s))
        s = input('Tell me a string to split: ')
    # it """works""" almost


# old python code
# s.strip().split()
# all you need is
# s.split() <-- will do the stripping for you


"""
    Refresher on prime numbers:
        What is a prime number?  
            A prime number is some natural number > 1 (note that 1 is not prime) so that it is divisible only
            by 1 and itself.  (only two divisors)
            9 (engineers prime == not a prime) (joke, odd integers are prime, so 9 is too)
        2, 3, 5, 7, 11, 13, etc
"""


def is_prime(n):
    # why dont we start at 1?  because 1 divides everything evenly so it isn't helpful
    # how can we tell if something divides evenly?  There's a specific special operator we learned.

    # edge cases (on the edge of the input spectrum)
    if n == 0 or n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            # way cleaner than asking for fractional remainders.
            return False

    return True


def test_is_prime():
    for i in range(100):
        print(i, is_prime(i))


"""
    Local variables vs global variables
    
        Local variables live inside of functions, and their lifetime is only as long as the function exists
"""


def modify_string(the_string):
    """
     This function is a lie
     But why?
        my_favorite_string never got changed, even though the_string did.

     In python types are divided into two "groups" immutable types, mutable types

     immutable: int, float, bool, string, [datetime, tuples, ..]
        when you pass it into a function it passes "by value"
        copy of the value into the new variable, the_string ISNT actually my_favorite_string
        what it is, is a copy. Not the original data element/memory location/whatever.

        Advantage: you can pass immutable things to a function and be sure that it won't mess them up.
            You know that its making a copy of the value, so it won't be destroyed by the function call.
     mutable: lists, [dictionaries, classes] when we get to them.
        when you pass a mutable object into a function it passes "by reference"
        that means it's not making a copy, the name of the variable is a secret placeholder for the other variable

    """
    print(the_string)
    the_string = 'hello there'
    print(the_string)


def modify_my_int(my_int):
    my_int += my_int ** 2 - 2 + 5 * my_int
    print(my_int)
    return my_int


# my_favorite_string = "definitely not hello there, no way, no how"
# modify_string(my_favorite_string)
# print(my_favorite_string)
favorite_integer = 17
result = modify_my_int(favorite_integer)
print(favorite_integer, result)


def modify_my_list(test_list):
    test_list.append("hello")
    if 'robot' in test_list:
        test_list.remove('robot')


greatest_list_ever = ['robot', 'attack', 'fishing', 'scrumptious', 'deleterious', 'foible']
result = modify_my_list(greatest_list_ever)
print(greatest_list_ever, result)
# wait you were just saying that functions don't modify their arguments!?!?!?!
# that's the whole point of the immutable vs mutable debate/question/whatever
# BUT !!! lists are mutable when you pass them into a function, there's a danger
# "most functions will be good" - in python you have to trust the code you're calling.
# in C++ there's a reference operator & which allows us to CHOOSE which thing we want
# in Python (different) you never choose whether to pass by value or reference
# it's entirely decided by the nature of the variable (immutable/mutable)

"""
    Let's talk about palindromes
        Palindromes are pointless, i agree
        but they're a great problem:
            require you to think about indices in strings/lists
            0 <-> len - 1
            1 <-> len - 2
            2 <-> len - 3
            i <-> len - (1 + i) or len - i - 1
            ...
            whenever we get to the middle we can stop
            racecar
            amanaplancanalpanama
            tacocat
            
            abcdcba <-- same if you reverse it.  
"""


def is_palindrome(test_pal):
    for i in range(len(test_pal)):
        if test_pal[i] != test_pal[len(test_pal) - 1 - i]:
            return False
    return True


s = input('Tell me a string to test for pals: ')
while s != 'quit':
    s = ''.join(s.split())
    print(s)
    print(is_palindrome(s))
    s = input('Tell me a string to test for pals: ')

