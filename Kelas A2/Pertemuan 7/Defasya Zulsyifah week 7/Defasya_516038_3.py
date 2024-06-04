class UpperCaseDecorator:
    def _init__ (self, func):
        self.func = func

    def _call__ (self, *args, ** kwargs):
        result = self.func(*args, ** kwargs)
        return result.upper()

@UpperCaseDecorator
def fungsi_ucapan(nama):
    return f"Selamat pagi, {nama}!"

nama = "Defasya"
ucapan = fungsi_ucapan(nama)

print(f"Ucapan untuk {nama}: {ucapan}")