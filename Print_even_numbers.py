#Print Even numbers

n=int(input("Enter a number:"))
print(n)
even=int(input("Enter the number of even numbers you wish to print:"))
print(even)
for i in range(n+1,n+even+1):
  if(i%2==0):
    print(i)