n = int(input("Enter the number:"))
reverse = 0
while n != 0:
    remainder = int(n % 10)
    reverse = (reverse * 10) + remainder
    n = n // 10
print(reverse)
