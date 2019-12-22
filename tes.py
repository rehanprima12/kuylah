# 1 . MENGHITUNG NILAI AKHIR MAHASISWA

NAMA= input("Masukan NAMA         : ")
UTS = int(input("Masukan Nilai UTS    : "))
UAS= int(input("Masukan Nilai UAS     : "))
TUGAS= int(input("Masukan Nilai Tugas : ")) 

print(("NAMA       :"),NAMA)
print(("UTS        :"),UTS)
print(("UAS        :"),UAS)
print(("Tugas      :"),TUGAS)


akhir =int(UTS+UAS+TUGAS)/3
print(("Nilai akhir     :"),akhir)
if akhir>80:
    print ("Nilai huruf       : A")

    
    print ("Keterangan         :LULUS")
elif akhir>=70 and akhir <=80 :
    print (" Nilai huruf       : B")
    print ("Keterangan         :LULUS")
elif akhir>=65 and akhir <=70 :
    print (" Nilai huruf       : C")
    print ("Keterangan         :TIDAK LULUS")
elif akhir>=40 and akhir <=50 :
    print (" Nilai huruf       : D")
    print ("Keterangan         : TIDAK LULUS")
elif akhir>=0 and akhir <=30  :
    print (" Nilai huruf       : E")
    print ("Keterangan         : TIDAK LULUS")