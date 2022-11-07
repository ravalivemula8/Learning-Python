#Create a python program to print odd numbers

def print_odd_numbers(number, odd_number_count):
 for i in range(5, 9+odd_number_count):
    if i % 2 != 0:
        print(i)


number = int(input("Enter a number: "))

odd_number_count = int(input("How many odd numbers you want to print: "))

print_odd_numbers(number, odd_number_count)