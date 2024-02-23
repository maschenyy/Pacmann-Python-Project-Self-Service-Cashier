from tabulate import tabulate

# id_transaksi = str(input("Masukkan id transaksi: "))

class Transaction:

  all_item = {"Nama item:":[],
              "Harga per item:":[],
              "Jumlah item:":[],
              "Total harga item:":[]}

  def __init__(self, id_transaksi):
    """
    Parameter:
      id_transaksi (str) = id dari transaksi yang sedang berlangsung
    """
    self.id_transaksi = id_transaksi

  def add_item(self):
    """
    Parameter:
      id_transaksi (str) = id dari transaksi yang sedang berlangsung

    Input:
      nama_item (str) = variabel untuk menampung input nama dari barang yang ditambahkan
      jumlah item (int) = variabel untuk menampung input jumlah dari barang yang ditambahkan
      harga_item (int) = variabel untuk menampung input harga dari barang yang ditambahkan
    """
    try:
      #input data item
      nama_item = str(input("Masukkan nama barang: "))
      jumlah_item = int(input("Masukkan jumlah barang: "))
      harga_item = int(input("Masukkan harga barang: "))
      total_harga = jumlah_item * harga_item

      #Memasukkan data ke dalam dictionary
      self.all_item["Nama item:"].append(nama_item)
      self.all_item["Harga per item:"].append(harga_item)
      self.all_item["Jumlah item:"].append(jumlah_item)
      self.all_item["Total harga item:"].append(total_harga)
    except ValueError:
      print("Pastikan Type Data yang dimasukkan sudah benar string ataupun integer")

  def update_item_name(self):
    """
    Parameter:
      None

    Input:
      nama_item (str) = sebagai variabel untuk menampung nama barang yang nantinya akan di cek di dictionary
      update_nama_item (str) = sebagai variabel untuk menampung nama barang yang baru
    """
    try:
        #menampilkan tabel barang
        header = ["Nama Barang", "Harga per item" , "Jumlah item","Total harga"]
        print(tabulate(self.all_item, headers = header, tablefmt = "github"))

        #mengupdate nama_item
        nama_item = input("Masukkan nama barang yang ingin diupdate: ") #input nama item yang akan diupdate
        if nama_item in self.all_item["Nama item:"]:  #menagmbil key dari dictionary
            index = self.all_item["Nama item:"].index(nama_item) #mengambil data dari key "Nama item", index item menyesuaikan dari nama item
            update_nama_item = input("Masukkan nama barang yang baru: ") # menginputkan data baru
            self.all_item["Nama item:"][index] = update_nama_item #memasukkan data baru ke dictionary
            print("Nama barang berhasil diupdate.")
        else:
            print("Nama barang tidak ditemukan.")
    except ValueError:
      print("Pastikan Type Data yang dimasukkan sudah benar string ataupun integer")

  def update_item_qty(self):
    """
    parameter:
      None

    input:
      nama_item (str) = sebagai variabel untuk menampung nama barang yang nantinya akan di cek di dictionary
      update_jumlah_item (int) = sebagai variabel untuk menampung jumlah barang yang baru
    """
    header = ["Nama Barang", "Harga per item" , "Jumlah item","Total harga"]
    print(tabulate(self.all_item, headers = header, tablefmt = "github"))
    try:
      nama_item = input("Masukkan nama dari barang yang ingin diubah: ")
      if nama_item in self.all_item["Nama item:"]:
          index = self.all_item["Nama item:"].index(nama_item) #mengambil data dari key "Nama item", index item menyesuaikan dari nama item
          update_jumlah_item = int(input("Masukkan jumlah baru: ")) #masukkan data item baru
          self.all_item["Jumlah item:"][index] = update_jumlah_item #memasukkan data baru ke dictionary
          #otomatis mengubah total harga
          self.all_item["Total harga item:"][index] = update_jumlah_item * self.all_item["Harga per item:"][index]
          print("Jumlah barang berhasil diupdate.")
      else:
          print("Nama barang tidak ditemukan.")
    except ValueError:
      print("Pastikan Type Data yang dimasukkan sudah benar string ataupun integer")

  def update_item_price(self):
    """
    parameter:
      None

    input:
      nama_item (str) = sebagai variabel untuk menampung nama barang yang nantinya akan di cek di dictionary
      update_item_price (int) = sebagai variabel untuk menampung harga barang yang baru
    """
    #Menampilkan table data barang
    header = ["Nama Barang", "Harga per item" , "Jumlah item","Total harga"]
    print(tabulate(self.all_item, headers=header, tablefmt="github"))
    #Mengupdate barang
    try:
      nama_item = input("Masukkan nama dari barang yang ingin diubah: ") #masukkan nama barang yang akan di update
      if nama_item in self.all_item["Nama item:"]:  #untuk mengambil key dalam dictionary
          index = self.all_item["Nama item:"].index(nama_item) #mengambil data dari key "Nama item", index item menyesuaikan dari nama item
          update_harga_item = int(input("Masukkan harga baru: "))   #masukkan haraga yang akan diupdate
          self.all_item["Harga per item:"][index] = update_harga_item #memasukkan data baru ke dictionary

          self.all_item["Total harga item:"][index] = update_harga_item * self.all_item["Jumlah item:"][index] #otomatis menghitung total harga
          print("Harga barang berhasil diupdate.")
      else:
        print("Nama barang tidak ditemukan.")
    except ValueError:
      print("Pastikan Type Data yang dimasukkan sudah benar string ataupun integer")

  def delete_item(self):
    """
    parameter:
      None

    input:
      nama_item (str) = sebagai variabel untuk menampung nama barang yang nantinya akan di cek di dictionary
    """
    #menampilkan table
    header = ["Nama Barang", "Harga per item" , "Jumlah item","Total harga"]
    print(tabulate(self.all_item, headers = header, tablefmt="github"))
    #proses delete
    try:
      nama_item = input("Masukkan nama barang yang ingin dihapus: ") #masukkan nama barang yang akan di hapus
      #akan menghapus semua data dari nama barang
      if nama_item in self.all_item["Nama item:"]:
        index = self.all_item["Nama item:"].index(nama_item)
        del self.all_item["Nama item:"][index]
        del self.all_item["Harga per item:"][index]
        del self.all_item["Jumlah item:"][index]
        del self.all_item["Total harga item:"][index]

        print("Barang berhasil dihapus.")
      else:
        print("Nama barang tidak ditemukan")
    except ValueError:
      print("Pastikan Type Data yang dimasukkan sudah benar string ataupun integer")

  def reset_item(self):
    """
    parameter:
      None

    input:
      choice str.lower : dengan ini inputan string akan dipaksa menjadi huruf kecil

    keterangan:
    mereset semua value dari data pada dictionary
    """
    try:
      while True:
        choice = str(input("Apakah kamu yakin? y/n: ")).lower()
        if choice == 'y':
          #menghapus semua value yang ada pada data dictionary
          for value in self.all_item.values():
            del value[:]
          # self.all_item.clear()
          print("Transaksi berhasil dihapus")
          break
          main_menu()
        elif choice == "n":
          print("Kembali ke menu utama")
          break
          main_menu()
        else:
          print("Input salah. Masukkan antara y / n")
    except ValueError:
      print("Pastikan Type Data yang dimasukkan sudah benar string ataupun integer")

  def check_order(self):
    """
    parameter:
      None

    input:
      None

    keterangan:
    Menampilkan data dictionary dalam bentuk table menggubakan tabulate
    """
    try:
      header = ["Nama Barang", "Harga per item" , "Jumlah item","Total harga"]
      print(tabulate(self.all_item, headers = header, tablefmt = "github"))
    except:
      print("terjadi error")

  def total_harga(self):
    """
    parameter:
      None

    input:
      None
    keterangan:
    - Menampilkan data dictionary dalam bentuk table menggubakan tabulate
    - menghitung diskon dari jumlah total harga
    """
    #menampilkan tabel
    header = ["Nama Barang", "Harga per item" , "Jumlah item","Total harga"]
    print(tabulate(self.all_item, headers = header, tablefmt = "github"))
    try:
      total_price = sum(self.all_item["Total harga item:"]) #menambah total harga seluruh item
      print(f"Total harga seluruh transaksi: {total_price}")
      final_price = 0
      if total_price > 500000: #kondisi untuk mendapatkan diskon
        print("Anda mendapatkan diskon 10%")
        price = total_price * 0.10
        final_price = total_price - price
        print(f'Harga yang anda dapatkan yaitu menjadi {final_price}')
      elif total_price > 300000:
        print("Anda mendapatkan diskon 8%")
        price = total_price * 0.08
        final_price = total_price - price
        print(f'Harga yang anda dapatkan yaitu menjadi {final_price}')
      elif total_price > 200000:
        print("Anda mendapatkan diskon 5%")
        price = total_price * 0.05
        final_price = total_price - price
        print(f'Harga yang anda dapatkan yaitu menjadi {final_price}')
      else:
        print("Anda tidak memiliki diskon")
    except ValueError:
      print("Pastikan Type Data yang dimasukkan sudah benar string ataupun integer")

