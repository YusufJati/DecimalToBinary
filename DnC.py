"""
    Nama file: DnC.py
    Nama Pembuat: Muhamad Aditya Yusuf Jatikusumo
    Deskripsi: Program ini merupakan program yang mengimplementasikan algoritma Divide and Conqueror dan Brute Force dalam 
            kasus konversi nilai desimal ke biner
"""
import time
# Kasus: Konversi nilai desimal ke biner
# Metode: Divide and Conqueror
start = time.time()
print("===================== Divide and Conqueror =====================")
def KonversiDnC(angka):
    hasil = ""
    if angka <= 8:
        hasil = "{:03b}".format(angka) 
        print(f"Conquer: {angka} -> {hasil}")
    else:
        temp1 = angka // 8  
        print(f"Divide1: {angka} -> {temp1}")
        temp2 = angka % 8
        print(f"Divide2: {angka} -> {temp2}")
        hasil1 = KonversiDnC(temp1)
        hasil2 = KonversiDnC(temp2)
        hasil = hasil + hasil1 + hasil2
        print(f"Combine: {temp1} -> {hasil1}, {temp2} -> {hasil2} -> {hasil}")
    return hasil
print()
a = int(input("Masukkan angka yang ingin dikonversi: "))
print("Hasil dari konversi adalah:", KonversiDnC(a))
end = time.time()
print("Waktu hasil eksekusi adalah:",end - start,"s")
print("=================================================================")

