def mul(x, y):
    mul= int(p) * int(q)
    print(mul)


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
mul = int(a) * int(b)

print(mul)