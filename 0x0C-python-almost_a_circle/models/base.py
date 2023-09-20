#!/usr/bin/python3
""" A module containing the base class prototype """


import json
import csv
import turtle


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
        function that saves a list of dictionaries to a json file

        Args:
            list_objs: the list of dicts
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            with open(filename, "w") as f:
                f.write("[]")
        else:
            list_objsc = list_objs.copy()
            for i in range(len(list_objsc)):
                list_objsc[i] = list_objsc[i].to_dictionary()
            with open(filename, "w") as f:
                f.write(Base.to_json_string(list_objsc))

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
            dummy = Rectangle(1, 1)
            dummy.update(**dictionary)
            mydict = dummy.to_dictionary()
            return cls(**(dummy.to_dictionary()))
        else:
            dummy = Square(1)
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        function that saves a list to a csv file

        Args:
            list_objs: a list of the objects to be saved in the file
        """
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            with open(filename, "w") as f:
                csvw = csv.writer(f)
                csvw.writerow(["id", "width", "height", "x", "y"])

                data = []
                list_obj = [obj.to_dictionary() for obj in list_objs]
                for i in list_obj:
                    li = [0, 0, 0, 0, 0]
                    li[0] = i["id"]
                    li[1] = i["width"]
                    li[2] = i["height"]
                    li[3] = i["x"]
                    li[4] = i["y"]
                    data.append(li)
                for i in data:
                    csvw.writerow(i)
        else:
            with open(filename, "w") as f:
                csvw = csv.writer(f)
                csvw.writerow(["id", "size", "x", "y"])
                data = []
                list_obj = [obj.to_dictionary() for obj in list_objs]
                for i in list_obj:
                    li = [0, 0, 0, 0]
                    li[0] = i["id"]
                    li[1] = i["size"]
                    li[2] = i["x"]
                    li[3] = i["y"]
                    data.append(li)
                for i in data:
                    csvw.writerow(i)

    @classmethod
    def load_from_file_csv(cls):
        """
        function that creates an instance from a csv file

        Returns:
            returns a list of instances
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "r") as f:
            li = []
            csvr = csv.DictReader(f)
            for i in csvr:
                li.append(cls.create(**i))
            return li

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#47ee29")
        turt.pensize(2)
        turt.shape("turtle")

        turt.color("#ffffff")
        last = 0
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y + last)
            last += rect.height
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#ffffff")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y + last)
            last + sq.height
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
