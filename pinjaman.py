#=======================soal 1===============================================
# pinjaman =int(input("Masukkan jumlah pinjaman: "))
# jangkaWaktu = int(input("Masukkan jangka waktu peminjaman (dalam bulan): "))
# bunga = float(0.1)

# for i in range(jangkaWaktu):
#     total_bunga =pinjaman * bunga
#     pinjaman = total_bunga + pinjaman
    
# print("Pinjaman yang harus dibayar setelah jatuh tempo:", int(pinjaman))

#========================soal 2================================================
pinjamanAwal = int(input("Masukkan jumlah pinjaman: "))
waktuPinjaman = int(input("masukkan jangka waktu peminjaman (dalam bulan): "))

# if waktuPinjaman<1 :
    

for i in range(waktuPinjaman):

    sakit = input("Bulan ke " + str(i+1) + " apakah peminjaman sakit? ").lower().strip()
    if sakit == "false" :
        totalBunga = pinjamanAwal * 0.1
        pinjamanAwal = totalBunga + pinjamanAwal
    elif sakit == "true" :
        pinjamanAwal = pinjamanAwal
    else :
        print("Masukkan Nilai : [ True / False ]")
        # reversed(i-1)
        # break:
        # i=reversed(range(i))
        # i += 1
        # range(i+1).start
    
print("Pinjaman yang harus dibayar setelah jatuh tempo:", int(pinjamanAwal))

# pinjaman = int(input("Masukkan jumlah pinjaman: "))
# bulan = int(input("Masukkan bulan: "))
# bunga = 0.1
# limit = 0

# while limit < bulan:
#     isSakit = raw_input("Sakit? ")
#     if isSakit == "ya":
#         limit += 1
#         continue
#     elif isSakit == "tidak":
#         limit += 1
#         total_bunga = pinjaman * bunga
#         pinjaman = pinjaman + total_bunga
#     else:
#         continue
# #
# # for i in range(bulan):
# #     isSakit = input("Sakit? ")
# #     if isSakit:
# #         continue
# #     total_bunga = pinjaman * bunga
# #     pinjaman = pinjaman + total_bunga

# print("Hutang akhir", pinjaman)
