num = int(input("enter a number"))

print(f"the factors of {num}: ")
for i in range (1, num+1):
    if num%i ==0:
        print(i)