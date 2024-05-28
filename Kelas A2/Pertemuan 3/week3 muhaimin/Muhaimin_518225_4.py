class Koordinat2D:
    x=0
    y=0
    
    def __init__ (self,x,y):
        self.x=x
        self.y=y
class Koordinat3D(Koordinat2D):
    z=0
    
    def __init__(self,x,y,z):
        super(). __init__(x,y)
        self.z=z
    def tampilkan_lok(self):
        print("x = ", self.x)
        print("y = ", self.y)
        print("z = ", self.z)
titik1=Koordinat3D(1,2,3)
titik1.tampilkan_lok()
