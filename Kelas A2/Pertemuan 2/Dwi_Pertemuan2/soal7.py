class py_solution:
    def reserve_words(self, s):
        return ' '.join(reversed(s.split()))
    
x = input()
print(py_solution().reserve_words(x))