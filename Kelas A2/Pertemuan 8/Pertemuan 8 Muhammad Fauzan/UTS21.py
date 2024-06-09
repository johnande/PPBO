def mil_ke_kilometer(mil):
    kilometer = mil * 1.60934
    return kilometer


mil = float(input("Masukkan angka dengan satuan mil: "))
kilometer = mil_ke_kilometer(mil)
print(f"{mil} mil = {kilometer} kilometer")
