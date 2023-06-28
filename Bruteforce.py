"""
    Nama file: Bruteforce.py
    Nama Pembuat: Muhamad Aditya Yusuf Jatikusumo
    Deskripsi: Program ini merupakan program yang mengimplementasikan algoritma Divide and Conqueror dan Brute Force dalam 
            kasus konversi nilai desimal ke biner
"""
import time

# Menggunakan Algoritma Bruteforce
# Kasus: Konversi nilai desimal ke biner
# Bruteforce

start = time.time()
print("===================== Brute Force =====================")
def KonversiBruteForce(angka):
    hasil = ""
    bagi = 0
    pembanding = 0
    if angka == 0: 
        hasil = hasil + "000"
    while angka > 0: 
        hasil = str(angka % 2) + hasil
        angka = angka // 2
        bagi += 1
        if pembanding < angka:
            pembanding = angka
    return hasil
print("Hasil dari konversi adalah:", KonversiBruteForce(4))
#a = int(input("Masukkan angka yang ingin dikonversi: "))
#KonversiBruteForce(a)
#print("Hasil dari konversi adalah:", KonversiBruteForce(a))
end = time.time()
print("Waktu hasil eksekusi adalah:",end - start,"s")
print("=========================================================")