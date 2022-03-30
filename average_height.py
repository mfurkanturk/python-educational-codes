# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sumn=0
for n in student_heights:
    sumn += n
leng=0
for n in student_heights:
    leng +=1
avg= round(sumn/leng)

print(avg)
