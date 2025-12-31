import urllib.request
import urllib.parse
import json

def konversi_mata_uang():
    print("\n=== Konversi Mata Uang (IDR → USD & EUR) ===")

    try:
        idr = int(input("Masukkan jumlah uang (IDR, bilangan bulat): "))
        if idr < 0:
            print("Jumlah uang tidak boleh negatif!")
            return
    except ValueError:
        print("Input tidak valid! Gunakan bilangan bulat, contoh: 100000")
        return

    print("\nPilih mata uang tujuan:")
    print("1. USD")
    print("2. EUR")
    print("3. Keduanya")
    pilihan_currency = input("Masukkan pilihan (1-3): ")

    base_url = "https://api.exchangerate.host/latest"
    params = {
        "base": "IDR",
        "symbols": "USD,EUR"
    }

    try:
        query_string = urllib.parse.urlencode(params)
        url = f"{base_url}?{query_string}"

        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

        rate_usd = data["rates"]["USD"]
        rate_eur = data["rates"]["EUR"]

    except Exception:
        print("\n(Info: Gagal mengambil kurs real-time, menggunakan kurs estimasi)")
        rate_usd = 1 / 15500
        rate_eur = 1 / 16800

    print("\n--- Hasil Konversi ---")
    print(f"IDR : Rp {idr:,}")

    if pilihan_currency in ["1", "3"]:
        print(f"USD : $ {(idr * rate_usd):,.2f}")

    if pilihan_currency in ["2", "3"]:
        print(f"EUR : € {(idr * rate_eur):,.2f}")
