keranjangBelanja = []

while (True) :
    belanja = []
    namaBarang = input ("Masukkan Nama Barang : ")
    hargaSatuan = int(input ("Masukkan Harga Satuan : "))
    jumlahBeli = int(input ("Masukkan Jumlah Pembelian : "))
    belanja.append(namaBarang)
    belanja.append(hargaSatuan)
    belanja.append(jumlahBeli)
    belanja.append(hargaSatuan*jumlahBeli)

    keranjangBelanja.append(belanja)

    cekTambah = input ("Ada Barang Berikutnya ? (ya) ")
    if cekTambah == "ya" :
        continue
    else :
        break 
    
print("\nWARUNG MA ITI")
print("JALAN RUSAK NO.145 JAKARTA TENGGARA")
print("=====================================")

jumlahList = len(keranjangBelanja)

total = 0
for i in range(jumlahList):
    print(keranjangBelanja[i][0])
    print(keranjangBelanja[i][2],"*",keranjangBelanja[i][1],"=",keranjangBelanja[i][3],"\n")
    total = total + keranjangBelanja[i][3]
   
print ("Total :" , total  )




