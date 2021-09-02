totalbill=int(input("Enter the amount \n "))
tip=int(input("Enter the tip percentage \n "))
amount=(totalbill*tip)/100
print(round(amount))
sharing=int(input("Shared among? \n "))
pay=amount//sharing
print(f"Each person should pay £{round(pay)}")