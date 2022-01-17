num = int(input("Enter the number : "))

prime = True

for i in range (2 , num):
    if num%i==0:
        prime = False
        break
    else:
        prime = True

if prime==False:
    print("NOT a prime number")
else:
    print("Prime number")