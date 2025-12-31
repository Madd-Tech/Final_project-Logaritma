
def hitung_bmi():
    print("\n=== Kalkulator Body Mass Index (BMI) ===")

    try:
        berat = float(input("Masukkan berat badan (kg): "))
        tinggi_cm = float(input("Masukkan tinggi badan (cm): "))

        if berat <= 0 or tinggi_cm <= 0:
            print("Berat dan tinggi harus lebih dari 0!")
            return
    except ValueError:
        print("Input harus berupa angka!")
        return

    tinggi_m = tinggi_cm / 100
    bmi = berat / (tinggi_m ** 2)

    # kategori BMI (array + pengkondisian)
    kategori = [
        ("Kurus", bmi < 18.5),
        ("Normal", 18.5 <= bmi < 25),
        ("Overweight", 25 <= bmi < 30),
        ("Obesitas", bmi >= 30)
    ]

    hasil_kategori = ""
    for nama, kondisi in kategori:
        if kondisi:
            hasil_kategori = nama
            break

    print("\n--- Hasil BMI ---")
    print(f"Berat Badan : {berat} kg")
    print(f"Tinggi     : {tinggi_cm} cm")
    print(f"BMI        : {round(bmi, 2)}")
    print(f"Kategori   : {hasil_kategori}")
