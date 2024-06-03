def mil_ke_kilometer(mil):
    # 1 mil = 1.60934 kilometer
    kilometer = mil * 1.60934
    return kilometer

mil = float(input("Masukkan jumlah mil: "))

kilometer = mil_ke_kilometer(mil)

print(f"{mil} mil = {kilometer} kilometer")

