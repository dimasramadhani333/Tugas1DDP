def nimfungsi():
    print("BOP mahasiswa angkatan", ang, "adalah", bop)
    js = eval(input("Jumlah SKS yang diambil semester ini? "))
    if js > 15:
        bsks=(js-15)*sks
        total=bop + bsks
        print("Biaya tambahan untuk", js - 15, "SKS: ", bsks)
        print("Total biaya kuliah: ", total, "\n")
        subs = input("Apakah kamu ingin mengajukan subsidi biaya kuliah (Y/T)? ")
        if subs == 'Y' or subs =='y':
            rip = 0
            avg = 0
            semsat = eval(input("Semester berapa anda sekarang? "))
            if semsat > 1 and semsat < 9:
                # pengulangan = 0
                for pengulangan in range(1, semsat):
                    ip = eval(input("Masukkan IP Semester " + str(pengulangan) + ": "))
                    avg = avg + ip
                rip = avg/(semsat-1)
                dpsubs = (round(rip, 2)/4.00 * 1000000)
                print("Anda mendapatkan subsidi sebesar Rp.", round(dpsubs))
                print("Total biaya kuliah anda: Rp.", bop - round(dpsubs))
            else:
                print("Anda tidak dapat mengajukan subsidi.")
        elif subs == 'T' or subs =='t':
            print("Penghitungan biaya kuliah selesai.")
        else:
            print("Inputan Salah")
    elif js == 15:
        subs = input("Apakah kamu ingin mengajukan subsidi biaya kuliah (Y/T)? ")
        if subs == 'Y' or subs =='y':
            rip = 0
            avg = 0
            semsat = eval(input("Semester berapa anda sekarang? "))
            if semsat > 1 and semsat < 9:
                pengulangan = 0
                for pengulangan in range(1, semsat):
                    ip = eval(input("Masukkan IP Semester: "))
                    avg = avg + ip
                rip = avg/(semsat-1)
                dpsubs = (round(rip, 2)/4.00 * 1000000)
                print("Anda mendapatkan subsidi sebesar Rp.", round(dpsubs))
                print("Total biaya kuliah anda: Rp.", bop - round(dpsubs))
            else:
                print("Anda tidak dapat mengajukan subsidi.")
nim = input("Masukkan NIM Anda: ")
if nim[5:7]=='20' and len(nim)==10:
    bop = 4000000
    sks = 200000
    ang = "2020"
    nimfungsi()
elif nim[5:7]=='19' and len(nim)==10:
    bop = 3500000
    sks = 175000
    ang = "2019"
    nimfungsi()
elif nim[5:7]=='18' and len(nim)==10:
    bop = 3200000
    sks = 150000
    ang = "2018"
    nimfungsi()
elif nim[5:7]=='17' and len(nim)==10:
    bop = 2800000
    sks = 130000
    ang = "2017"
    nimfungsi()
else:
    print("NIM anda Tidak Benar")