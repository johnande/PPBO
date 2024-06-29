class Myname:
    def __init__(self, nama):
        self.nama = nama

x = Myname("fatih")
print(x.nama)

delattr(x, 'nama')
print(x.nama)