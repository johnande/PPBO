# ================================================================= TUGAS 2
class Lingkaran:
    def __init__(self, r):
        self.jari_jari = r
    def luas(self):
        return 3.14 * self.jari_jari * self.jari_jari

lingkaran1 = Lingkaran(5)
lingkaran2 = Lingkaran(10)

print(lingkaran1.luas())
print(lingkaran2.luas())

#================================================================ Tugas 3
class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
    def luas(self):
        return self.sisi * 2
    def keliling(self):
        return self.sisi * 4
    def tampilkan_data(self):
        print("Luas persegi= ", self.luas())
        print("Keliling persegi= ", self.keliling())

persegi1 = Persegi(4)
persegi1.tampilkan_data()

# ================================================================= TUGAS 4
class Shark:
    def __init__(self, name):
        self.name = name
    def swim(self):
        print(self.name + " is swimming.")
    def be_awesome(self):
        print(self.name + " is being awesome.")
def main():
    sammmy = Shark("Sammy")
    sammmy.swim()
    sammmy.be_awesome()
if __name__ == "__main__":
    main()

# ================================================================= Tugas 5
class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))
    
x = input()
print(py_solution().reverse_words(x))

# ================================================================= Tugas 6
class Manusia:
    def __init__(self):
        self.nama = input("Masukkan nama: ")
        self.umur = int(input("Masukkan umur: "))

    def tampilkan_data(self):
        print("nama: ", self.nama)
        print("umur: ", self.umur)

manusia1 = Manusia()
manusia1.tampilkan_data()

# ================================================================= Tugas 7
class py_solution:
    def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x
        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x, -n)
        val = self.pow(x, n//2)
        if n%2 ==0:
            return val*val
        return val*val*x
    
print(py_solution().pow(2, -3));
print(py_solution().pow(3, 5));
print(py_solution().pow(100, 0));

# ================================================================= Tugas 8
class Mahasiswa:  
  def __init__(self, nama, nim):
    self.nama = nama
    self.nim = nim
    
  def tampil(self):
    print("Nama:", self.nama)
    print("NIM:", self.nim)

mahasiswa1 = Mahasiswa("Anto", "519033")
mahasiswa2 = Mahasiswa("Titik", "514777")

mahasiswa1.tampil()
mahasiswa2.tampil()