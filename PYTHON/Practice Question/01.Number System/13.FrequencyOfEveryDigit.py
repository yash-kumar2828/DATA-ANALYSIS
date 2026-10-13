# Find the Frequency of Every Digit

num = int(input("Enter your positive number."))


for i in range(10):
    print(i, "→", str(num).count(str(i)))