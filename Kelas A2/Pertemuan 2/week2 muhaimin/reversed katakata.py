class py_solution:
    def reverse_word(self,x):
        return ' '.join(reversed(x.split()))

x=input()
print(py_solution().reverse_word(x))