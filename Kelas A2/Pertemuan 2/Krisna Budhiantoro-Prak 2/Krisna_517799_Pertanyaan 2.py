class PySolution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

x = input("Masukkan Nama: ")
print(PySolution().reverse_words(x))
