Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import namedtuple
>>> jane = {"name": "Jane", "age": 25, "height": 1.75}
>>> jane["age"] = 26
>>> jane["age"]
26
>>> jane["weight"] = 67
>>> jane
{'name': 'Jane', 'age': 26, 'height': 1.75, 'weight': 67}
>>> #Equivalent namedtuple
>>> Person = namedtuple("Person", "name age height")
>>> jane = Person("Jane", 25, 1.75)
>>> jane
Person(name='Jane', age=25, height=1.75)
>>> jane.age =26
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    jane.age =26
AttributeError: can't set attribute
>>> jane.weight = 67
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    jane.weight = 67
AttributeError: 'Person' object has no attribute 'weight'
>>> 