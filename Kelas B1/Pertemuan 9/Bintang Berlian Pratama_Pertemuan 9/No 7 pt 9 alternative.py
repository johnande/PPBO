from collections import namedtuple

Dosen = namedtuple('Dosen', ['nama', 'nidn'])
Mahasiswa = namedtuple('Mahasiswa', ['nama', 'nim', 'jurusan', 'nilai'])
MataKuliah = namedtuple('MataKuliah', ['kode', 'nama', 'sks'])
Kelas = namedtuple('Kelas', ['dosen', 'mata_kuliah', 'mahasiswa'])

dosen_pengampu = Dosen('Yuris Mulya Saputra, S.T., M.Sc., Ph.D.', '123456')
mahasiswa1 = Mahasiswa('Bintang Berlian', '518496', 'TRI', [90, 85, 88, 92])
mahasiswa2 = Mahasiswa('Muhammad Luthfi', '518497', 'TRPL', [80, 75, 78, 82])
mata_kuliah = MataKuliah('SVRI2142', 'PBO', 2)
kelas_pemrograman = Kelas(dosen_pengampu, mata_kuliah, [mahasiswa1, mahasiswa2])

print("Informasi Kelas:")
print("Dosen Pengampu:", kelas_pemrograman.dosen.nama)
print("Mata Kuliah:", kelas_pemrograman.mata_kuliah.nama)
print("Jumlah SKS:", mata_kuliah.sks)
print("Daftar Mahasiswa:")
for mahasiswa in kelas_pemrograman.mahasiswa:
    print("\nNama:", mahasiswa.nama)
    print("NIM:", mahasiswa.nim)
    print("Jurusan:", mahasiswa.jurusan)
    print("Nilai:", mahasiswa.nilai)
