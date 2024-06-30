class Mahasiswa:
    def __init__(self, nama, jurusan, ipk):
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk
    def __str__(self):
        return f"Nama: {self.nama}, Jurusan: {self.jurusan}, IPK: {self.ipk:.2f}"

class DatabaseMahasiswa:
    __instance = None  # Atribut instance Singleton
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.mahasiswa = [] 
        return cls.__instance
    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswa.append(mahasiswa)
    def dapatkan_semua_mahasiswa(self):
        return self.mahasiswa

class ProfilMahasiswa:
    @staticmethod
    def buat_mahasiswa(nama, jurusan, ipk):
        return Mahasiswa(nama, jurusan, ipk)

# Eksekusi program
database = DatabaseMahasiswa()  # Instance Singleton

# Tambahkan mahasiswa dengan PabrikMahasiswa
mahasiswa1 = ProfilMahasiswa.buat_mahasiswa("Bintang", "Teknik Informatika", 3.9)
mahasiswa2 = ProfilMahasiswa.buat_mahasiswa("Berlian", "Teknologi Informasi", 3.7)
mahasiswa3 = ProfilMahasiswa.buat_mahasiswa("Pratama", "TRPL", 3.8)

# Tambahkan mahasiswa ke database
database.tambah_mahasiswa(mahasiswa1)
database.tambah_mahasiswa(mahasiswa2)
database.tambah_mahasiswa(mahasiswa3)

# Dapatkan semua mahasiswa
semua_mahasiswa = database.dapatkan_semua_mahasiswa()
print("Semua Mahasiswa:")
for mahasiswa in semua_mahasiswa:
    print(mahasiswa)