"""
    Nama file: Bruteforce.py
    Nama Pembuat: Muhamad Aditya Yusuf Jatikusumo
    Deskripsi: Program ini merupakan program yang mengimplementasikan algoritma Divide and Conqueror dan Brute Force dalam 
            kasus konversi nilai desimal ke biner
"""

# Menggunakan Algoritma Bruteforce
# Kasus: Konversi nilai desimal ke biner
# Bruteforce

print("===================== Brute Force =====================")
def KonversiBruteForce(angka):
    hasil = ""
    bagi = 0
    pembanding = 0
    if angka == 0: # Handle kasus 0
        hasil = hasil + "000"
    while angka > 0: # Handle kasus > 0
        print("Langkah ke-", bagi + 1)
        hasil = str(angka % 2) + hasil
        angka = angka // 2
        bagi += 1
        if pembanding < angka:
            pembanding = angka
        print("Hasil konversi: ", hasil)
        print()
        print("Jumlah pembagian: ", bagi)
        print()
        print("Jumlah perbandingan: ", pembanding)
a = int(input("Masukkan angka yang ingin dikonversi: "))
KonversiBruteForce(a)
print("=========================================================")

"""
    Nama file: DnC.py
    Nama Pembuat: Muhamad Aditya Yusuf Jatikusumo
    Deskripsi: Program ini merupakan program yang mengimplementasikan algoritma Divide and Conqueror dan Brute Force dalam 
            kasus konversi nilai desimal ke biner
"""

# Kasus: Konversi nilai desimal ke biner
# Divide and Conqueror
print("===================== Divide and Conqueror =====================")
def KonversiDnC(angka):
    hasil = ""
    if angka <= 8:
        # Merupakan base case
        # if angka == 0:
        #     hasil = hasil + "000"
        # elif angka == 1:
        #     hasil = hasil + "001"  
        # elif angka == 2:
        #     hasil = hasil + "010"
        # elif angka == 3:
        #     hasil = hasil + "011"
        # elif angka == 4:
        #     hasil = hasil + "100"
        # elif angka == 5:
        #     hasil = hasil + "101"
        # elif angka == 6:
        #     hasil = hasil + "110"
        # elif angka == 7:
        #     hasil = hasil + "111"
        # elif angka == 8:
        #     hasil = hasil + "1000"
        hasil = "{:03b}".format(angka) # Conqueror
        print(f"Conqueror: {angka} -> {hasil}")
    else:
        # Merupakan bagian dari Divide and Conqueror
        temp1 = angka // 8  
        print(f"Divide: {angka} -> {temp1}") # Divide 1
        temp2 = angka % 8
        print(f"Divide: {angka} -> {temp2}") # Divide 2
        hasil1 = KonversiDnC(temp1)
        hasil2 = KonversiDnC(temp2)
        hasil = hasil + hasil1 + hasil2 # Rekursif atau merupakan bagian combine
        print(f"Combine: {temp1} -> {hasil1}, {temp2} -> {hasil2} -> {hasil}")
        # Konversi kembali ke desimal
        print(f"Hasil setelah dikonversi kembali adalah: {int(hasil, 2)}")
    return hasil 
print()
print("Hasil konversi: ",KonversiDnC(10))
print("=================================================================")

def KonversiDesimal(biner):
    panjang = len(biner)
    hasil = 0

    for i in range(panjang):
        digit = int(biner[i])
        pangkat = panjang - i - 1
        hasil += digit * (2 ** pangkat)

    return hasil
#print("Hasil konversi kembali: ",KonversiDesimal(KonversiBruteForce(4)))

