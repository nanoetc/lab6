
from data import *

while pilihan !=0:
    print("(L)ihat.", "(T)ambah", "(U)bah", "(H)apus", "(C)ari")
    pilihan = input("masukkan pilhan anda : ")
    if pilihan == "T":
        tambah()
    elif pilihan == "L":
        lihat()
    elif pilihan == "U":
        ubah()
    elif pilihan == "H":
        hapus()
    elif pilihan == "C":
        cari()
    else:
        keluar()
        break

