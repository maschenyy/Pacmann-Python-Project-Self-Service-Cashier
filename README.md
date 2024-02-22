# Final Projek Python Pacmann
Berikut merupakan hasil dan penjelasan dari projek python yang disediakan oleh pacmann yang berada pada folder atau repository final project python. Projek yang diberikan yaitu program kasir dimana self-service pada suatu supermarket.

# A. Backgroud Problem 
Terdapat kasus (case) dimana pemilik supermarket bernama Andi memiliki rencana untuk melakukan perbaikan bisnis dengan cara membuat sistem kasir self-service. Sistem tersebut memungkinkan pembeli untuk memasukkan barang yang dibeli, jumlah item, harga item, serta fitur lainnya. Permasalahan yang dihadapi yaitu Andi membutuhkan seorang programmer untuk membuat sistem kasir tersebut

# B. Tujuan Pengerjaan Project
1. Membuat program kasir sederhana menggunakan python
2. Mengaplikasikan pembuatan program yang berbasis fungsi (function) atau objek (OOP)
3. Mengaplikasikan penulisan kode yang bersih (clean code), mengacu pada PEP 8

# C. Requirements atau Objectives
## Requirements
Requirement yang diperlukan pada program yang dibuat antara lain:
    *add_item sebagai menu untuk menambahkan barang
    *update_item_name sebagai method pada menu untuk mengubah nama item
    *update_item_price sebagai method pada menu untuk mengubah harga item
    *update_item_qty sebagai method pada menu untuk mengubah jumlah item
    *delete_item untuk sebagai method pada menu untuk menghapus sebuah item, termasuk harga dan kuantitas
    *reset_transaction sebagai method pada menu untuk menghapus keseluruhan transaksi
    *check_order untuk sebagai method pada menu untuk memastikan ulang nama, harga serta jumlah item
    *total_price sebagai method untuk menghitung harga akhir dari belanja dan terdapat diskon dengan syarat tertentu

## Objectives
Objektif pada project kali ini yaitu membuat program sistem kasir yang dapat melakukan fitur create, read, update, dan delete. Program tersebut diharapkan dapat berjalan dengan baik sehingga pembeli dapat melakukan transaksi dengan nyaman. Penjelasan lebih lanjut mengenai fitur-fitur tersebut yaitu:
Create:
    *Pengguna dapat membuat id transaksi ketika berbelanja
    *Pengguna dapat menambahkan detail barang belanja berupa nama barang, harga per barang, jumlah barang. Kemudian sistem secara otomatis dapat melakukan perhitungan total harga yang didapat dari harga per barang dikali dengan jumlah barang
Read:
    *Pengguna dapat melihat barang apa yang telah dimasukkan atau ditambahkan
    *Pengguna dapat melihat harga akhir transaksi 
Update:
    *Pengguna dapat mengubah nama barang jika pengguna salah memasukkan nama barang 
    *Pengguna dapat mengubah kuantitas atau jumlah barang yang dimasukkan jika pengguna salah memasukkan jumlah barang
    *Pengguna dapat mengubah harga barang jika pengguna salah memasukkan harga barang
Delete:
    *Pengguna dapat menghapus salah satu item dengan menggunakan nama barang kemudian secara otomatis, harga dan kuantitas dari barang tersebut juga terhapus
    *Pengguna dapat menghapus semua transaksi atau reset transaksi yang sedang dilakukan   

# D. Flowchart
![flowchart_project](https://github.com/maschenyy/Pacmann-Python-Project-Self-Service-Cashier/assets/77559787/27158041-64d9-4bdd-a368-99bbe79ab758) 

# E. Test Case
1. Test case tambah item

2. Test case update nama item
    
    
3. Test case update jumlah item


4. Test case update jumlah harga per item


5. Test case hapus data


6. Test case reset belanjaan
    

7. Test case check belanjaan


8. Test case payment

# F. Deskripsi File
1. Modul 'modul.py' berisi fungsi-fungsi program kasir yang telah dibuat.
2. Modul 'main.py' yaitu program untuk menjalankan aplikasi kasir.

# G. Cara Menggunakan Program
1. Download semua file/module Python ke dalam satu direktori lokal.
2. Definisikan variabel-variabel di modul 'modul.py' dan simpan.
3. Buka terminal atau code editor dan sesuaikan lokasi direktori lokal.
4. Jalankan modul python 'main.py'

