"""
    Objective: ask the user if they have a bunch of stuff
        If they can bake a single batch of cookies based on their inputs.

    2 1/4 cups all-purpose flour
    2 large eggs
    1 cup (2 sticks) butter, softened
    3/4 cup granulated sugar
    3/4 cup packed brown sugar
    2 cups Semi-Sweet Chocolate Chips 1 bag of chocolate chips (too much)

    won't ask about:
    1 teaspoon vanilla extract
    1 teaspoon salt
    1 teaspoon baking soda

"""
# 2.25 aka 2 + 1/4 cup of flour. 9/4
# 2 1/4 cup in baking ... ok
flour_quantity = float(input('How much flour do you have (in cups)? '))
if flour_quantity >= 9/4:
    # assume no fractional eggs exist
    eggs = int(input('Good you have the flour for this job, now... how many eggs do you have? '))
    if eggs >= 2:
        # you can argue that maybe we can use a float, i don't care
        butter = int(input('Good so far, how many sticks of butter do you have? '))
        if butter >= 2:
            yes_no = input('Do you have 3/4 cup of granulated sugar and 3/4 cup of brown sugar? ')
            # this is in lower case
            # if yes_no == 'yes' or yes_no == 'Yes' or yes_no == 'YES':
            if yes_no.lower() == 'yes':
                #  you are permitted to use .lower() method
                # \' escape sequence it allows us to use the ' as a character rather than a
                #                       string terminator
                print('Alright you\'re good to go')
            else:
                print('You need some more sugar.')
        else:
            print('Moo... get to the store.')
    else:
        print('Get some chickens, make some eggs, you know the drill. ')
else:
    print('Go to the store and buy flour. ')

