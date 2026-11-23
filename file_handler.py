class FileHandler:
    def __init__(self, nama_file):
        self.__nama_file = nama_file

def baca_data(self):
        data_buku = {}  
        try:
            with open(self.__nama_file, 'r') as file:
                for baris in file:
                    potongan = baris.strip().split(',')
                    data_buku[potongan[0]] = potongan
                    
        except FileNotFoundError:
            pass 
                
        return data_buku

def simpan_data(self, data):
        with open(self.__nama_file, 'w') as file:
            for kode, info in data.items():
                teks_baris = ",".join(info) + "\n"                
                file.write(teks_baris)
