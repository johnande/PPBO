Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import namedtuple
>>> jane = {"name": "Jane", "age": 25, "height": 1.75}
>>> jane["age"] = 26
>>> jane["age"]
26
>>> jane["weight"] = 67
>>> jane
{'name': 'Jane', 'age': 26, 'height': 1.75, 'weight': 67}
>>> # Equivalent named tuple
>>> Person = namedtuple("Person", "name age height")
>>> jane = Person("Jane", 25, 1.75)
>>> jane
Person(name='Jane', age=25, height=1.75)
>>> jane.age = 26
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    jane.age = 26
AttributeError: can't set attribute
>>> jane.weight = 67
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    jane.weight = 67
AttributeError: 'Person' object has no attribute 'weight'
