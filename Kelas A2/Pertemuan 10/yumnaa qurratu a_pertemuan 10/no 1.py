class Sim_Cache:
    def __new__(cls):
        if not hasattr(cls, 'cache'):
            cls.cache = super().__new__(cls)
        return cls.cache

    def __init__(self):
        self.nama_web = "PBOTRI"
        self.create_cache()

    def create_cache(self):
        self.cache_source = self.nama_web + ".txt"
        self.cache_file_name = "cache_" + self.nama_web + ".txt"
        sf = open(self.cache_source, "r")  # buka file sumber
        cf = open(self.cache_file_name, "w")  # buat file cache baru
        cf.write(f"Ini adalah file cache dari web {self.nama_web}\n")
        line1 = False
        for l in sf:
            if "Start_cache" in l:  # menentukan baris awal cache
                line1 = True
            if line1:
                cf.write(l)  # menyalin cache dari sumber

    def get_cache(self):
        if not self.cache:
            self.cache = Sim_Cache()
        print(f"Nama file cache adalah {self.cache_file_name}")
        cf = open(self.cache_file_name, "r")
        print(cf.read())

# Instansiasi pertama
print("=====Instansiasi pertama:=====")
cache1 = Sim_Cache()
cache1.get_cache()

# Instansiasi kedua
print("\n=====Instansiasi kedua:=====")
cache2 = Sim_Cache()
add_cache = open("cache_PBOTRI.txt", "a")
add_cache.write("\n***Baris tambahan di file cache***")
add_cache.close()
cache2.get_cache()