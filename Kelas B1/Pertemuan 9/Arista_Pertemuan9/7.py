from collections import namedtuple

Event = namedtuple("Event", ["judul", "waktu", "lokasi", "deskripsi", "kapasitas", "tiket_terjual"])

class JadwalAcara:
    def __init__(self):
        self.acara = []

    def tambah_acara(self, judul, waktu, lokasi, deskripsi="", kapasitas=100):
        self.acara.append(Event(judul, waktu, lokasi, deskripsi, kapasitas, 0))

    def pesan_tiket(self, idx_acara, jumlah_tiket):
        if 0 <= idx_acara < len(self.acara):
            event = self.acara[idx_acara]
            sisa_kapasitas = event.kapasitas - event.tiket_terjual
            if jumlah_tiket <= sisa_kapasitas:
                self.acara[idx_acara] = event._replace(tiket_terjual=event.tiket_terjual + jumlah_tiket)
                print(f"Berhasil memesan {jumlah_tiket} tiket untuk acara '{event.judul}'.")
            else:
                print("Maaf, tiket tidak tersedia.")
        else:
            print("Indeks acara tidak valid.")

    def tampilkan_jadwal(self):
        for i, event in enumerate(self.acara, start=1):
            print(f"Acara {i}:")
            print(f"  Judul: {event.judul}")
            print(f"  Waktu: {event.waktu}")
            print(f"  Lokasi: {event.lokasi}")
            print(f"  Deskripsi: {event.deskripsi}")
            print(f"  Kapasitas: {event.kapasitas}")
            print(f"  Tiket Terjual: {event.tiket_terjual}")
            print()


jadwal = JadwalAcara()

jadwal.tambah_acara("Pameran Fotografi", "Sabtu, 15 Mei 2024 - 10.00-18.00 WIB", "Gedung Pameran Seni", "Pameran fotografi karya-karya terbaik dari fotografer lokal.", kapasitas=200)

jadwal.tampilkan_jadwal()

jadwal.pesan_tiket(0, 50)

jadwal.tampilkan_jadwal()
