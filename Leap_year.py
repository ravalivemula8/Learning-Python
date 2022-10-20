#Create a Leap Year check program
Year = int(input("Enter an year"))
#i=Year%400
#print(i)
if Year%400 == 0:
    print("checking if 2000 is a leap year")
    print(Year , "is a loop year as it's divisible by 400")
if Year%100 == 0:
    if Year != 400 == 0:
        print("checking if 2100 is a leap year")
        print(Year , "is not a leap year as it's divisible by 100 but not by 400")
if Year%4 == 0 and Year != 100 or Year != 400:
    print(Year , "is a leap year as it's divisible by 4 but not by 100 or 400")


