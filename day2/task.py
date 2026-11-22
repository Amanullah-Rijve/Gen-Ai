# # task 1
# num = int(input("Enter a number: "))

# if num %2 ==0:
#     print(f"Number {num} is Even")
# else:
#     print(f"Number {num} is odd")

# # task 2
# total = 0


# for i in range(1,11):
#     total += i

# print(f"Sum: {total}")

# # task 3
# total = 0

# for i in range(1,21):
#     if i % 2==0:
#         total +=i

# print(total)

# # task 4
# num = int(input("Enter a number: "))

# for i in range(1,11):
#     print(f"{num} x {i}: {num * i}")

# # # task 5
# for i in range(1,16):
#     if i ==5:
#         continue
#     elif i ==10:
#         continue
#     elif i ==15:
#         continue
#     else:
#         print(i)
for n in range(1, 8):
    print(f"checking n = {n}, n % 3 = {n % 3}")
    if n % 3 == 1:
        print("  -> condition true, continue runs, skipping print")
        continue
    print(f"  -> printed {n}")