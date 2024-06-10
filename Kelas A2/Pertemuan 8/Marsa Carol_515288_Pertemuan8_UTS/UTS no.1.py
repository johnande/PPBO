def ubah_mil_ke_kilometer(mil):
    kilometer = 1.60934
    return mil * kilometer

def main():
    user_input = float(input("Masukkan jarak dalam mil: "))
    result = ubah_mil_ke_kilometer(user_input)
    print(f"{user_input} mil = {result} kilometer")

if __name__ == "__main__":
    main()
