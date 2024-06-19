bilangan = int(input("Masukkan angka: "))

if bilangan <= 1:
    print(f"{bilangan} bukan bilangan prima.")
else:
    prima = True
    for i in range(2, int(bilangan ** 0.5) + 1):
        if bilangan % i == 0:
            prima = False
            break

    if prima:
        print(f"{bilangan} adalah bilangan prima.")
    else:
        print(f"{bilangan} bukan bilangan prima.")
