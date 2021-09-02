studentscore=input("Enter the scores of student \n ").split()
for x in range(0, len(studentscore)):
    studentscore[x]=int(studentscore[x])
print(studentscore)

highscore=0
for score in studentscore:
    if score > highscore:
        highscore=score
print(f"Highest score is: {highscore}")

