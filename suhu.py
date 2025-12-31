
def konversi_suhu():
    menu = ["Celcius ke Fahrenheit", "Fahrenheit ke Celcius"]

    print("\n=== Konversi Suhu ===")
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item}")

    pilihan = int(input("Pilih menu (1-2): "))

    if pilihan == 1:
        c = float(input("Masukkan suhu Celcius: "))
        f = (c * 9 / 5) + 32
        print(f"Hasil: {f} °F")
    elif pilihan == 2:
        f = float(input("Masukkan suhu Fahrenheit: "))
        c = (f - 32) * 5 / 9
        print(f"Hasil: {c} °C")
    else:
        print("Pilihan tidak valid!")
