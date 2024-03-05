# Buatlah sebuah fungsi yang dapat menentukan apakah minimal dua dari tiga
# parameter yang diberikan memiliki digit paling kanan yang sama. Fungsi tersebut menghasilkan
# nilai True jika memenuhi dan False jika tidak memenuhi. Gunakan fungsi tersebut untuk
# mengecek beberapa test-case berikut ini:
# • Input = 30, 20, 18. Output yang diharapkan = True
# • Input = 145, 5, 100. Output yang diharapkan = True
# • Input = 71, 187, 18. Output yang diharapkan = False
# • Input = 1024, 14, 94. Output yang diharapkan = True
# • Input = 53, 8900, 658. Output yang diharapkan = False
# Ketiga bilangan tersebut diinputkan oleh pengguna, sehingga anda perlu membaca input dari
# pengguna. Fungsi anda harus diberi nama cek_digit_belakang(). 

def cek_digit_belakang(n1, n2, n3):
    tn1 = n1 % 10
    tn2 = n2 % 10
    tn3 = n3 % 10
    if (tn1 == tn2 or tn2 == tn3 or tn1 == tn3):
        return True
    else:
        return False
    
num1 = input("Insert 1st number: ")
num2 = input("Insert 2nd number: ")
num3 = input("Insert 3rd number: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
except:
    print("Please use numbers, not words")
    exit()

result = cek_digit_belakang(num1, num2, num3)
print(result)