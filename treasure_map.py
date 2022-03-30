row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


c = int(position[0])
r = int(position[1])

if r== 1:
    if c==1:
        row1[0]="X"
    elif c==2:
        row1[1]="X"
    elif c==3:
        row1[2]="X"

elif r== 2:
    if c==1:
        row2[0]=  "X"
    elif c==2:
        row2[1]=  "X"
    elif c==3:
        row2[2]=  "X"

else:
    if c==1:
        row3[0]=  "X"
    elif c==2:
        row3[1]=  "X"
    elif c==3:
        row3[2]=  "X"

print(f"{row1}\n{row2}\n{row3}")
