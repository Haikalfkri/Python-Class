## What is Class?
In Python, a class is a blueprint for creating objects (instances of the class) that encapsulate data and the functions that operate on that data. It defines a set of attributes and methods that describe the behavior of the objects that are created from it.

To create a class in Python, you use the class keyword followed by the name of the class. 
For example:

```sh
class MyClass:
    pass
```

This creates a basic class called MyClass that doesn't have any attributes or methods defined. You can then create instances of the class by calling its constructor:

```sh
my_object = MyClass()
```

You can add attributes to a class by defining them in the class body:

```sh
class MyClass:
    my_attribute = 42
```

And you can add methods by defining functions within the class body:

```sh
class MyClass:
    def my_method(self):
        print("Hello, World!")
```

In the example above, the my_method method takes a self parameter, which refers to the instance of the class that the method is called on. You can call this method on an instance of the class like this:

```sh
my_object = MyClass
my_object.my_method() # prints "Hello, World!"
```

Classes are an important part of object-oriented programming, and they provide a powerful way to organize and structure your code.

for more about class in python (https://www.w3schools.com/python/python_classes.asp)