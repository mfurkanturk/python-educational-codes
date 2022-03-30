# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
x=0
counter=0
for n in student_scores:
   
    if student_scores[x]>= n:
        highest = student_scores[x]
    else :
        x = counter
        highest = student_scores[x]
    counter +=1
    
print(f"The highest score in the class is: {highest}")



