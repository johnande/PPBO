class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

X=input("Masukkan kalimat yang ingin dibalik urutan katanya:")
print(py_solution().reverse_words(x))
