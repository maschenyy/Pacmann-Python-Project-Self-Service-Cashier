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

    - a. add_item sebagai method pada menu untuk menambahkan barang. Input pada method ini yaitu nama barang pada variabel 'nama_item', jumlah barang pada variabel 'jumlah_item', dan harga barang pada variabel 'harga_item'
    - b. update_item_name sebagai method pada menu untuk mengubah nama item. Input pada method ini yaitu nama barang pada variabel 'nama_item' dan nama barang yang baru pada variabel 'update_nama_item'
    - c. update_item_price sebagai method pada menu untuk mengubah harga item. Input pada method ini yaitu nama barang pada variabel 'nama_item' dan harga barang yang baru pada variabel 'update_harga_item'
    - d. update_item_qty sebagai method pada menu untuk mengubah jumlah item. Input pada method ini yaitu nama barang pada variabel 'nama_item' dan jumlah atau kuantitas barang yang baru pada variabel 'update_jumlah_barang'
    - e. delete_item untuk sebagai method pada menu untuk menghapus sebuah item, termasuk harga dan kuantitas. Input pada method ini yaitu nama barang pada variabel 'nama_barang'. Jika nama barang tidak ditemukan maka akan kembali ke menu utama (main menu)
    - f. reset_transaction sebagai method pada menu untuk menghapus keseluruhan transaksi
    - g. check_order untuk sebagai method pada menu untuk menampilkan dan memastikan ulang nama, harga serta jumlah item
    - h. total_price sebagai method untuk menghitung harga akhir dari belanja dan terdapat diskon dengan syarat tertentu
        * jika total belanja diatas Rp. 200.000 maka akan mendapatkan diskon sebesar 5%
        * jika total belanja diatas Rp. 300.000 maka akan mendapatkan diskon sebesar 8%
        * jika total belanja diatas Rp. 500.000 maka akan mendapatkan diskon sebesar 10%
        

## Objectives
Objektif pada project kali ini yaitu membuat program sistem kasir yang dapat melakukan fitur create, read, update, dan delete. Program tersebut diharapkan dapat berjalan dengan baik sehingga pembeli dapat melakukan transaksi dengan nyaman. Penjelasan lebih lanjut mengenai fitur-fitur tersebut yaitu:
1. Create:
    + Pengguna dapat membuat id transaksi ketika berbelanja
    + Pengguna dapat menambahkan detail barang belanja berupa nama barang, harga per barang, jumlah barang. Kemudian sistem secara otomatis dapat melakukan perhitungan total harga yang didapat dari harga per barang dikali dengan jumlah barang
2. Read:
    + Pengguna dapat melihat barang apa yang telah dimasukkan atau ditambahkan
    + Pengguna dapat melihat harga akhir transaksi
3. Update:
    + Pengguna dapat mengubah nama barang jika pengguna salah memasukkan nama barang
    + Pengguna dapat mengubah kuantitas atau jumlah barang yang dimasukkan jika pengguna salah memasukkan jumlah barang
    + Pengguna dapat mengubah harga barang jika pengguna salah memasukkan harga barang
4. Delete:
    + Pengguna dapat menghapus salah satu item dengan menggunakan nama barang kemudian secara otomatis, harga dan kuantitas dari barang tersebut juga terhapus
    + Pengguna dapat menghapus semua transaksi atau reset transaksi yang sedang dilakukan

# D. Flowchart
![flowchart_project](https://github.com/maschenyy/Pacmann-Python-Project-Self-Service-Cashier/assets/77559787/27158041-64d9-4bdd-a368-99bbe79ab758) 

Penjelasan dari flowchart tersebut yaitu
Pertama pengguna memasukkan id transaksi terlebih dahulu. Setelah itu, akan tampil halaman utama (main menu). Pada main menu, pengguna dapat memasukkan menu mana yang akan diakses. Jika sudah selesai pada menu tersebut, user dapat memilih antara untuk kembali ke menu utama atau tetap pada menu tersebut. Jika sudah selesai, pengguna dapat pilih menu nomor 9 untuk keluar dari program

# E. Test Case
1. Test case tambah item
* ![add item](https://github.com/maschenyy/Pacmann-Python-Project-Self-Service-Cashier/assets/77559787/45f51747-6707-4772-a356-19512086da9f)

2. Test case update nama item
* ![update item name](https://github.com/maschenyy/Pacmann-Python-Project-Self-Service-Cashier/assets/77559787/11ab1020-ae4d-44e0-a8ec-a425dc25ec27)
        
3. Test case update jumlah item
* ![update item quantity](https://github.com/maschenyy/Pacmann-Python-Project-Self-Service-Cashier/assets/77559787/f24ae153-13a4-40b9-bd6e-9e8cbc176294)

4. Test case update jumlah harga per item
* ![update item price](https://github.com/maschenyy/Pacmann-Python-Project-Self-Service-Cashier/assets/77559787/bc83d229-f609-46f3-b0b4-c89c694ec0ab)

5. Test case hapus data
* ![delete item](https://github.com/maschenyy/Pacmann-Python-Project-Self-Service-Cashier/assets/77559787/1019f996-ddc0-4cfb-94a5-126a6578436d)

6. Test case reset belanjaan
* ![reset transaction](https://github.com/maschenyy/Pacmann-Python-Project-Self-Service-Cashier/assets/77559787/7ac23167-e846-412c-8c1f-fcdbad997af4)    

7. Test case check belanjaan
* ![check order](https://github.com/maschenyy/Pacmann-Python-Project-Self-Service-Cashier/assets/77559787/91f80f33-19c2-46af-8354-e205168292dc)

8. Test case payment
* ![total payment](https://github.com/maschenyy/Pacmann-Python-Project-Self-Service-Cashier/assets/77559787/3f5e0dc1-c71c-4577-a35b-dd6fe8f37645)


# F. Deskripsi File
1. Modul 'modul.py' berisi fungsi-fungsi program kasir yang telah dibuat.
2. Modul 'main.py' yaitu program untuk menjalankan aplikasi kasir.

# G. Cara Menggunakan Program
1. Download semua file/module Python ke dalam satu direktori lokal.
2. Definisikan variabel-variabel di modul 'modul.py' dan simpan.
3. Buka terminal atau code editor dan sesuaikan lokasi direktori lokal.
4. Jalankan modul python 'main.py'

