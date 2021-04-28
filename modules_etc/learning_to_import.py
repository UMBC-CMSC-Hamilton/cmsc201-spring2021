"""

Importing Modules. - Project 2

Initially: Relevant to project 2 maybe 3, useful good stuff.

Totally useless: but probably far more interesting.

What does importing mean?

    A way to include code/use code that you basically "didn't write" that's in a different "module" =
        [Directory, File, Place, etc]

    Tradition:
        import right under your header comment.
            Is it possible to import other places? yes
            Is it terribly smart to do that? no
                1) When you go back to modify your code, if there's some secret import later, i wouldn't know
                    that my code is actually dependent on some extra stuff
                2) Order matters.  These things are not commutative.
                    Code is interpreted exactly linearly (one line after the other)
"""

import time
# import the module under the module name "time"
# read in the "random.py" file (somewhere in the deep dark depths of python)
from random import random, randint, seed
# import random makes us add random. in front of everything.

# not about Python itself.
# import the file name without the .py that will import the file
import primes
from primes import Person
"""
    Can you import a single function out of a class that's inside another module? no.
        You can't use a function/method from a class without having an underlying class behind it.  
    Can you import the class? Yes i just did. 
"""

# from board import Board
# from the board.py file import the Board class and allow me to use it without saying board.Board
# I can just say Board.


"""
    If you're working in pycharm you're going to say, I just can't really deal with this red underline
    screaming at me that there's some kind of error with my code, how do I fix this?
        This code ran!!!!
        Get Pycharm to chill out.  
        Right click on directory of your file, go to Mark Directory As -> Sources Root.  
    99% of the time Pycharm is smart
    This is the 1%.  It pretends not work.   
"""


# import json, csv, requests

if __name__ == '__main__':
    # module.something
    # print(time.time_ns())

    print(time.time())

    for i in range(1000000):
        i += 1
    print(time.time())

    seed(time.time_ns())
    # what does seed do?
    # what seed does is changes the initial starting parameters for a random number generator
    # pseudo-random, possible that python "may" allow the same seed to happen
    # <attack> if you can get a program to accidentally generate the same seed
    #           your program becomes more vulnerable because the attacker can basically set their seed to your
    #           seed and run the same rng algorithm.

    """
        How does a random number generator work?
        
            There's no such thing as "random." there's only really pseudo-random.
            "Evenly distributed" 
        QBit a|0> + b|1>
            collapse the qbit state -> |0> |1> 
            "Truly Random"
        QBits - Quantum Computer Parts
    """
    counts = [0 for _ in range(100)]

    for i in range(100000):
        counts[randint(0, 99)] += 1

    for i in range(100):
        print(i, counts[i])

    print(random())

    print(5, primes.is_prime(5))
    print(12, primes.is_prime(12))

    # we learned that we can pull in a class type from another file
    # Person is not defined in this file
    # but we can create Person instances
    archie = Person('Archibald')
    hrothgar = Person('Hrothgar the Spear Dane')

    hrothgar.what_is_my_name()
