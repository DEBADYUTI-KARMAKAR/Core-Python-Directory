# Digit of a number
num = int(input("Enter a number"))
while num>0:
    dig = int(num % 10)
    print(dig)
    num = int(num / 10)

print("-------")

for i in range(1,5):
    print(i)
