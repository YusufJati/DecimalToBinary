def KonversiDnC(angka):
    if angka == 0:
        return "0"

    integer_part = int(abs(angka))
    fractional_part = abs(angka) - integer_part

    # Handle integer part
    hasil_integer = DivideAndConquerInteger(integer_part)

    # Handle fractional part
    hasil_fractional = DivideAndConquerFractional(fractional_part)

    # Combine the results
    hasil = hasil_integer + "." + hasil_fractional

    # Handle negative numbers
    if angka < 0:
        hasil = "-" + hasil

    return hasil


def DivideAndConquerInteger(angka):
    if angka <= 1:
        return str(angka)

    mid = angka // 2
    left = DivideAndConquerInteger(mid)
    right = DivideAndConquerInteger(angka - mid)

    return left + right


def DivideAndConquerFractional(angka):
    if angka == 0 or angka >= 1:
        return ""

    mid = angka * 2
    left = str(int(mid))
    right = DivideAndConquerFractional(mid - int(mid))

    return left + right

print(KonversiDnC(2.4))