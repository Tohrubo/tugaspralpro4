# Buatlah fungsi-fungsi konversi suhu menggunakan lambda function. Fungsi-fungsi
# yang harus anda implementasikan:
# • Celcius to Fahrenheit. F = (9/5) ∗C +32
# • Celcius to Reamur. R = 0.8 ∗C
# Berikan contoh penggunaannya untuk test-case berikut ini:
# • Input C = 100. Output F = 212.
# • Input C = 80. Output R = 64.
# • Input = 0. Output F = 32.


fhr = lambda c: (9/5)*c +32
rem = lambda c: 0.8*c

celc = input("Input temp to convert: ")

try:
    celc = int(celc)
except:
    print("Please us numbers, not words")
    exit()

print(f"Temprature in Fahrenheit: {fhr(celc)}")
print(f"Temprature in Reamur: {rem(celc)}")