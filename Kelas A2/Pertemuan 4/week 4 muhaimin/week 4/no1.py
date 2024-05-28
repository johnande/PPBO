class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id

# Contoh penggunaan kelas Orang
orang1 = Orang("John", "Doe", "123456")
print("Nama Lengkap:", orang1.nama_depan, orang1.nama_belakang)
print("Nomor ID:", orang1.nomor_id)

class Mahasiswa(Orang):
    # Konstanta untuk jenjang
    SARJANA = "SARJANA"
    MASTER = "MASTER"
    DOKTOR = "DOKTOR"

    def __init__(self, nama_depan, nama_belakang, nomor_id, jenjang):
        # Memanggil konstruktor kelas Orang
        super().__init__(nama_depan, nama_belakang, nomor_id)
        
        # Atribut jenjang
        if jenjang not in [self.SARJANA, self.MASTER, self.DOKTOR]:
            raise ValueError("Jenjang tidak valid")
        self.jenjang = jenjang
        
        # List kosong untuk mata kuliah
        self.matkul = []

    def enrol(self, mata_kuliah):
        # Menambahkan mata kuliah ke dalam list matkul
        self.matkul.append(mata_kuliah)
        print(f"{self.nama_depan} {self.nama_belakang} berhasil mendaftar mata kuliah: {mata_kuliah}")

# Contoh penggunaan kelas Mahasiswa
mahasiswa1 = Mahasiswa("Alice", "Smith", "789012", Mahasiswa.SARJANA)
print("Nama Lengkap:", mahasiswa1.nama_depan, mahasiswa1.nama_belakang)
print("Nomor ID:", mahasiswa1.nomor_id)
print("Jenjang:", mahasiswa1.jenjang)

# Menambahkan mata kuliah
mahasiswa1.enrol("Matematika Dasar")
mahasiswa1.enrol("Fisika Dasar")

# Menampilkan mata kuliah yang diambil
print("Mata Kuliah yang Diambil:", mahasiswa1.matkul)

class Karyawan(Orang):
    # Konstanta untuk status karyawan
    TETAP = "TETAP"
    TDK_TETAP = "TDK_TETAP"

    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan):
        # Memanggil konstruktor kelas Orang
        super().__init__(nama_depan, nama_belakang, nomor_id)
        
        # Atribut status karyawan
        if status_karyawan not in [self.TETAP, self.TDK_TETAP]:
            raise ValueError("Status karyawan tidak valid")
        self.status_karyawan = status_karyawan

# Contoh penggunaan kelas Karyawan
karyawan1 = Karyawan("Bob", "Johnson", "345678", Karyawan.TETAP)
print("Nama Lengkap:", karyawan1.nama_depan, karyawan1.nama_belakang)
print("Nomor ID:", karyawan1.nomor_id)
print("Status Karyawan:", karyawan1.status_karyawan)

class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan):
        # Memanggil konstruktor kelas Karyawan
        super().__init__(nama_depan, nama_belakang, nomor_id, status_karyawan)
        
        # List kosong untuk mata kuliah yang diajar
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        # Menambahkan mata kuliah yang diajar ke dalam list matkul_diajar
        self.matkul_diajar.append(mata_kuliah)
        print(f"Dosen {self.nama_depan} {self.nama_belakang} sedang mengajar mata kuliah: {mata_kuliah}")

# Contoh penggunaan kelas Dosen
dosen1 = Dosen("Dr. Sarah", "Williams", "567890", Dosen.TETAP)
print("Nama Lengkap:", dosen1.nama_depan, dosen1.nama_belakang)
print("Nomor ID:", dosen1.nomor_id)
print("Status Karyawan:", dosen1.status_karyawan)

# Menambahkan mata kuliah yang diajar
dosen1.mengajar("Pemrograman Python")
dosen1.mengajar("Basis Data")

# Menampilkan mata kuliah yang diajar
print("Mata Kuliah yang Diajar:", dosen1.matkul_diajar)

bowo = Mahasiswa("Bowo", "Nugroho", "987654", Mahasiswa.SARJANA)

# Memanggil metode enrol untuk menambahkan mata kuliah "Basis Data"
bowo.enrol("Basis Data")
print(bowo.nama_depan,bowo.nama_belakang,bowo.nomor_id,bowo.jenjang,bowo.matkul)