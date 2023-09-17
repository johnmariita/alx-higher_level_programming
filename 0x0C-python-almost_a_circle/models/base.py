#!/usr/bin/python3
""" A module containing the base class prototype """


import json


class Base:
    """ Base class implementation """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization of the Base class """
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        function that returns a json string from a list of dicts

        Args:
            list_dictionaries: the list containing dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        function that saves a list of dictionaries to a file

        Args:
            list_objs: the list of dicts
        """
        list_objsc = list_objs.copy()
        filename = cls.__name__ + ".json"
        for i in range(len(list_objsc)):
            list_objsc[i] = list_objsc[i].to_dictionary()
        with open(filename, "w") as f:
            json.dump(list_objsc, f)

    @staticmethod
    def from_json_string(json_string):
        """
        function that returns an object from a json string

        Args
            json_string: the json string to be parsed
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        function that returns an instance to create an object

        Args:
            dictionary: key-worded arguments to create the instance
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ == "Rectangle":
            dummy = Rectangle(1, 1, 1, 1, 1)
            dummy.update(**dictionary)
            mydict = dummy.to_dictionary()
            return cls(**(dummy.to_dictionary()))
        else:
            dummy = Square(1, 1, 1, 1)
            dummy.update(**dictionary)
            mydict = dummy.to_dictionary()
            return cls(**(dummy.to_dictionary()))

    @classmethod
    def load_from_file(cls):
        """
        function that gets a json string from a file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                json_string = cls.from_json_string(f.readline().rstrip())

            for i in range(len(json_string)):
                json_string[i] = cls.create(**json_string[i])

            return json_string
        except FileNotFoundError:
            return []
