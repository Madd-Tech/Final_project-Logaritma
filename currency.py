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

    # Menggunakan API publik yang gratis dan tidak memerlukan API key
    url = "https://api.exchangerate-api.com/v4/latest/IDR"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

        rate_usd = data["rates"]["USD"]
        rate_eur = data["rates"]["EUR"]

    except Exception as e:
        print(f"\n(Info: Gagal mengambil kurs real-time: {e})")
        print("(Menggunakan kurs estimasi)")
        # Fallback rates (Estimasi kasar)
        rate_usd = 1 / 16000  
        rate_eur = 1 / 17500

    print("\n--- Hasil Konversi ---")
    print(f"IDR : Rp {idr:,}")

    if pilihan_currency in ["1", "3"]:
        print(f"USD : $ {(idr * rate_usd):,.2f}")

    if pilihan_currency in ["2", "3"]:
        print(f"EUR : € {(idr * rate_eur):,.2f}")
