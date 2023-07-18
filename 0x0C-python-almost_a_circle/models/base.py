#!/usr/bin/python3
"""
Module Docs
"""
from json import dumps, loads
from os.path import isfile
import csv
import turtle
from random import randint, shuffle, randrange


class Base:
    """
    Class Docs
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Function Docs
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Function Docs
        """

        if type(list_dictionaries) is list:
            if len(list_dictionaries) == 0:
                return dumps([])
            else:
                return dumps(list_dictionaries)
        elif list_dictionaries is None:
            return dumps([])

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Function Docs
        """

        if list_objs is None:
            final_list = []
        else:
            final_list = [i.to_dictionary() for i in list_objs]
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as f:
            f.write(Base.to_json_string(final_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Function Doc
        """

        if type(json_string) is str:
            if len(json_string) == 0:
                return []
            else:
                return loads(json_string)
        elif json_string is None:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        Function Doc
        """

        if cls.__name__ == "Rectangle":
            dummy_obj = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_obj = cls(1)
        else:
            dummy_obj = cls()
            return dummy_obj
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """
        Function Doc
        """

        filename = "{}.json".format(cls.__name__)
        obj_list = []
        if isfile(filename):
            with open(filename, "r") as f:
                line = f.readline()
                final_list = Base.from_json_string(line)
            for i in final_list:
                class_created = cls.create(**i)
                obj_list.append(class_created)
        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        function docs
        """

        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode='w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',',
                                    quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)
            for i in list_objs:
                i_list = cls.to_list(i)
                csv_writer.writerow(i_list)

    @classmethod
    def load_from_file_csv(cls):
        """
        function docs
        """
        filename = "{}.csv".format(cls.__name__)
        obj_list = []
        if isfile(filename):
            final_list = []
            with open(filename, "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    obj_dict = cls.parse_csv(row)
                    final_list.append(obj_dict)
            for i in final_list:
                class_created = cls.create(**i)
                obj_list.append(class_created)
        return obj_list

    @classmethod
    def parse_csv(cls, row):
        """
        Function doc
        """

        dictionary_row = {}
        if type(row) is list:
            dictionary_row["id"] = row[0]
            if cls.__name__ == "Rectangle":
                if len(row) == 5:
                    dictionary_row["width"] = row[1]
                    dictionary_row["height"] = row[2]
                    dictionary_row["x"] = row[3]
                    dictionary_row["y"] = row[4]
            elif cls.__name__ == "Square":
                if len(row) == 4:
                    dictionary_row["size"] = row[1]
                    dictionary_row["x"] = row[2]
                    dictionary_row["y"] = row[3]
        return dictionary_row

    @classmethod
    def to_list(cls, obj_item):
        """
        Function doc
        """

        list_item = []
        if isinstance(obj_item, Base):
            list_item.append(obj_item.id)
            if cls.__name__ == "Rectangle":
                list_item.append(obj_item.width)
                list_item.append(obj_item.height)
            elif cls.__name__ == "Square":
                list_item.append(obj_item.size)
            list_item.append(obj_item.x)
            list_item.append(obj_item.y)
        return list_item

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Function doc
        """

        new_list = list_rectangles + list_squares
        try:
            turtle.title("21. Let's draw it")
            screen = turtle.getscreen()
            turtle.bgcolor("black")
            t = turtle.Turtle()
            turtle.colormode(255)

            def exit_on_click(i, j):
                screen.exitonclick()

            screen.onclick(exit_on_click)
            screen.listen()
            r = False
            while True:
                if r:
                    shuffle(new_list)
                height = 0
                width = 0
                direction = randrange(4)
                for i in range(len(new_list)):
                    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
                    t.begin_fill()
                    t.pendown()
                    for j in range(2):
                        t.fd(new_list[i].width)
                        t.rt(90)
                        t.fd(new_list[i].height)
                        t.rt(90)
                    t.end_fill()
                    t.penup()
                    if direction == 0:
                        if i != len(new_list) - 1:
                            width += new_list[i].width + 10
                    elif direction == 1:
                        if i != len(new_list) - 1:
                            width += -new_list[i + 1].width - 10
                    elif direction == 2:
                        if i != len(new_list) - 1:
                            height += new_list[i + 1].height + 10
                    elif direction == 3:
                        if i != len(new_list) - 1:
                            height += -new_list[i].height - 10
                    t.goto(width, height)
                t.goto(0, 0)
                t.clear()
                r = True
        except Exception:
            print("Goodbye!")
