import random


class WarpDrive:
    def __init__(self, max_speed, dilithium_per_second, singularity=False):
        # for default parameters, it sets it to whatever it is equal to if you don't include that parameter
        # the spaces PEP-8 standard says no spaces between var=default
        # for this class who cares?

        self.max_speed = max_speed
        self.dps = dilithium_per_second
        self.singularity = singularity
        # Romulans used Quantum Singularities (mini-black holes) somehow for their drives.


class Starship:

    # constructor.
    # what is a constructor?
    #   whenever you create a new instance of a class, this is the function that runs.
    # what do you do in this function?
    #   set up instance variables, and get it ready to be useful.
    def __init__(self, name, hull_number, crew_size):
        self.ship_name = name
        self.hull_number = hull_number  # note here there are TWO VARIABLES in this line
        # one is called hull_number, that's a parameter of the function __init__ NOT a member variable of the class
        # the other one is self.hull_number which is the member variable.
        # whenever you need to save a variable for as long as the class is alive, make sure you do self.whatever = something

        self.crew_size = crew_size
        # you can make lists and even dictionaries as member variables!
        # you can even have a class as a member variable!
        self.crew = []

    def set_engine(self, warp_engine):
        self.warp_engine = warp_engine

    def add_crew_member(self, crew_member):
        """
        This is a member function, it only runs when the user of the class calls it directly.
        :param crew_member:
        :return:
        """
        # this one is a local variable, it only lives as long as this function is running,
        # NOT as long as the class
        # is alive
        if crew_member not in self.crew:
            self.crew.append(crew_member)
        else:
            print('Hey that person is already aboard.  ')

    def display_crew(self):
        for crew_member in self.crew:
            print(crew_member)


def star_trek():
    enterprise_d = Starship('Enterprise-D', 1701, 1014)
    enterprise_d.add_crew_member('Picard')
    # Starship.add_crew_member(enterprise_d, 'Picard')
    enterprise_d.add_crew_member('Riker')
    enterprise_d.add_crew_member('Troi')
    enterprise_d.add_crew_member('Data')
    enterprise_d.add_crew_member('Geordi')
    enterprise_d.add_crew_member('Worf')

    enterprise_d.display_crew()  # enterprise d is self here
    # enterprise_d.display_crew() -> Starship.display_crew(enterprise_d)
    #
    print(enterprise_d.ship_name)
    enterprise_d_as_a_dictionary = {'ship_name': 'Enterprise D', 'Hull Number': 1701, 'crew_size': 1014}
    if False:
        # cannot do this
        print(enterprise_d_as_a_dictionary.ship_name)
        # can do this
        print(enterprise_d_as_a_dictionary['ship_name'])

    voyager = Starship('Voyager', 74656, 152)
    voyager.add_crew_member('Janeway')  # voyager is self.
    voyager.add_crew_member('Tuvok')
    voyager.add_crew_member('Harry Kim')
    voyager.add_crew_member('Seven of Nine')
    voyager.add_crew_member('Neelix')

    voyager.display_crew()
    # Starship.display_crew(voyager)
    # which one are we referring to? Enterprise D or Voyager?
    # python needs to know when it does this weird translation

    original_enterprise = Starship('Enterprise', 1701, 400)

    original_enterprise.add_crew_member('Kirk')
    original_enterprise.add_crew_member('Spock')
    original_enterprise.add_crew_member('McCoy')
    original_enterprise.add_crew_member('Scotty')
    original_enterprise.add_crew_member('Sulu')
    original_enterprise.add_crew_member('Chekov')
    original_enterprise.add_crew_member('Uhura')
    original_enterprise.add_crew_member('Nurse Chapel')  # never forget her.

    original_enterprise.display_crew()

    original_enterprise_drive = WarpDrive(8.0, 0.1234)
    original_enterprise.set_engine(original_enterprise_drive)

    new_drive = WarpDrive(9.95, .2211, False)
    enterprise_d.set_engine(new_drive)

    # here is a cautionary note.
    # classes are mutable, THEREFORE they always pass by reference into functions.
    voyager.set_engine(new_drive)
    # hey voyager has a faster top speed or something
    voyager.warp_engine.max_speed = 9.975
    # here's the point.
    print(voyager.warp_engine.max_speed)
    print(enterprise_d.warp_engine.max_speed)
    # huh... that's weird. (not really that weird but maybe unexpected).

    # reference = there is an underlying object in memory somewhere, it can have multiple different names
    # python might call it class_389293847238 we call it new_drive, self.warp_drive


# frogger <-- the game


