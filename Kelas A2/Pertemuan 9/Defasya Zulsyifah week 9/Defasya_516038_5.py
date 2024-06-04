from collections import namedtuple

# Definisikan namedtuple untuk representasi data tarian
Tarian = namedtuple('Tarian', ['nama', 'asal', 'jenis', 'deskripsi'])

# Buat beberapa instance dari namedtuple Tarian
tarian1 = Tarian('Pendet', 'Bali', 'Tari Sakral', 'Tarian penyambutan
para dewa dalam ritual keagamaan. ')
tarian2 = Tarian('Tari Saman', 'Aceh', 'Tari Tradisional', 'Tarian
grup yang menampilkan gerakan-gerakan indah dan energik.')
tarian3 = Tarian('Tari Tor-Tor', 'Sumatera Utara', 'Tari Adat',
'Tarian ritual yang melibatkan gerakan dan musik tradisional Batak.')

for idx, tarian in enumerate([tarian1, tarian2, tarian3], start=1):
    print(f"Tarian {idx}:")
    print(f"Nama: {tarian.nama}")
    print(f"Asal: {tarian.asal}")
    print(f"Jenis: {tarian.jenis}")
    print(f"Deskripsi: {tarian.deskripsi}")
    print()