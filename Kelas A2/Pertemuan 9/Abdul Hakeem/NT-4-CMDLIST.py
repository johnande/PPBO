from collections import namedtuple

jane = {"name": "Jane", "age": 25, "height":1.75}

jane["age"] = 26
jane["age"]

jane["weight"] = 67
jane

# equivalent tuple:

person = namedtuple("person", "name age height")
jane = person("Jane", 25, 1.75)
jane
jane.age = 26
jane.weight = 67