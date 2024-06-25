#No4b

class Koordinat2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Koordinat3D(Koordinat2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def tampilkan_koord(self):
        print('x =', self.x)
        if hasattr(self, 'y'):
            print('y =', self.y)
        else:
            print('y attribute does not exist')
        if hasattr(self, 'z'):
            print('z =', self.z)
        else:
            print('z attribute does not exist')

titik1 = Koordinat3D(1, 2, 3)
titik1.tampilkan_koord()

delattr(titik1, 'z')
print('efek fungsi delattr()')
titik1.tampilkan_koord()

del titik1.y
print('efek keyword del')
titik1.tampilkan_koord()
