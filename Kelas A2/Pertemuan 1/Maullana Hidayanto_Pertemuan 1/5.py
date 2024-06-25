import math

def hitung_lingkaran(r) :

    luas = math.pi*(r*r)
    keliling = 2*math.pi*r
    return luas, keliling

# Meminta input jari-jari dari pengguna 
r = int(input("Masukkan Jari-Jari Lingkaran: "))

# Menghitung Keliling dan Luas Lingkaran
luas, keliling = hitung_lingkaran(r)

# Menampilkan Hasil Perhitungan
print ("Luas Lingkaran \t   =",format(luas,'.2f'))
print ("Keliling Lingkaran =",format(keliling,'.2f'))