
def kalkulator_aritmatika():
    operasi = ["+", "-", "*", "/"]

    print("\n=== Kalkulator Aritmatika ===")
    print("Pilih operasi:")
    for i, op in enumerate(operasi, start=1):
        print(f"{i}. {op}")

    pilihan = int(input("Masukkan pilihan (1-4): "))
    if pilihan < 1 or pilihan > 4:
        print("Pilihan tidak valid!")
        return

    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))

    if operasi[pilihan - 1] == "+":
        hasil = a + b
    elif operasi[pilihan - 1] == "-":
        hasil = a - b
    elif operasi[pilihan - 1] == "*":
        hasil = a * b
    elif operasi[pilihan - 1] == "/":
        if b == 0:
            print("Error: Pembagian dengan nol!")
            return
        hasil = a / b

    print("Hasil:", hasil)
