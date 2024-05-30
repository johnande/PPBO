from collections import namedtuple

# Definisikan namedtuple untuk buah-buahan
BuahMonokotil = namedtuple('BuahMonokotil', ['nama', 'biji'])
BuahDikotil = namedtuple('BuahDikotil', ['nama', 'biji'])

# Buah-buahan Monokotil
pisang = BuahMonokotil('Pisang', 'tunggal')
kelapa = BuahMonokotil('Kelapa', 'tunggal')

# Buah-buahan Dikotil
apel = BuahDikotil('Apel', 'banyak')
jeruk = BuahDikotil('Jeruk', 'banyak')

# Cetak informasi buah-buahan
print("Buah Monokotil:")
print(pisang)
print(kelapa)

print("\nBuah Dikotil:")
print(apel)
print(jeruk)
