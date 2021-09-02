year=int(input("Enter a year \n "))
if year%4==0:
    print("Leap year \n ")
elif year%100==0 and year%400==0:
    print("Leap year \n ")
else:
    print("Not a leap year \n ")

