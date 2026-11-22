from buku import Buku
from file_handler import FileHandler

class Perpustakaan:
    def __init__(self, nama_file):
        self.__file_handler = FileHandler(nama_file)
        self.__daftar_buku = self.__file_handler.baca_data()

    def cari_buku(self, kode_buku):
        if kode_buku in self.__daftar_buku:
            return self.__daftar_buku[kode_buku]
        return None

    def tambah_buku(self, kode_buku, judul_buku, penulis, tahun_terbit):
        if kode_buku in self.__daftar_buku:
            print("Kode buku sudah digunakan!")
            return False

        buku = Buku(kode_buku, judul_buku, penulis, tahun_terbit)
        self.__daftar_buku[kode_buku] = buku.format_simpan()
        self.__file_handler.simpan_data(self.__daftar_buku)

        print("Buku berhasil ditambahkan!")
        return True

    def update_buku(self, kode_buku, judul_buku, penulis, tahun_terbit):
        if kode_buku not in self.__daftar_buku:
            print("Buku tidak ditemukan!")
            return False

        buku = Buku(kode_buku, judul_buku, penulis, tahun_terbit)
        self.__daftar_buku[kode_buku] = buku.format_simpan()
        self.__file_handler.simpan_data(self.__daftar_buku)

        print("Data buku berhasil diperbarui!")
        return True
    
    def hapus_buku(self, kode_buku):
        if kode_buku not in self.__daftar_buku:
            print("Buku tidak ditemukan!")
            return False

        print("\nData buku yang akan dihapus:")
        print("Kode Buku :", kode_buku)
        print("Judul Buku :", self.__daftar_buku[kode_buku][1])

        konfirmasi = input("Yakin ingin menghapus buku? (y/n): ")

        if konfirmasi.lower() == "y":
            del self.__daftar_buku[kode_buku]
            self.__file_handler.simpan_data(self.__daftar_buku)

            print("Buku berhasil dihapus!")
            return True

        print("Penghapusan dibatalkan.")
        return False

    def tampilkan_semua(self):
        if not self.__daftar_buku:
            print("Belum ada data buku!")
            return

        print("\n===== DAFTAR SELURUH BUKU =====")

        for nomor, (kode, info) in enumerate(self.__daftar_buku.items(), start=1):
            print(f"\nBuku ke-{nomor}")
            print("Kode Buku   :", kode)
            print("Judul Buku  :", info[1])
            print("Penulis     :", info[2])
            print("Tahun Terbit:", info[3])

        print("\n===== AKHIR DAFTAR BUKU =====")

