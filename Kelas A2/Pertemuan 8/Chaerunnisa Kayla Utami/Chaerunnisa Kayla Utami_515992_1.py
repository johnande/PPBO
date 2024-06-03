def mil_ke_kilometer(mil):
    kilometer = mil * 1.60934
    return kilometer

def main():
    mil = float(input("Masukkan jumlah mil: "))
    kilometer = mil_ke_kilometer(mil)
    print(f"{mil} mil = {kilometer} kilometer")

if __name__ == "__main__":
    main()