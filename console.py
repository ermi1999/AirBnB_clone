#!/usr/bin/python3
"""
This is the command interpreter for hbnb.
"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    This is the command interpreter for hbnb.
    """
    __classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
    prompt = "(hbnb) "

    def default(self, line):
        """
        overides the default behavior to handle some commands.
        """
        list_methods = ["all", "count", "destroy", "show", "update"]
        list_static_methods = ["count", "all"]
        if line:
            arg = line
            if '.' in arg and '(' in arg and ')' in arg:
                if arg[-1:] == ')':
                    arg = arg.split('.')
                    if len(arg) > 1:
                        class_name = arg[0]
                        if class_name in self.__classes:
                            instance_method = arg[1]
                            arg = instance_method.split('(')
                            instance_method = arg[0]
                            if instance_method in list_methods:
                                arg = arg[1]
                                arg = arg[:-1]
                                if instance_method in list_static_methods:
                                    instance_method = "self.{}".format(instance_method)
                                else:
                                    instance_method = "self.do_{}".format(instance_method)
                                if arg and arg[-1:] == '}':
                                    arg = arg.split(',', 1)
                                    if len(arg) == 2:
                                        id = arg[0]
                                        id = id.replace('"', '')
                                        id = id.replace("'", "")
                                        dictionary = arg[1]
                                        try:
                                            dictionary = dictionary.replace("'", '"')
                                            dictionary = json.loads(dictionary)
                                            for key, value in dictionary.items():
                                                arg = "{} {} {} {}".format(class_name, id, key, value)
                                                eval(instance_method) (arg)
                                            return
                                        except Exception as e:
                                            pass
                                else:
                                    if arg:
                                        arg = arg.replace('"', '')
                                        arg = arg.replace('"', '')
                                        arg = "{} {}".format(class_name, arg)
                                        eval(instance_method) (arg)
                                    else:
                                        eval(instance_method) (class_name)
                                    return
        super().default(line)

    @staticmethod
    def count(class_name):
        """
        retrieves the number of instances of a class.
        """
        all_obj = storage.all()
        count = 0
        for obj in all_obj.values():
            if class_name == obj.__class__.__name__:
                count += 1
        print(count)

    @staticmethod
    def all(class_name):
        """
        prints all the instances of the class.
        """
        result = []
        all_obj = storage.all()
        for obj in all_obj.values():
            if class_name == obj.__class__.__name__:
                result.append(obj.__str__())
        output = '[' + ', '.join(result) + ']'
        print(output)

    def do_create(self, line):
        """
        creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        args = line.split()
        if len(args) > 0:
            arg = args[0]
            if arg in self.__classes:
                all_obj = storage.all()
                new_class = eval(arg) ()
                new_class.save()
                print(new_class.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        """
        prints help message for create.
        """
        print("creates a new instance of BaseModel\nsaves it to JSON file.\n")
        print("ARGS:\n\t1. The class name.")


    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on the class name and id.
        """
        args = line.split()
        if len(args) > 0:
            class_name = args[0]
            if class_name not in self.__classes:
                print("** class doesn't exist **")
            else:
                if len(args) > 1:
                    id = args[1]
                    all_obj = storage.all()
                    obj_id = "{}.{}".format(class_name, id)
                    if obj_id in all_obj:
                        print(all_obj[obj_id])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
        else:
            print("** class name missing **")
    
    def help_show(self):
        """
        prints help for show.
        """
        print("Prints the string representation of an instance based on the class name and id.")
        print("ARGS:\n\t1. class name\n\t2. class id to be printed.")

    def do_quit(self, line):
        """
        quits the cmd
        """
        return True

    def help_quit(self):
        """
        prints the help for quit.
        """
        print("Quit command to exit the program\n")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        """
        args = line.split()
        all_obj = storage.all()
        if len(args) > 0:
            class_name = args[0]
            found = 0
            for obj in all_obj.values():
                if class_name == obj.__class__.__name__:
                    found = 1
                    break
            if found:
                if len(args) > 1:
                    id = args[1]
                    obj_id = "{}.{}".format(class_name, id)
                    if obj_id in all_obj:
                        del all_obj[obj_id]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_destroy(self):
        """
        prints help for destroy.
        """
        print("Deletes an instance based on the class name and id\nArgs: \
                \n\t1. the class name\n\t2. the id of the object to delete")

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        args = line.split()
        result = []
        all_obj = storage.all()
        if len(args) > 0:
            class_name = args[0]
            for obj in all_obj.values():
                if obj.__class__.__name__ == class_name:
                    result.append("{}".format(obj.__str__()))
        else:
            for obj in all_obj.values():
                result.append("{}".format(obj.__str__()))
        if len(result) == 0:
            print("** class doesn't exist **")
        else:
            print(result)

    def help_all(self):
        """
        prints the help for all.
        """
        print("Prints all string representation of all instances based or not on the class name.\nArgs:\
                \n\t1. class name (optional)")

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute.
        """
        args = line.split()
        all_obj = storage.all()
        if len(args) > 0:
            class_name = args[0]
            found = 0
            for obj in all_obj.values():
                if class_name == obj.__class__.__name__:
                    found = 1
                    break
            if found:
                if len(args) > 1:
                    id = "{}.{}".format(class_name, args[1])
                    if id in all_obj.keys():
                        instance = all_obj[id]
                        if len(args) > 2:
                            attr = args[2]
                            if len(args) > 3:
                                if isinstance(args[3], str):
                                    value = args[3].replace('"', '')
                                if hasattr(instance, attr):
                                    previous_type = type(getattr(instance, attr))
                                    value = previous_type(args[3])
                                setattr(instance, attr, value)
                                storage.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_update(self):
        """
        prints help for update.
        """
        print("Updates an instance based on the class name and id by adding or updating attribute.\nARGS:\
                \n\t1. class name\n\t2. the id of the object\n\t3. attribute name\n\t4. attribute value")


    def do_EOF(self, line):
        """
        quits the program.
        """
        print()
        return True

    def emptyline(self):
        """
        when empty line is incountered do nothing.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

