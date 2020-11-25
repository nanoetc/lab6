nim = []
nama = []
tugas = []
uts = []
uas = []
akhir = []
pilihan = True
lihat = "L"
tambah = "T"
ubah = "U"
hapus = "H"
cari = "C"
keluar = "K"
while pilihan != 0:
    print("(L)ihat.", "(T)ambah", "(U)bah", "(H)apus", "(C)ari", "(K)eluar")

    pilihan = input("masukkan pilhan anda : ")
    if pilihan == "T":
        nim1 = input("masukkan nim: ")
        nim.append({'nim': nim1})
        nama1 = input("masukkan nama: ")
        nama.append({'nama': nama1})
        tugas1 = input("masukkan nilai tugas: ")
        tugas.append({'tugas': tugas1})
        uts1 = input("masukkan nilai UTS: ")
        uts.append({'uts': uts1})
        uas1 = input("masukkan nilai UAS: ")
        uas.append({'uas': uas1})
        akhir1 = 0.3*float(tugas1) + 0.35*float(uts1) + 0.35*float(uas1)
        akhir.append({'akhir': akhir1})
    elif pilihan == "L":
        penentu = True
        print("============================================")
        print("nim \t nama \t tugas \t uts \t uas \t akhir")
        print("============================================")
        for i in range(len(nim)):
            print(nim[i]['nim'], '\t', nama[i]['nama'], '\t', tugas[i]['tugas'], '\t', uts[i]['uts'], '\t',
                  uas[i]['uas'], '\t', akhir[i]['akhir'], '\t')
            pententu = False
    elif pilihan == "U":
        pilihan3 = input("masukkan data yang akan diubah : ")
        if pilihan3 == "nim":
            masnim = str(input("masukkan nim :"))
            masnim2 = str(input("masukkan nim yang baru :"))
            for i in range(len(nim)):
                if masnim == nim[i]['nim']:
                    nim[i]['nim'] = masnim2
        elif pilihan3 == "nama":
            masnama = str(input("masukkan nama :"))
            masnama2 = str(input("masukkan nama yang baru :"))
            for i in range(len(nama)):
                if masnama == nama[i]['nama']:
                    print(i)
                    nama[i]['nama'] = masnama2
        elif pilihan3 == "tugas":
            mastugas = str(input("masukkan nilai tugas :"))
            mastugas2 = str(input("masukkan nilai tugas yang baru :"))
            for i in range(len(tugas)):
                if mastugas == tugas[i]['tugas']:
                    tugas[i]['tugas'] = mastugas2
        elif pilihan3 == "uts":
            masuts = input("masukkan nilai uts :")
            masuts2 = input("masukkan nilai uts yang baru :")
            for i in range(len(uts)):
                if masuts == uts[i]['uts']:
                    print(i)
                    uts[i]['uts'] = masuts2
        elif pilihan3 == "uas":
            masuas = str(input("masukkan nilai uas : "))
            masuas2 = input("masukkan nilai uas yang baru :")
            for i in range(len(uas)):
                if masuas == uas[i]['uas']:
                    print(i)
                    uas[i]['uas'] = masuas2
    elif pilihan == "H":
        masnim = input("masukan nim : ")
        for i in range(len(nim)):
            if masnim == nim[i]['nim']:
                del nim[i]
                del nama[i]
                del tugas[i]
                del uts[i]
    elif pilihan == "C":
        cari = input("masukan data yang dicari : ")
        if cari == "nim":
            for i in range(len(nim)):
                print(nim[i]['nim'])
        elif cari == "nama":
            if cari == "nama":
                for i in range(len(nama)):
                    print(nama[i]['nama'])
        elif cari == "tugas":
            if cari == "tugas":
                for i in range(len(tugas)):
                    print(tugas[i]['tugas'])
        elif cari == "uas":
            if cari == "uas":
                for i in range(len(uas)):
                    print(uas[i]['uas'])
        elif cari == "uts":
            if cari == "uts":
                for i in range(len(uts)):
                    print(uts[i]['uts'])
        elif cari == "akhir":
            if cari == "akhir":
                for i in range(len(akhir)):
                    print(akhir[i]['akhir'])
        else:
            print("data yang anda cari tidak ada")
    elif pilihan == "K":
        break
