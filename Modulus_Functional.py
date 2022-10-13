def modulus(x,y):
    modulus= int(p)%int(q)
    print(modulus)


print("first input")
a = input()
if int(a) < 0:
    print("not valid")
    exit()
else:
    print("first number is " + a)
print("second input")
b = input()
if int(b) < 0:
    print("not valid ")
    exit()
else:
    print("second number is " + b)
    print("result")
modulus = int(a) % int(b)

print(modulus)