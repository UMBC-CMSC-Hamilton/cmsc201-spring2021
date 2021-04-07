"""
    A class is a new type
        ints, floats, strings, bool, lists, dictionaries
        class <-- not really a type
            a type maker.

    What kind of things can types have?
        data inside of them (member variables, instance variables)
        functions inside of them.
"""


class Lion:
    """
        Constructor for the lion class.
    """
    # 2x underscore init 2x underscore
    def __init__(self, name):
        self.lion_name = name
        self.position = ''

    def eat(self, food):
        print(self.lion_name, 'eats', food)

    def roar(self):
        print(self.lion_name, 'roars... ROAR!!!!')

    def run(self, destination):
        """
            secret of self is that it knows that the first argument is actually the calling class.
        :param destination:
        :return:
        """
        print(self.lion_name, 'has run to ', destination)
        self.position = destination

    def sleep(self, time):
        print(self.lion_name, 'has slept for {} hours'.format(time))


"""
    Each class has its own variables, it's own data.
    They all kind of share the functions though.
    
    We are making built-in functions for a variable type.  
  
"""

leo_the_lion = Lion('Leo')
hercules = Lion('Hercules')
simba = Lion('Simba')

simba.sleep(5)
# Lion.sleep(simba, 5)
# that's the secret.
# self is actually "simba"
hercules.eat('villager')
# hercules.eat('villager')
# Lion.eat(hercules, 'villager')
leo_the_lion.roar()
# Lion.roar(leo_the_lion)
