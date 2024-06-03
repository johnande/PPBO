
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
        print('y =', self.y)
        print('z =', self.z)

# Membuat sebuah instance dari kelas Koordinat3D
titik1 = Koordinat3D(10, 20, 30)

# Tidak perlu menghapus atribut y karena kita ingin mencetaknya nanti

print('efek keyword del')
titik1.tampilkan_koord()