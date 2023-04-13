class CoffeeMenu:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

class CoffeeOrder:
    def __init__(self, menu, jumlah):
        self.__menu = menu
        self.__jumlah = jumlah

    def get_menu(self):
        return self.__menu

    def get_jumlah(self):
        return self.__jumlah

    def hitung(self):
        harga = self.__menu.get_price() * self.__jumlah
        ppn = int(harga * 0.1)
        if self.__jumlah >= 5:
            diskon = int(harga * 0.2)
            totalharga = int(harga - diskon + ppn)
        else:
            diskon = 0
            totalharga = int(harga + ppn)
        return harga, diskon, ppn, totalharga

# Daftar menu kopi
menu_items = {
    "a": CoffeeMenu("ES Kopi Susu", 11000),
    "b": CoffeeMenu("ES Kopi Coklat", 12000),
    "c": CoffeeMenu("ES Kopi Hitam", 11000),
    "d": CoffeeMenu("Ice Americano", 14000)
}

while True:
    input_awal = input("Apakah ingin memesan? (Y/N): ").lower()
    if input_awal == "y":
        break
    elif input_awal == "n":
        quit()
    else:
        print("Input tidak valid. Masukkan 'y' atau 'n'.")


while True:
    print("""
    ==============================
    
    Ananda Coffee
    List Menu Minuman Kopi
 
    ==============================
    A. ES Kopi Susu    : Rp 11.000
    B. ES Kopi Coklat  : Rp 12.000
    C. ES Kopi Hitam   : Rp 11.000
    D. Ice Americano   : Rp 14.000
    ==============================
    """)

    print("-------------------------------------")
    print("            Sebelum Memesan")
    print("         Silahkan masukkan Nama")
    print("-------------------------------------")

    while True:
        name = input("Nama Anda                            : ")
        if name.strip() != "":
            break
        else:
            print("Nama tidak boleh kosong.")

    while True:
        pilih_menu = input("Masukkan abjad menu kopi (A/B/C/D)   : ").lower()
        if pilih_menu not in menu_items:
            print("Menu tidak tersedia.")
            continue
        break

    while True:
        try:
            jumlah = int(input("Masukan Jumlah Pesanan               : "))
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    # Membuat objek pesanan kopi
    menu = menu_items[pilih_menu]
    order = CoffeeOrder(menu, jumlah)

    # Menghitung harga, diskon, PPN, dan total harga
    harga, diskon, ppn, totalharga = order.hitung()

    # Menampilkan rincian pesanan
    print("-----------------------------------------")
    print("             Ananda Coffee")
    print("-----------------------------------------")
    print("Nama               :", name)
    print("Menu               :", order.get_menu().get_name())
    print("Jumlah Pesan       :", order.get_jumlah())
    print("Harga              :", harga)
    print("Diskon             :", diskon)
    print("PPN                :", ppn)
    print("-----------------------------------------")
    print("Jumlah Bayar       :", totalharga)
    print("-----------------------------------------")

    ulang = input("Apakah Anda ingin memesan lagi? (Y/N): ")
    if ulang.lower() != "y":
        break