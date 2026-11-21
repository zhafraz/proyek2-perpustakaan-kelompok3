def tampilkan_menu():
    print("\n=== APLIKASI PERPUSTAKAAN ===")
    print("1. Tambah Data Buku")
    print("2. Cari Data Buku")
    print("3. Perbarui Data Buku")
    print("4. Hapus Data Buku")
    print("5. Tampilkan Semua Buku")
    print("0. Keluar")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (0-5): ").strip()

        if pilihan == "1":
            print("Menu Tambah Buku dipilih.")
        elif pilihan == "2":
            print("Menu Cari Buku dipilih.")
        elif pilihan == "3":
            print("Menu Perbarui Buku dipilih.")
        elif pilihan == "4":
            print("Menu Hapus Buku dipilih.")
        elif pilihan == "5":
            print("Menu Tampilkan Semua dipilih.")
        elif pilihan == "0":
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()