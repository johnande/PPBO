# Membuat class decorator
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Menggunakan class decorator!")
        return self.func(*args, **kwargs)

# Menggunakan class decorator
@MyDecorator
def greeting(name):
    return "Assalamu'alaikum, " + name + "!"

# Memanggil fungsi yang telah didekorasi
message = greeting("Marsa")
print(message)

