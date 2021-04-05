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


split_word = input('Enter a word to test for palindromeness: ').lower().split()
word = ''
for part in split_word:
    word += part
print(recurisve_palindrome(word))
