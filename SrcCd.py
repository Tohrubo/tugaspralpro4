import random

# def damage(hp):
#     hit = random.randint(1,10)
#     hp -= hit
#     return hp

# health = 100
# while health > 0:
#     act = input("Action: ")
#     if act == "attack":
#         health = damage(health)
#     else:
#         print("Invalid")
#     print(health)

# def calculator(n1, n2, op):
#     if op == "+":
#         r = n1+n2
#     elif op == "-":
#         r = n1-n2
#     elif op == "*":
#         r = n1*n2
#     elif op == "/":
#         r = n1/n2
#     else:
#         return ("Invalid operator")
#     return r

# def fprice(amnt=1, cost=1000):
#     final_price = amnt * cost
#     return final_price


# fp = fprice(5)
# print(fp)

# addten = lambda n: n+10

# print(addten(5))

# r = subt(10)

# def subt(x):
#     x -= 10
#     return x

# print(r)

# def prt2(message):
#     print(message)
#     print(message)

# prt2("Good morning")

def powered(x, y):
    r = x**y
    return r

n1 = input("Number: ")
n2 = input("Power: ")

result = powered(n1, n2)
print(result)