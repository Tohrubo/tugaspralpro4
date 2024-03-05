# Buatlah sebuah fungsi yang dapat menentukan apakah ketiga parameter memenuhi
# semua ketentuan berikut ini:
# • Ketiga parameter tersebut nilainya berbeda semua.
# • Ada kemungkinan jika diambil dua parameter dan dijumlahkan hasilnya sama dengan
# parameter lainnya (yang tersisa).
# Fungsi tersebut akan menghasilkan nilai True jika semua ketentuan tersebut dipenuhi. Jika
# tidak terpenuhi maka fungsi akan menghasilkan nilai False. Fungsi anda harus diberi nama
# cek_angka()

def cek_angka(n1, n2, n3):
    if (n1 != n2 != n3 != n1) and (n1+n2 == n3 or n2+n3 == n1 or n1+n3 == n2):
        return True
    else:
        return False

num1 = input("Input 1st number: ")
num2 = input("Input 2nd number: ")
num3 = input("Input 3rd number: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
except:
    print("Please use numbers, not words")
    exit()
    
result = cek_angka(num1, num2, num3)
print(result)