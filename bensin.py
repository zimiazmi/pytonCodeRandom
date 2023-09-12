PREMIUM = 6450
PERTALITE = 7650
PERTAMAX = 9000
PERTAMAXTURBO = 9850
BIOSOLAR = 5150
DEXLITE = 9500
DEX = 10200

JenisBensin = input("Masukkan Jenis BBM yang ingin dibeli : ").upper()
jumlahLiter = int(input("masukkan Jumlah Liter : "))

if JenisBensin=="PREMIUM":
    total = jumlahLiter * PREMIUM
    if jumlahLiter > 10:
        print("Maaf, jumlah pembelian maksimal BBM ", JenisBensin, "adalah 10 liter")
    print("Jumlah yang harus dibayar Rp. ", total)
elif JenisBensin == "PERTALITE" :
    total = jumlahLiter * PERTALITE
    if jumlahLiter > 10:
        print("Maaf, jumlah pembelian maksimal BBM ", JenisBensin, "adalah 10 liter")
    print("Jumlah yang harus dibayar Rp. ", total)
elif JenisBensin == "PERTAMAX" :
    total = jumlahLiter * PERTAMAX
    if jumlahLiter > 10:
        print("Maaf, jumlah pembelian maksimal BBM ", JenisBensin, "adalah 10 liter")
    print("Jumlah yang harus dibayar Rp. ", total)
elif JenisBensin == "PERTAMAXTURBO" :
    total = jumlahLiter * PERTAMAXTURBO
    if jumlahLiter > 10:
        print("Maaf, jumlah pembelian maksimal BBM ", JenisBensin, "adalah 10 liter")
    print("Jumlah yang harus dibayar Rp. ", total)
elif JenisBensin == "BIOSOLAR" :
    total = jumlahLiter * BIOSOLAR
    if jumlahLiter > 10:
        print("Maaf, jumlah pembelian maksimal BBM ", JenisBensin, "adalah 10 liter")
    print("Jumlah yang harus dibayar Rp. ", total)
elif JenisBensin == "DEXLITE" :
    total = jumlahLiter * DEXLITE
    if jumlahLiter > 10:
        print("Maaf, jumlah pembelian maksimal BBM ", JenisBensin, "adalah 10 liter")
    print("Jumlah yang harus dibayar Rp. ", total)
elif JenisBensin == "DEX" :
    total = jumlahLiter * DEX
    if jumlahLiter > 10:
        print("Maaf, jumlah pembelian maksimal BBM ", JenisBensin, "adalah 10 liter")
    print("Jumlah yang harus dibayar Rp. ", total)
else :
    print("Bensin Tidak tersedia")
