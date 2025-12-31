
def desimal_ke_biner():
    print("\n=== Konversi Desimal ke Biner ===")

    angka = int(input("Masukkan bilangan bulat (desimal): "))

    if angka < 0:
        print("Bilangan harus positif!")
        return

    if angka == 0:
        print("Hasil: 0")
        return

    hasil_biner = []
    temp = angka

    while temp > 0:
        sisa = temp % 2
        hasil_biner.append(str(sisa))
        temp //= 2

    hasil_biner.reverse()
    print(f"Hasil biner dari {angka} adalah: {''.join(hasil_biner)}")
    