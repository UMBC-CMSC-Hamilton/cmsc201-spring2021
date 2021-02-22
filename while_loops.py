if False:
    # as a string:
    phone_number = input('Tell me your phone number: ')
    # by default, split splits on whitespace
    # if you stick a string into the split argument, then you'll split on that
    split_number = phone_number.split('-')

    # nothing happens to the original string
    print(phone_number)
    # this is a list of little substrings
    print(split_number)
    # to access elements in a list:
    print(split_number[0], split_number[2], split_number[1])

    full_name = input('Tell me your full name: ')
    # without any special marking inside of the argument
    # hitting enter will end input
    print(full_name.split())
    weird_string = """
    Hello there.
    
    \t\tThis string is going to have some tabs.
    \t\tAnd also some endlines.
    """
    print(weird_string)
    print(weird_string.split())

    # without it...

    my_key = '123-2244667'
    # you technically have all the knowledge you need to avoid using split for this problem.
    first_part = ''
    second_part = ''
    # boolean flag <-- flag variable is a variable which marks when you find something, or a condition
    found = False
    for c in my_key:
        if not found and c != '-':
            first_part += c
        elif c == '-' and not found:
            found = True
        else:
            second_part += c

    print(first_part, second_part)

    """
    Let's begin on while loops
    """

    password = 'fluffy bunny'  # the best idea <-- ;-)
    entered_password = input('Enter your password: ')  # can't get back up to this line
    # password is a sentinel value <-- a value that is watched for and then either execute code jump out of a loop
    # when it happens.
    while password != entered_password:
        print('Wrong password')
        entered_password = input('Enter your password: ')  # we need to make sure that we get a new password
    print('You\'re in the system')
    # advantage here:  this will keep the user stuck in the password screen/entering thing forever until they
    # give up and tell you the right password.

    list_of_movies = []
    # prime the input
    movie = input('Tell me a movie: ')  # before we're in the while loop!
    # priming the pump <-- if you've heard that phrase
    while movie.lower() != 'quit':
        list_of_movies.append(movie)
        # if you don't put this here, that's infinite loop time.
        # this loop wont run forever, because yes, you will eventually run out of ram.
        movie = input('Tell me a movie: ')

    print(list_of_movies)

    """
        "While loops are more powerful than for loops"
        everything you can do with a for loop you can do with a while loop.  
            To prove this, all i need to do is construct a while loop that does the for loop type of thing
    """

    # we want to replicate this functionality
    # for is checking to make sure that 0 <= i < len(list_of_movies)
    # also whenever you come back to the for line, it adds one to i rechecks
    for i in range(len(list_of_movies)):
        # who cares about this, but it's a line of code
        print(list_of_movies[i])

    i = 0  # to start
    while i < len(list_of_movies):
        # whatever code
        print(list_of_movies[i])
        # end of whatever code
        # i = i + 1
        i += 1

    # in general, when you are doing this kind of operation, scanning though a list, use a for loop 99% of the time
    # BUT you can use a while loop for it if you're in a bind.
    i = 0  # to start
    while i < len(list_of_movies):
        # whatever code
        print(list_of_movies[i])
        # end of whatever code
        # i = i + 1
        # either 1 or 2 based on user input...
        if input('Skip or nah?').lower() == 'skip':
            i += 2
        else:
            i += 1

    # This is a good justification for using a while loop in this particular case
    # but that is a kind of weird case, i don't know why you'd want to do that...

    # forbidden
    import random

    the_number = random.randint(1, 100)
    #  number guesser
    # priming the input here...
    guess = int(input('Tell me a number: '))
    while guess != the_number:
        if guess < the_number:
            print('Go Higher')
        elif guess > the_number:
            print('Go Lower')
        guess = int(input('Tell me a number: '))

    # why can't this be a for loop?
    # the answer is... because you don't know how many guesses the user will take

    """
        games <-- while (someone didn't win)
        input validation <-- kind of what we've been doing with the passwords and stuff like that.  
            What I don't mean: type validation
            What I do mean: for the correct values within a type 
        while loops for GUI <Graphical user Interfaces> programs (while a messages comes in, do some processing)
        server programs (while the server is running, do the following things)
    """
    # trust us we're not going to break your code intentionally
    pos_int = int(input('Tell me a positive integer: '))
    while not (pos_int > 0):
        pos_int = int(input('That was not positive, please try again.  Tell me a positive integer: '))

    print(pos_int)
# enter a size of a grid
# user enters -45, -2
# you should not allow that
# your code may actually break with garbage input
# always good to think: How am I going to prevent the relatively insane user hammers keys 'at random' from
# breaking my code?

# generally in this class don't fix input for the user, just reprompt
# if the user enters the wrong type, your program is permitted to die.
# ValueError is the "correct result" for this
# If you catch it using try/except then we're gonna have to yell at you for using forbidden arts.

# approximation example i like to do.

# a_{n + 1} = (1/2)(a_n + x / a_n)

# to actually square root a number x ** (1/2)

a_number = float(input('Tell me a number to take the square root of: '))
# 100% legal < also very cool, very legal
previous = float(input('Guess what the answer is: '))
current = previous + 1
while abs(current - previous) > 0.0001:
    previous = current
    current = 0.5 * (current + a_number / current)
    print('The current guess is', current)

print(current, a_number ** (1/2))
"""
    It shows that we dont' know how long this approx technique is going to run.
        While the accuracy isn't satisfied, keep going. Perfect job for a while loop.  
    Almost impossible to know how many times you need to run it so a for loop is not really the right answer.
        for loops = Almost certainly the very wrong answer
    I don't know how many times the thing is going to run.  
    I want it to run while some condition is true.  

    Big Danger: infinite loops.  
"""
