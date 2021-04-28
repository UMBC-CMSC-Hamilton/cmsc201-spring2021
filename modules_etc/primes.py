def is_prime(n):
    """
    :param n: an integer
    :return: True if Prime, False if Not Prime.

    # this runs in O(sqrt(N)) time cool, don't really care.
    """
    for i in range(2, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            return False

    return True


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('Blah blah blah')

    def walk(self):
        pass

    def what_is_my_name(self):
        print("My name is {}".format(self.name))
