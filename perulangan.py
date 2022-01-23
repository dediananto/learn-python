# 1. for-in (list | string)
# array = [1,2,3,4,5]
# for angka in array:
#     print(angka)

# for huruf in "Hello Python":
#     print(huruf)

# 2. for-in-range(x)
# for angka in range(3):
#     print(angka)

# 3. for-in-range(x, y)
# for angka in range(10, 15):
#     print(angka)

# 4. while
# angka = 1
# while angka<10:
#     print(angka)
#     angka += 1

# 5 while-break
# angka = 1
# while angka<10:
#     print(angka)
#     angka += 1
#     if angka == 5:
#         break
# print('--')

# 6 while-continue
angka = 0
while angka<10:
    angka += 1
    if angka == 5:
        continue
    print(angka)