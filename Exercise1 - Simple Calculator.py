# Calculator Sederhana

print("Selamat datang di kalkulator sederhana")
print("Operator (+, -, x, /)")

operator = input("Masukkan operator : ")
angka_a = float(input("Masukkan angka a : "))
angka_b = float(input("Masukkan angka b : "))

if operator == "+":
    hasil = angka_a + angka_b
    print(f"Hasilnya adalah : {hasil}")
elif operator == "-":
    hasil = angka_a - angka_b
    print(f"Hasilnya adalah : {hasil}")
elif operator == "x":
    hasil = angka_a * angka_b
    print(f"Hasilnya adalah : {hasil}")
elif operator == "/":
    hasil = angka_a / angka_b
    print(f"Hasilnya adalah : {hasil}")
else:
    print("Yang bener lah ASW")