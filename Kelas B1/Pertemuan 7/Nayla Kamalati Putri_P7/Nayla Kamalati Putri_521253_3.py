#No3

def add_greeting(cls):
  def greeting(Self):
    print(f"Hello, I am a {Self.__class__.__name__}!")
  cls.greeting = greeting
  return cls

@add_greeting
class MyClass:
  pass

obj = MyClass()
obj.greeting()
