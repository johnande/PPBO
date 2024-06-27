angka = 2
while angka <= 2:
    angka = int(input("Input sebuah bilangan: "))

    if angka >=2:
        for i in range (2, angka):
            if (angka % i) == 0:
                print(angka, "bukan bilangan prima")
                break
        else:
            print(angka, "adalah bilangan prima")
            break