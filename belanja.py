print("Selamat datang di toko souvenir One Piece \n kami menyediakan beberapa item seperti : \n 1. Baju \n 2. Jaket \n 3. Topi \n 4. Action Figure \n 5. Parfume \n 6. Gantungan Kunci")

list_baju = [
    ["Baju Luffy",85000],
    ["Baju Zoro", 80000],
    ["Baju Nami", 75000]
]

ulang = True
while ulang :

    pilih = int(input("Silahkan masukkan pilihan barang yang ingin anda beli :"))

    if pilih == 1 :
        print("Anda Memilih Baju")
        # for lists in list_baju:
        print(list_baju)
        ulang_input = input("Apakah masih ada yang product yang ingin anda lihat : [y/n]")
    elif pilih == 2 :
        print("Anda Memilih Jaket")
        ulang_input = input("Apakah masih ada yang product yang ingin anda lihat : [y/n]")
    elif pilih == 3 :
        print("Anda Memilih Topi")
        ulang_input = input("Apakah masih ada yang product yang ingin anda lihat : [y/n]")
    elif pilih == 4 :
        print("Anda Memilih Action Figure")
        ulang_input = input("Apakah masih ada yang product yang ingin anda lihat : [y/n]")
    elif pilih == 5 :
        print("Anda Memilih Parfume")
        ulang_input = input("Apakah masih ada yang product yang ingin anda lihat : [y/n]")
    elif pilih == 6 :
        print("Anda Memilih Gantungan Kunci")
        ulang_input = input("Apakah masih ada yang product yang ingin anda lihat : [y/n]")
    else :
        print("Masukkan Anda Tidak Ada Pada Daftar")

     
    if ulang_input == "n" :
        ulang = False
    else :
        ulang = True
