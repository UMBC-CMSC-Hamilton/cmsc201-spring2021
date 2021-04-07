"""
    Let's actually do some recursion

    What is a palindrome?
        racecar
        tacocat
        A man a plan canal panama
        pop
        repaper
        Able was I ere I saw Elba.
        Do geese see God? <-- heh
        Gateman sees name, garageman sees name tag. <-- heh^2

    How can we write a recursive function to determine if something is a palindrome?
        What's the easiest case?
            0 or 1 letter
            '', 'a' 'c', 'e' , 'f' ? palindromes or not? yes
        So now, how do we break down the harder problems into simpler problems?
            pop -> yep how about o? --> yep
            pop -> o
            racecar -> aceca -> cec -> e -> yes
            that -> ha -> no
        Compare the first and last letters and then peel them off and go again.
"""


def recurisve_palindrome(word):
    print(word)
    # base case if the length is 0 or 1, then it's a palindrome by default
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[len(word) - 1]:
            # if they match at front and back, it MAY be a palindrome but we need to keep checking
            return recurisve_palindrome(word[1: len(word) - 1])
        else:
            # if they don't match then nope, return false, we're done.
            # base case, because it doesn't call recurisve_palindrome
            return False


def recursive_palindrome_test():
    split_word = input('Enter a word to test for palindromeness: ').lower().split()
    word = ''
    for part in split_word:
        word += part
    print(recurisve_palindrome(word))


"""
    Project 1 - Mancala <-- 1d list project
    Project 2 - Battleship <-- 2d list project
    Project 3 - hmm... <-- recursion project Family Tree stuff, pathfinding, etc.  
"""

"""
    A "common" problem... hiring interview type question
    
        I want you to display for me all the strings of a's and b's where there are always strictly more a's than b's 
            "in the front of the string"
            
        aab = good
        aba = bad
        aaabaabab <-- works
        aabababab <-- works
        b <-- nope
        ba <-- nope
        baaaaaaa <-- nope
        aabb <-- nope
        aaabb <-- yep that works
"""


# default argument is what happens when you don't provide that argument
def more_as_than_bs(length, difference=0, current_string=''):
    """
        there are iterative solutions... BUT... the recursive solution is just infinitely better.
    :param length: use length to count down to 0, recursively, once it hits zero we'll just print instead of
        recursing more
    :param difference: difference = number of a's - number of b's
    :param current_string:
    """
    if not length:
        print(current_string)
        # returning nothing, just exit the function at the next line
        return
        # equivalent to return None

    # cool
    more_as_than_bs(length - 1, difference + 1, current_string + 'a')
    # trickier
    if difference > 1:
        more_as_than_bs(length - 1, difference - 1, current_string + 'b')


#  more_as_than_bs(int(input()))


