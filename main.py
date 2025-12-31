
import aritmatika
import suhu
import satuan
import biner
import diskon
import currency
import bmi   

def main():
    while True:
        print("\n=== KALKULATOR ADVANCE ===")
        menu = [
            "Aritmatika Dasar",
            "Konversi Suhu",
            "Konversi Gram ke Kg",
            "Konversi Desimal ke Biner",
            "Hitung Diskon",
            "Konversi Mata Uang (IDR → USD & EUR)",
            "Hitung Body Mass Index (BMI)",
            "Keluar"
        ]

        for i, item in enumerate(menu, start=1):
            print(f"{i}. {item}")

        pilihan = input("Pilih menu (1-8): ")

        if pilihan == "1":
            aritmatika.kalkulator_aritmatika()
        elif pilihan == "2":
            suhu.konversi_suhu()
        elif pilihan == "3":
            satuan.gram_ke_kg()
        elif pilihan == "4":
            biner.desimal_ke_biner()
        elif pilihan == "5":
            diskon.hitung_diskon()
        elif pilihan == "6":
            currency.konversi_mata_uang()
        elif pilihan == "7":
            bmi.hitung_bmi()
        elif pilihan == "8":
            print("Terima kasih telah menggunakan kalkulator.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
