"""
    Let's talk about json
"""
import json

"""
    Two important functions:
    
    json.loads() : string-> dictionary
    
    json.dumps() : dictionary -> string
    
    Why do we want a string object?
        String are savable into files.
        
"""


class Toy:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    def dump_toy(self):
        return {'name': self.name, 'weight': self.weight, 'color': self.color}

    def load_toy(self, toy_dictionary):
        self.name = toy_dictionary['name']
        self.weight = toy_dictionary['weight']
        self.color = toy_dictionary['color']


def write_json():
    test_dict = {'hello': 5, 'goodbye': 17, 't-rex': 4, 'who knows': 3391}

    t = Toy('ball', 0.25, 'red')

    my_raw_materials = {'Iron': 3, 'Copper': 2, 'Silicon': 1}
    my_recipes = {'iron rod': [('Iron\n\r', 2)]}
    my_total_structure = {'recipes': my_recipes, 'raw': my_raw_materials, 'the_toy': t.dump_toy()}

    write_json_file = open('test.json', 'w')
    # create the string
    string_to_write = json.dumps(my_total_structure)
    # write the string into the file.
    #
    write_json_file.write(string_to_write)
    # this could result in a file left open after the program terminates, could be bad
    write_json_file.close()


def read_json():
    read_file = open('test.json', 'r')
    # just a string with the json stuff read in.
    json_string = read_file.read()
    # just call read once, get everything out of the file.
    data = json.loads(json_string)
    print(data)
    t = Toy('', '', '')
    t.load_toy(data['the_toy'])
    print(t)
    # this has successfully translated from data in ram -> file -> the same data in ram


# write_json()
# read_json()
