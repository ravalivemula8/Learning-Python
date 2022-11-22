#Program should accept
x = input('what is the string')
y=len(x)

#find out the slice
x1=x[1:-1]
print(x1)

#Find out the slice of the string after removing the 2 characters
x2=x[2:]
print(x2)

#Removing last two characters
x3=x[:-3]
print(x3)

#Slicing in between
x4=x[int(len(x)//2):]
x5=x[int(len(x)//2)]
print(x5,x4)


