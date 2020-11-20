def nim20():
    bop = 4000000
    sks = 200000
    print("BOP mahasiswa angkatan 2020 adalah", bop)
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
                for pengulangan in range(1, semsat):
                    ip = eval(input("Masukkan IP Semester: "))
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
                for pengulangan in range(1, semsat):
                    ip = eval(input("Masukkan IP Semester: "))
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

    elif js < 15:
        print("SKS anda semester ini kurang")
    else:
        print("Inputan Salah")
def nim19():
    bop = 3500000
    sks = 175000
    print("BOP mahasiswa angkatan 2019 adalah", bop)
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
                for pengulangan in range(1, semsat):
                    ip = eval(input("Masukkan IP Semester: "))
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
                for pengulangan in range(1, semsat):
                    ip = eval(input("Masukkan IP Semester: "))
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

    elif js < 15:
        print("SKS anda semester ini kurang")
    else:
        print("Inputan Salah")
def nim18():
    bop = 3200000
    sks = 130000
    print("BOP mahasiswa angkatan 2018 adalah", bop)
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
                for pengulangan in range(1, semsat):
                    ip = eval(input("Masukkan IP Semester: "))
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
                for pengulangan in range(1, semsat):
                    ip = eval(input("Masukkan IP Semester: "))
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

    elif js < 15:
        print("SKS anda semester ini kurang")
    else:
        print("Inputan Salah")
def nim17():
    bop = 2800000
    sks = 130000
    print("BOP mahasiswa angkatan 2017 adalah", bop)
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
                for pengulangan in range(1, semsat):
                    ip = eval(input("Masukkan IP Semester: "))
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
                for pengulangan in range(1, semsat):
                    ip = eval(input("Masukkan IP Semester: "))
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

    elif js < 15:
        print("SKS anda semester ini kurang")
    else:
        print("Inputan Salah")
nim = input("Masukkan NIM Anda: ")
if nim[5:7]=='20' and len(nim)==10:
    nim20()
elif nim[5:7]=='19' and len(nim)==10:
    nim19()
elif nim[5:7]=='18' and len(nim)==10:
    nim18()
elif nim[5:7]=='17' and len(nim)==10:
    nim17()
else:
    print("NIM anda Tidak Benar")