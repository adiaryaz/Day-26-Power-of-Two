def power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

num = int(input("Enter a number: "))

if power_of_two(num):
    print(f"{num} is a power of two.")
else:
    print(f"{num} is not a power of two.")