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