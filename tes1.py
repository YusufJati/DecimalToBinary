def Konversi(angka):
    hasil = ""
    bagi = 0
    banding = 0

    # Handle negative numbers
    is_negative = False
    if angka < 0:
        is_negative = True
        angka = abs(angka)

    # Handle integer part
    integer_part = int(angka)
    if integer_part == 0:
        hasil = "0"
    else:
        while integer_part > 0:
            hasil = str(integer_part % 2) + hasil
            integer_part = integer_part // 2

    # Handle fractional part
    hasil += "."
    fractional_part = angka - int(angka)
    while fractional_part > 0:
        if len(hasil) > 64:  # Limit the length of fractional part to avoid infinite loops
            break
        fractional_part *= 2
        bit = int(fractional_part)
        hasil += str(bit)
        fractional_part -= bit
        print("Hasil konversi: ", hasil)
        print("Jumlah pembagian: ", bagi)
        print()
        print("Jumlah perbandingan: ", banding)
        bagi += 1
        if banding < integer_part:
            banding = integer_part

    # Handle special cases
    if angka == 0:
        hasil = "0"
    if is_negative:
        hasil = "-" + hasil

    return hasil

#print(Konversi(0.5))

def KonversiBruteForce(angka):
    integer_part = int(abs(angka))
    fractional_part = abs(angka) - integer_part

    # Handle integer part
    hasil = ""
    if integer_part == 0:
        hasil = "0"
    else:
        while integer_part > 0:
            hasil = str(integer_part % 2) + hasil
            integer_part = integer_part // 2

    # Handle fractional part
    hasil += "."
    precision = 3  # Set the desired precision for the fractional part
    while fractional_part > 0 and precision > 0:
        fractional_part *= 2
        bit = int(fractional_part)
        hasil += str(bit)
        fractional_part -= bit
        precision -= 1

    # Handle special cases
    if angka == 0:
        hasil = "0"
    if angka < 0:
        hasil = "-" + hasil

    return hasil
#print(KonversiBruteForce(0.15))
