def prime_num (num:int) -> str:

    list_modulus = []

    if num == 1:
        return "bukan bilangan prima"

    for i in range (1, num + 1):
        list_modulus.append(num % i)

    jumlah_nol = list_modulus.count(0)

    if jumlah_nol > 2:
        return "bukan bilangan prima"
    
    else:
        return "bilangan prima"

number = int(input("masukkan angka: "))    
print(prime_num(number))