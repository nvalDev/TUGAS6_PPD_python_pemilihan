# Sistem Pendaftaran Bimbingan Belajar Kak Diana

Sebuah program CLI (Command Line Interface) berbasis Python untuk simulasi sistem pendaftaran dan kasir bimbingan belajar. Program ini merupakan tugas implementasi materi "Pemilihan" (Conditional Statement / If-Else) yang disusun murni tanpa menggunakan struktur data tingkat lanjut seperti Array atau Dictionary[cite: 1].

## Deskripsi Proyek

Program ini dirancang untuk mengelola alur pendaftaran paket belajar dengan ketentuan harga, pemberian bonus, dan diskon yang bersifat dinamis[cite: 1]. Kalkulasi biaya akhir ditentukan berdasarkan periode gelombang pendaftaran serta kuantitas paket yang diambil oleh pengguna[cite: 1]. Sistem ini sepenuhnya menggunakan logika percabangan bersarang (Nested-If) untuk memastikan validasi data berjalan sesuai dengan spesifikasi.

## Fitur Utama

1. **Sistem Login:** Autentikasi keamanan awal yang mengharuskan pengguna memasukkan Username dan Password dengan benar sebelum mengakses menu utama[cite: 1].
2. **Menu Navigasi Dinamis:** Pemilihan kategori utama dan sub-menu paket belajar melalui proses validasi bertingkat guna mencegah kesalahan input dari pengguna[cite: 1].
3. **Kalkulasi Diskon Gelombang:**
   - Gelombang 1: Memberikan diskon sebesar 15% dari total harga dasar[cite: 1].
   - Gelombang 2: Memberikan diskon sebesar 10% dari total harga dasar[cite: 1].
   - None: Tidak ada pemotongan diskon gelombang[cite: 1].
4. **Promo Paket Bundle:** Pemberian potongan harga tambahan per paket secara spesifik apabila pendaftar mengambil lebih dari 3 paket pembelajaran sekaligus[cite: 1].

## Penjelasan Logika dan Struktur Kode

Kode program secara fundamental dibagi menjadi enam bagian utama:

### 1. Validasi Pengguna (Login)
Berfungsi sebagai gerbang keamanan awal program. Sistem menggunakan fungsi `input()` dan logika percabangan `if` dengan operator logika `or`. Apabila input kredensial tidak sesuai dengan basis data, program akan langsung memanggil fungsi `exit()` untuk menghentikan eksekusi secara otomatis[cite: 1].

### 2. Main Menu dan Validasi Kategori
Menampilkan antarmuka untuk memilih kategori program akademik atau non-akademik. Input diproses menggunakan tipe data integer (`int()`). Terdapat penanganan kesalahan (error handling) yang akan menghentikan program jika pengguna memasukkan opsi kategori yang tidak tersedia[cite: 1].

### 3. Sub-Menu dan Penetapan Variabel (Nested-If)
Merupakan inti dari penetapan data. Mengingat program tidak menggunakan Array, rincian harga, potongan khusus, dan bonus ditetapkan secara manual menggunakan logika `IF-ELIF-ELSE` yang bersarang. Pemilihan paket pada kategori tertentu akan mendeklarasikan nilai pada variabel `nama_paket`, `harga_satuan`, `potongan_satuan`, dan `bonus_paket` secara dinamis.

### 4. Input Kuantitas dan Gelombang
Sistem meminta pengguna memasukkan jumlah paket dan melakukan validasi mutlak bahwa angka yang dimasukkan tidak boleh nol atau negatif[cite: 1]. Setelah tervalidasi, sistem akan meminta input periode gelombang pendaftaran (Gelombang1/Gelombang2/None) sebagai parameter kalkulasi tahap akhir[cite: 1].

### 5. Kalkulasi Harga dan Diskon
Operasi matematika dijalankan dengan urutan prioritas berikut:
1. **Total Awal** = Harga Satuan dikalikan Jumlah Paket.
2. **Diskon Gelombang** = Persentase diskon (15% atau 10%) dikalikan Total Awal[cite: 1].
3. **Total Sementara** = Total Awal dikurangi Diskon Gelombang[cite: 1].
4. **Potongan Bundle** = Apabila kuantitas lebih dari 3, maka Potongan Satuan dikalikan Jumlah Paket[cite: 1].
5. **Total Akhir** = Total Sementara dikurangi Potongan Bundle[cite: 1].

### 6. Output Bukti Pendaftaran
Fase final untuk mencetak ringkasan transaksi pendaftaran ke layar Console[cite: 1]. Fase ini memanfaatkan fitur *f-string* (Formatted String Literal) pada Python untuk menyisipkan nilai akhir dari setiap variabel langsung ke dalam format teks, sehingga menghasilkan tata letak cetakan yang sejajar dan profesional sesuai spesifikasi[cite: 1].

## Cara Menjalankan Program

1. Pastikan lingkungan komputasi Anda telah terinstal Python versi 3.x.
2. Unduh (*download*) atau *clone* repositori ini ke dalam direktori lokal Anda.
3. Buka terminal atau *command prompt*, kemudian arahkan (*navigate*) ke direktori penyimpanan file.
4. Eksekusi perintah berikut:
   ```bash
   python main.py