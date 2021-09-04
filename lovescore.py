boy=input(" Enter boy's name ")
girl=input("Enter girl's name ")
together=boy+girl
relation=together.lower()

t=relation.count("t")
r=relation.count("r")
u=relation.count("u")
e=relation.count("e")

true=t+r+u+e

l=relation.count("l")
o=relation.count("o")
v=relation.count("v")
e=relation.count("e")

love=l+o+v+e

lovescore= int(str(true+love))

if lovescore > 10:
    print("true love")
else:
    print("Friendship")
