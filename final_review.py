my_list = [1, 2, 3, 5, 7, 2, 4, 6, 3, 5, 3, 2, 3, 5, 3, 2]

"""
    For i loop because the index is used.  
"""

current_max = 0
for i in range(len(my_list)):
    if my_list[i] > current_max:
        current_max = my_list[i]

print(current_max)

"""
    For each loop: 
       iterate through the actual elements of a list, dictionary, object, whatever.  
"""
cur_max_for_each = 0
for x in my_list:
    if x > cur_max_for_each:
        cur_max_for_each = x

print(cur_max_for_each)

"""
    Primary Trick/Non-distinction/Error:
        for i in something:
         for i loop, no!!!!!!!
    Even if the variable is called i, that doesn't matter, check whether it's an index or an element!
"""

count = 0
n = int(input('Enter an integer: '))
while n > 0:
    n //= 3
    count += 1
    print(n)

print(count)

"""
    When should I use a while loop over a for loop?
        99% answer for this is: whenever you don't know how many times the loop will run.
            len(my_list) <-- pretend that we "know this"  
            
        0,... N <-- for territory
        there's a list you want to iterate through -> for
        getting user input, user might screw up a few times -> while
        running a server, running graphics user interface -> while
        mathematical approximation things (while the error is bigger than some specified amount) -> while  
        
        While loops don't have to run, run 0 times if the first condition is false.  
        While loops generally have the fun feature that they can run forever, infinite loop.                

    y = 15
    while x > 0:
        y -= 1
        print(y)
    
    print('done')

    "Most/nearly all - 0.00000001% for loops can't be infinite loops"
"""


# infinite for loop in python.
# this is definitely an exception; not the rule.
def inf_for():
    my_list = [1, 2, 3, 4, 5]
    for x in my_list:
        my_list.append(x + 1)
        print(my_list)


"""
    Functions - also a form of repetition.  
        allow code to be repeated from other points of your program.  
        
        Allow abstraction to start.  
        
        Advantages: allow local variables.
            You can do some intermediate processing/calculation.  
            Whatever var name you pick won't be taken up in the global space.  
            No one has to worry about you accidentally changing their own local variables, generally other globals.
        
        When we teach a rule: "global variables are bad"
            What we're actually saying: "avoid the use of globals NOT because they're bad, but because it improves 
                your own code.  You want your code to run correctly regardless of what other people do in other functions."  
                If your function has a problem, then you know:
                    1) the input is bad (other code is wrong)
                    2) the function is bad (the function's code needs to be fixed). 
                This is good!
            What is the hardest part of coding?
                Spend 10 minutes coding something.  (Globals can decrease this coding time from 10 -> 5 minutes)
                Spend 50 minutes debugging that thing.  (if there's a bug, debug/testing time go up from 50-> 100)
"""

"""
    Some other things about functions?
        Functions take arguments (values sent in), sent in as parameters (local variables inside the function).
        Coding interview questions.    
"""


def f(x):
    return x ** 2 + 2 * x + 3


print(f(3))
# 3 is the argument, x in the f function is the parameter.

"""
    Scope:
    **** PYTHON SPECIFIC ****
    
    Mutable vs Immutable parameters 
        Mutable - passed by reference
        Immutable - passed by value
  
    Passing by value - we're going to make a copy of the argument, and pass that copy into the function
        the copy cannot modify the original (global/outside of the function) variable.    
    Passing by reference - we don't make a copy.  "The local variable is a reference to the variable 
        outside of the function."  Secretly, the parameter is actually just a renamed variable from the
        "global/outside" scope.
        
    C++ thing
        int my_function(int & my_ref) {...}  // pass by reference
        int my_function(int my_ref) {...} // pass by value
          
"""


def edit_my_string(the_string: str):
    the_string = the_string.replace('a', 'b')
    print(the_string)


the_big_string = 'able baker charlie dog'
edit_my_string(the_big_string)
# the_big_string out here was not changed!!!
# why?  we didn't return it! sure but that's not 100% an answer because
#   the_big_string "goes into the" edit_my_string function
#   the_string (the local name for the_big_string) gets changed
#   but wait, the_big_string is not changed
print(the_big_string)


# it passes by value! -> it makes a copy and that copy only has local scope.

def modify_my_list(definite_not_the_list):
    for x in definite_not_the_list:
        if x == 3:
            the_list.append(17)


the_list = [1, 2, 3, 4, 5]


def tricky_string_mod(my_list_of_strings):
    """
        Is this good? no.

        Is this tricky? yes.

        Is it kinda silly? also yes.
    :param my_list_of_strings:
    :return:
    """
    for i in range(len(my_list_of_strings)):
        if my_list_of_strings[i] == 'a':
            my_list_of_strings[i] = 'b'
        else:
            my_list_of_strings[i] = my_list_of_strings[i]
    # my_list_of_strings[0] = my_list_of_strings[0].replace('a', 'b')


tricky_list = list('able baker charlie dog')
tricky_string_mod(tricky_list)
print(''.join(tricky_list))

"""
    Next time on CMSC 201:
        1) Actual coding examples
        2) Recursion/Classes
        3) Future Python (python list comprehensions, ternary expressions, etc.)
            Well actually the list of things you "should know" is essentially infinite
            Time = finite
            ThingsWeTeach subset ThingsYouShouldKnow
"""

"""
    Announcements:
        The final exam will come out the 14th.  Due the 21st.  
        
        MCQ section on blackboard.  
        
        Project 3 due this Friday.
        
        Try to do the new submit system test.  It's worth 20 pts (basically free points, not extra credit).
        Replaced the Academic integrity quiz.  
          
    Goal: go over the previous semester's final exam.  
        
"""