def add_menumakanan(menu):
    def x(*args, **kwargs):
        return "Menu hari ini: " + menu(*args, **kwargs)
    return x

@add_menumakanan
def membuat_makanan(makanan):
    return makanan

nama_makanan = membuat_makanan("Ayam Bakar dan Tempe")
print(nama_makanan)