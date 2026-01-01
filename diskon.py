
def hitung_diskon():
    print("\n=== Kalkulator Diskon ===")

    harga_asli = float(input("Masukkan harga asli: "))
    persen_diskon = float(input("Masukkan diskon (%): "))

    if harga_asli < 0 or persen_diskon < 0:
        print("Harga dan diskon tidak boleh negatif!")
        return

    if persen_diskon > 100:
        print("Diskon tidak boleh lebih dari 100%!")
        return

    nilai_diskon = harga_asli * (persen_diskon / 100)
    harga_akhir = harga_asli - nilai_diskon

    print("\n--- Hasil Perhitungan ---")
    print(f"Harga Asli   : Rp {harga_asli:,.2f}")
    print(f"Diskon       : {persen_diskon}%")
    print(f"Potongan     : Rp {nilai_diskon:,.2f}")
    print(f"Harga Akhir  : Rp {harga_akhir:,.2f}")
