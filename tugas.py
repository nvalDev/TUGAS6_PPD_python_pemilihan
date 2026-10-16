
#validator sistem login nya bisa di bilang gate/middleware sih
username = input("Masukkan Username: ")
password = input("Masukkan Password: ")

if username != "naufal" or password != "4101":
    print("\n!! Username dan Password salah !!")
    print("!! Login Gagal !!")
    exit()
print(f"\nLogin berhasil. Welcome, {username}!\n")

#menu menu dari bimble nya
print("===== BIMBEL KAK DIANA =====")
print("1. Akademik")
print("2. Non-Akademik")
print("0. EXIT\n")

kategori = int(input("Pilih kategori: "))

if kategori == 0:
    exit()
#validari tanpa pakek list, pakek (and) :v
elif kategori != 1 and kategori != 2: 
    print("\nKategori tidak tersedia!")
    exit()

# buat nampung variable kosong dulu
nama_paket = ""
harga_satuan = 0
potongan_satuan = 0
bonus_paket = ""

#menu menu dari kategori 1 dan 2
if kategori == 1:
    print("1. Matematika (SD/SMP)")
    print("2. Fisika & Kimia (SMA)")
    print("3. Bahasa Inggris Intensif")
    
    paket = int(input("\nMasukkan paket belajar: "))
    
    if paket == 1:
        nama_paket = "Matematika (SD/SMP)"
        harga_satuan = 500000
        potongan_satuan = 50000
        bonus_paket = "1 buku rumus cepat"
    elif paket == 2:
        nama_paket = "Fisika & Kimia (SMA)"
        harga_satuan = 800000
        potongan_satuan = 100000
        bonus_paket = "1 buku rumus cepat dan 1 set tabel periodik"
    elif paket == 3:
        nama_paket = "Bahasa Inggris Intensif"
        harga_satuan = 650000
        potongan_satuan = 75000
        bonus_paket = "1 buku rumus cepat, 1 set tabel periodik, dan kamus saku"
    else:
        print("\n[!] Paket tersebut tidak ada dalam daftar")
        exit()

#paket belajar 2
elif kategori == 2:
    print("1. Pemrograman Python Dasar")
    print("2. Desain Grafis (Figma/Canva)")
    print("3. Public Speaking & Content")
    paket = int(input("\nMasukkan paket belajar: "))
    
    if paket == 1:
        nama_paket = "Pemrograman Python Dasar"
        harga_satuan = 900000
        potongan_satuan = 120000
        bonus_paket = "1 e-book modul syntax dasar"
    elif paket == 2:
        nama_paket = "Desain Grafis (Figma/Canva)"
        harga_satuan = 750000
        potongan_satuan = 90000
        bonus_paket = "1 e-book modul syntax dasar dan template asset UI"
    elif paket == 3:
        nama_paket = "Public Speaking & Content"
        harga_satuan = 700000
        potongan_satuan = 80000
        bonus_paket = "2 e-book modul syntax dasar, template asset, dan video panduan"
    else:
        print("\n[!] Paket tersebut tidak ada dalam daftar")
        exit()

#input jumlah gelombah nye
jumlah = int(input("\nMasukkan jumlah paket: "))
if jumlah <= 0:
    print("\n[!] Pembelian paket les tidak boleh nol atau minus")
    exit()

gelombang = input("\nMasukkan gelombang pendaftaran (Gelombang1/Gelombang2/None): ")

# penjumlahan harga
total_awal = harga_satuan * jumlah

#kalkulasi varisasi diskon" nya
diskon_persen = 0
if gelombang == "Gelombang1":
    diskon_persen = 0.15
elif gelombang == "Gelombang2":
    diskon_persen = 0.10

#penjumlahan diskkon nya
nilai_diskon = total_awal * diskon_persen
total_sementara = total_awal - nilai_diskon

total_potongan_bundle = 0
if jumlah > 3:
    total_potongan_bundle = potongan_satuan * jumlah 

#finnal diskon yang di dapetin
total_akhir = float(total_sementara - total_potongan_bundle)

# final output nya dari inputan dan proses dari code di atas nya
print("\n===== Data Pendaftaran =====")
print(f"Nama       : {username}")
print(f"Paket      : {nama_paket}")
print(f"Jumlah     : {jumlah} paket")
print(f"Total Biaya: Rp {total_akhir}")
print(f"Mendapatkan bonus {bonus_paket}")