def main_menu():
  """
    parameter:
      None

    input:

      choice str.lower : dengan ini inputan string akan dipaksa menjadi huruf kecil

    keterangan:
    Menampilkan menu untuk membantu memilih fungsi yang akan dijalankan
    """
  try:
    while True:
      trnsct_123 = Transaction(id_transaksi = id_transaksi)
      print("="*60)
      print("Selamat datang di menu kasir")
      print("Masukkan angka untuk masuk ke menu tertentu")
      print("="*60)
      print("1. Add item")
      print("2. Update item name")
      print("3. Update item quantity")
      print("4. Update item price")
      print("5. Delete item")
      print("6. Reset transaction")
      print("7. Check order")
      print("8. Payment")
      print("9. Exit")

      choice = str(input("Masukkan pilihan Anda: "))
      if choice == "1":
        trnsct_123.add_item()
        #looping jika pengguna ingin memasukkan barang lagi. Jika tidak kembali ke main menu
        while True:
          choice = input("Tambahkan barang lagi? y / n: ").lower()
          try:
            if choice == "y":
              trnsct_123.add_item()
            elif choice == "n":
              print("Menu add item telah selesai")
              print("")
              break
              main_menu()
          except:
            print("Salah input. Masukkan antara y / n!")
      elif choice == "2":
        trnsct_123.update_item_name()
        #looping jika pengguna ingin update nama barang lagi. Jika tidak kembali ke main menu
        while True:
          choice = input("Ganti nama barang lagi? y / n: ").lower()
          try:
            if choice == "y":
              trnsct_123.update_item_name()
            elif choice == "n":
              print("Menu update item name telah selesai")
              print("")
              break
              main_menu()
          except:
            print("Input salah. Masukkan y / n!")
      elif choice == "3":
        trnsct_123.update_item_qty()
        #looping jika pengguna ingin update jumlah barang lagi. Jika tidak kembali ke main menu
        while True:
          choice = input("Update jumlah barang? y / n: ").lower()
          if choice == "y":
            trnsct_123.update_item_qty()
          elif choice == "n":
            print("Menu update jumlah item telah selesai")
            print("")
            break
            main_menu()
          else:
            print("Input salah. Masukkan y / n!")
      elif choice == "4":
        trnsct_123.update_item_price()
        #looping jika pengguna ingin update harga barang lagi. Jika tidak kembali ke main menu
        while True:
          choice = input("Update harga item? y / n: ").lower()
          if choice == "y":
            trnsct_123.update_item_price()
          elif choice == "n":
            print("Menu update harga item selesai")
            print("")
            break
            main_menu()
          else:
            print("Input salah. Masukkan y / n")
      elif choice == "5":
        trnsct_123.delete_item()
        #looping jika pengguna ingin menghapus barang lagi. Jika tidak kembali ke main menu
        while True:
          choice = input("Hapus item lagi? y/n: ").lower()
          if choice == "y":
            trnsct_123.delete_item()
          elif choice == "n":
            print("Menu hapus item telah selesai")
            print("")
            break
            main_menu()
          else:
            print("Input salah. Masukkan y / n!")
      elif choice == "6":
        trnsct_123.reset_item()
      elif choice == "7":
        trnsct_123.check_order()
      elif choice == "8":
        trnsct_123.total_harga()
      elif choice == "9":
        print("Transaksi telah selesai. Keluar dari aplikasi kasir")
        break
  except ValueError:
      print("pastikan menginputkan dengan benar")

id_transaksi = str(input("Masukkan id transaksi: "))


