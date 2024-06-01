# contoh objek dan kelas pada python

#pembuatan kelas
class dosen:

    def __init__(self, name, subject) -> None:
        self.name = name
        self.subject = subject

    def show (self):
        print(f'Nama:\t {self.name} \nMengajar:\t {self.subject}')

#pembuatan objek
        
dosen1 = dosen('Budi', 'teknik telekomunikasi')

dosen1.show()