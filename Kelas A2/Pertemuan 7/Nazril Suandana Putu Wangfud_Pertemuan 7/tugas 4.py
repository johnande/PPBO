class PesanSelamatDatang:
    def __init__(self, fungsi_asli):
        self.fungsi_asli = fungsi_asli

    def __call__(self, *args, **kwargs):
        print("Selamat datang! Fungsi akan dijalankan.")
        return self.fungsi_asli(*args, **kwargs)
    
#DECORATOR
@PesanSelamatDatang
def fungsi_sapa(nama):
    print(f"Halo!", nama ,"Selamat datang di program ini.")

nama_pengguna = input("Masukkan nama Anda: ")
fungsi_sapa(nama_pengguna)