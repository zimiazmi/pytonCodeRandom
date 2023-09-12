print("Selamat Datang Di Tugas Akhir Python, kali ini kita akan bermain tebak kata buah")
print("poin kalian akan bertambah bila benar\n")
koleksiBuah=["anggur", "apel", "alpukat","mangga","jambu",
             "pisang","jeruk", "pepaya", "melon","stroberi",
             "salak","semangka","belimbing","dukuh","kelapa",
             "pir","manggis","durian","sirsak","leci","kurma",
             "kesemek","belimbing"]

n=len(koleksiBuah)
mulai = True
poin = 0
status = 0
pilihanUser = []

while(mulai):

    buah=input("Tebak Dan Masukkan Nama Buah ?").lower().strip() 
    # melakukan looping untuk mengcek nama buah yang dimasukkan dengan list buah
    for i in range(n):
        # bila kata buah tidak ditemukan status menjadi 0
        if (buah == koleksiBuah[i]):  
        # status menjadi 1 saat ditemukan kesamaan kata dan menambah poin 
            status = status + 1
            poin=poin + 20 
            #memasukkan nama buah kedalam list pilihanUser
            pilihanUser.append(buah) 
        else :
            status = status + 0  
         
    if (status > 0):
    # menyeleksi kata buah yang sudah terpilih
        print (buah)
        
        for i in range (len(pilihanUser)-1):
        # cek duplikasi nama buah yang dimasukkan
            if (buah==pilihanUser[i]):
                poin = poin - 20
                print("maaf, nama buah sudah pernah dimasukkan")
                print("total poin anda yaitu :" , poin)
                mulai = False
            
        print("yaay berhasil buah tersebut ada di list kami\n")
        status = 0
        if (poin == 100):
            print ("selamat anda mencapai perfect score !! : ", poin)
            break
        else:
            continue
                
    else :
        print("Yah belum beruntung, kata tersebut tidak ada di list")
        print("total poin anda yaitu :" , poin)
        mulai = False




