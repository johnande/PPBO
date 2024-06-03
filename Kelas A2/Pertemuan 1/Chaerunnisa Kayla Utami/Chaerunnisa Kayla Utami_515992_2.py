def klasifikasi_suhu(suhu):
  """
  Fungsi untuk mengklasifikasikan nilai suhu dalam derajat Celcius

  Args:
    suhu: Nilai suhu dalam derajat Celcius (tipe float)

  Returns:
    String yang menunjukkan klasifikasi suhu
  """
  if suhu < 0:
    return "Membeku"
  elif suhu < 10:
    return "Sangat Dingin"
  elif suhu < 20:
    return "Sejuk"
  elif suhu < 30:
    return "Hangat"
  elif suhu < 40:
    return "Panas"
  else:
    return "Sangat Panas"

# Meminta input nilai suhu
suhu = float(input("Masukkan nilai suhu (Celcius): "))

# Klasifikasikan suhu dan cetak output
klasifikasi = klasifikasi_suhu(suhu)
print(f"Suhu {suhu} derajat Celcius diklasifikasikan sebagai {klasifikasi}")
