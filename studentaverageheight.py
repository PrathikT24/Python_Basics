studentheights=input("Enter heights of student \n ").split()
for n in range(0, len(studentheights)):
    studentheights[n]= int(studentheights[n])
print(studentheights)
totalheight=0
for height in studentheights:
    totalheight+=height
print(totalheight)
noofstudents=0
for student in studentheights:
    noofstudents+=1
print(noofstudents)
avg=round(totalheight/noofstudents)
print(avg)

