#No6b

from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "height", "weight"])

jane = Person(name="Jane", age=25, height=1.75, weight=None)

print(jane.age)

jane = jane._replace(age=26)

jane = jane._replace(weight=67)

print(jane)
