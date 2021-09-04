print("Pizza order")
size=input("Enter the size of the pizza S,M,L ? \n ")
toppings=input("Do you need toppings  Y, N ? \n  ")
cheese=input("Do you need cheese? Y,N \n ")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
else:
    bill+=25
if toppings=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=5
if cheese=="Y":
    bill+=10
print(f"Your total bill is {bill} ")