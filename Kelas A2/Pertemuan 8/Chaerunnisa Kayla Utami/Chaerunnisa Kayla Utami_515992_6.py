class Rekening:
  def __init__(self, nama, no_rekening, saldo):
    self.nama = nama
    self.no_rekening = no_rekening
    self.saldo = saldo

  def Setor_tunai(self, nominal):
    self.saldo += nominal
    print(f"Setoran tunai Rp.{nominal:,.2f} berhasil dilakukan.")

  def Tarik_tunai(self, nominal):
    if nominal > self.saldo:
      print(f"Penarikan tunai gagal. Saldo Anda tidak mencukupi.")
    else:
      self.saldo -= nominal
      print(f"Penarikan tunai Rp.{nominal:,.2f} berhasil dilakukan.")

  def Transfer(self, penerima, nominal):
    if nominal > self.saldo:
      print(f"Transfer gagal. Saldo Anda tidak mencukupi.")
    else:
      self.saldo -= nominal
      penerima.saldo += nominal
      print(f"Transfer sebesar Rp.{nominal:,.2f} dari rekening {self.no_rekening} ke rekening {penerima.no_rekening} berhasil.")

class Nasabah(Rekening):
  def __init__(self, nama, no_rekening, saldo):
    super().__init__(nama, no_rekening, saldo)

  def tampilkan_data_nasabah(self):
    print(f"Nama Nasabah: {self.nama}")
    print(f"No. Rekening: {self.no_rekening}")
    print(f"Saldo: Rp.{self.saldo:,.2f}")

# Membuat dua objek dari class Nasabah
nasabah1 = Nasabah("Budi", 5555, 500000.0)
nasabah2 = Nasabah("Wati", 6666, 2000000.0)

# Simulasi Transaksi ATM
print("\nSimulasi Transaksi ATM:")

# Transaksi Nasabah 1
print("\nNasabah 1:")
nasabah1.tampilkan_data_nasabah()
nasabah1.Setor_tunai(1000000.0)
nasabah1.tampilkan_data_nasabah()

# Transaksi Nasabah 2
print("\nNasabah 2:")
nasabah2.tampilkan_data_nasabah()
nasabah2.Tarik_tunai(1000000.0)
nasabah2.tampilkan_data_nasabah()

# Transaksi Transfer
print("\nTransaksi Transfer:")
nasabah1.Transfer(nasabah2, 500000.0)

# Tampilkan data nasabah setelah transfer
print("\nData Nasabah Setelah Transfer:")
print("\nNasabah 1:")
nasabah1.tampilkan_data_nasabah()
print("\nNasabah 2:")
nasabah2.tampilkan_data_nasabah()
