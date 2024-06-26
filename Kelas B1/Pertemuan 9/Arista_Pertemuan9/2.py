class HotelRoom:
    def __init__(self, nomor_kamar, tipe_kamar, tersedia=True):
        self._nomor_kamar = nomor_kamar
        self._tipe_kamar = tipe_kamar
        self._tersedia = tersedia
    
    @property
    def nomor_kamar(self):
        return self._nomor_kamar
    @property
    def tipe_kamar(self):
        return self._tipe_kamar
    
    @property
    def tersedia(self):
        return self._tersedia
    
    @classmethod
    def dari_detail_kamar(cls, detail_kamar):
        nomor_kamar, tipe_kamar, tersedia = detail_kamar.split(',')
        return cls(nomor_kamar.strip(), tipe_kamar.strip(), tersedia.strip().lower() == 'ya')
    
    @staticmethod
    def info_kamar(kamar):
        tersedia_str = "Ya" if kamar.tersedia else "Tidak"
        return f"Nomor Kamar: {kamar.nomor_kamar}, Tipe: {kamar.tipe_kamar}, Tersedia: {tersedia_str}"

detail_kamar1 = "101, Standard, Ya"
kamar1 = HotelRoom.dari_detail_kamar(detail_kamar1)
print(HotelRoom.info_kamar(kamar1))

detail_kamar2 = "102, Suite, Tidak"
kamar2 = HotelRoom.dari_detail_kamar(detail_kamar2)
print(HotelRoom.info_kamar(kamar2))
