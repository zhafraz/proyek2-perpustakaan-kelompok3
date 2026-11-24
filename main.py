from modules.perpustakaan import Perpustakaan

def menu_tambah(perpus):
    print("\n--- [1] Tambah Data Buku ---")
    kode = input("Masukkan Kode Buku   : ").strip()
    if kode == "":
        print("Kode buku tidak boleh kosong!")
        return

    buku = perpus.cari_buku(kode)
    if buku is not None:
        print(f"Gagal: Buku dengan kode '{kode}' sudah terdaftar!")
        return

    judul = input("Masukkan Judul Buku  : ").strip()
    penulis = input("Masukkan Nama Penulis: ").strip()
    penerbit = input("Masukkan Penerbit    : ").strip()

    try:
        tahun = int(input("Masukkan Tahun Terbit: "))
    except ValueError:
        print("Input tahun harus berupa angka!")
        return

    perpus.tambah_buku(kode, judul, penulis, penerbit, tahun)

def menu_cari(perpus):
    print("\n--- [2] Cari Data Buku ---")
    kode = input("Masukkan Kode Buku yang dicari: ").strip()
    buku = perpus.cari_buku(kode)

    if buku is not None:
        print("\n[Data Buku Ditemukan]")
        print("Kode Buku   :", buku[0])
        print("Judul Buku  :", buku[1])
        print("Penulis     :", buku[2])
        print("Penerbit    :", buku[3])
        print("Tahun Terbit:", buku[4])
    else:
        print(f"Buku dengan kode '{kode}' tidak ditemukan.")

def menu_update(perpus):
    print("\n--- [3] Perbarui Data Buku ---")
    kode = input("Masukkan Kode Buku yang ingin diubah: ").strip()
    buku = perpus.cari_buku(kode)

    if buku is None:
        print(f"Buku dengan kode '{kode}' tidak ditemukan!")
        return

    print("\nData Buku Saat Ini:")
    print("Judul Buku   :", buku[1])
    print("Penulis      :", buku[2])
    print("Penerbit     :", buku[3])
    print("Tahun Terbit :", buku[4])

    print("\nMasukkan Data Baru:")
    judul_baru = input("Judul Baru       : ").strip()
    penulis_baru = input("Penulis Baru     : ").strip()
    penerbit_baru = input("Penerbit Baru    : ").strip()
    
    try:
        tahun_baru = int(input("Tahun Terbit Baru: "))
    except ValueError:
        print("Input tahun harus berupa angka!")
        return

    perpus.update_buku(kode, judul_baru, penulis_baru, penerbit_baru, tahun_baru)

def menu_hapus(perpus):
    print("\n--- [4] Hapus Data Buku ---")
    kode = input("Masukkan Kode Buku yang akan dihapus: ").strip()
    buku = perpus.cari_buku(kode)

    if buku is None:
        print(f"Buku dengan kode '{kode}' tidak ditemukan!")
        return

    print(f"\nBuku yang akan dihapus: {buku[1]} (Kode: {kode})")
    
    konfirmasi = input("Apakah Anda yakin ingin menghapus buku ini? (y/n): ").strip().lower()
    if konfirmasi == "y":
        if perpus.hapus_buku(kode):
            print("Berhasil: Buku telah dihapus dari sistem dan file!")
        else:
            print("Gagal menghapus data buku.")
    else:
        print("Penghapusan buku dibatalkan.")

def menu_tampilkan(perpus):
    perpus.tampilkan_semua()

def tampilkan_pilihan():
    print("\n" + "=" * 35)
    print("   SISTEM INFORMASI PERPUSTAKAAN   ")
    print("=" * 35)
    print("1. Tambah Data Buku")
    print("2. Cari Data Buku")
    print("3. Perbarui Data Buku")
    print("4. Hapus Data Buku")
    print("5. Tampilkan Semua Buku")
    print("0. Keluar")
    print("=" * 35)

def main():
    perpus = Perpustakaan("data/data_buku.txt")
    while True:
        tampilkan_pilihan()
        pilihan = input("Pilih menu (0-5): ").strip()

        if pilihan == "1":
            menu_tambah(perpus)
        elif pilihan == "2":
            menu_cari(perpus)
        elif pilihan == "3":
            menu_update(perpus)
        elif pilihan == "4":
            menu_hapus(perpus)
        elif pilihan == "5":
            menu_tampilkan(perpus)
        elif pilihan == "0":
            print("\nTerima kasih.")
            break
        else:
            print("\nPilihan tidak valid, silakan coba lagi!")

if __name__ == "__main__":
    main()