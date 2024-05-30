def konversi_mil_ke_kilometer(mil):
    try:
        kilometer = mil * 1.60934
        return kilometer
    except TypeError:
        print("Error: Masukkan harus berupa angka")

try:
    mil = float(input("Masukkan angka dalam satuan mil untuk dikonversi ke kilometer, sesuai keinginan Anda: "))
    kilometer = konversi_mil_ke_kilometer(mil)
    output = f"{mil} mil = {kilometer} kilometer"
    print(output)
    print()
    print(f"Jadi, sesuai input Anda menyatakan bahwa {output}")
except ValueError:
    print("Error: Masukkan harus berupa angka")
