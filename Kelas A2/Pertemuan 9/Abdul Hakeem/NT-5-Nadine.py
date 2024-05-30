from collections import namedtuple

# Mendefinisikan namedtuple 'Mahasiswa' dengan atribut 'nama', 'nim', dan 'jurusan'
hewan = namedtuple('hewan', ['nama', 'habitat', 'jenis'])

# Membuat instance dari namedtuple 'Mahasiswa'
harimau = hewan('harimau', 'Darat', 'Karnivora')
lumbalumba = hewan('lumba-lumba', 'Laut', 'Karnivora')

print(f'Hewan pertama adalah seekor {harimau.nama}')
print(f'{lumbalumba.nama} tinggal di {lumbalumba.habitat}')
print(f'{harimau.nama} adalah hewan {harimau.jenis}')




