# Fungsi untuk mengkonversi mil ke kilometer
def konversi_mil_ke_km(mil):
    km = mil * 1.60934
    return km

# Meminta input dari pengguna
mil = float(input("Masukkan jumlah mil: "))

# Mengkonversi mil ke kilometer
km = konversi_mil_ke_km(mil)

# Menampilkan hasil konversi
print(f"{mil} mil = {km} kilometer")
