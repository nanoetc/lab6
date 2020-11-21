stop = False
nama = [];
nim = [];
nilaitugas = [];
nilaiuts = [];
nilaiuas = [];
nilaiakhir = [];
i = 0
a = int(len(nama))
berhenti = False
while(not stop):
    nama1 = input("NAMA = ")
    nama.append(nama1)
    nim1 =input("NIM = ")
    nim.append(nim1)
    nilaitugas1 =int(input("NILAI Tugas = "))
    nilaitugas.append(nilaitugas1)
    nilaiuts1 =int(input("NILAI UTS = "))
    nilaiuts.append(nilaiuts1)
    nilaiuas1 =int(input("nilai uas = "))
    nilaiuas.append(nilaiuas1)
    nilaiakhir1 = nilaitugas1*0.3
    nilaiakhir2 = nilaiuts1*0.35
    nilaiakhir3 = nilaiuas1*0.35
    nilaiakhir4 = nilaiakhir1 + nilaiakhir2 + nilaiakhir3
    nilaiakhir.append(nilaiakhir4)
    tanya = input("tambahkan data ya/tidak")
    if(tanya == "tidak"):
        stop = True
print("=================================================")
print("nama","  | ","nim","   | ","tugas","   | ","uts","   | ","uas","   | ","akhir")  
print("=================================================")
while (not berhenti):
       print(nama[i],nim[i],nilaitugas[i],nilaiuts[i],nilaiuas[i],nilaiakhir[i], sep="    |   ")
       i += 1
       if(i <= a):
           berhenti = True

