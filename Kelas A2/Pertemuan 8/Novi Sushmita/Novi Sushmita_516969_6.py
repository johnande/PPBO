from collections import namedtuple

jane = {"name": "jane", "age":25, "height":1.75}
jane["age"] = 26
jane["age"]
jane["height"] = 67
jane

Person = namedtuple("Person", "name age height")
jane = Person("jane", 25, 1.75)
jane
jane.age = 26
jane.height = 67