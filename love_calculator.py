print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1= name1.lower()
lower_name2= name2.lower()

first_dig= str(lower_name1.count("t")+lower_name1.count("r")+lower_name1.count("u")+lower_name1.count("e")+lower_name2.count("t")+lower_name2.count("r")+lower_name2.count("u")+lower_name2.count("e"))

sec_dig= str(lower_name1.count("l")+lower_name1.count("o")+lower_name1.count("v")+lower_name1.count("e")+lower_name2.count("l")+lower_name2.count("o")+lower_name2.count("v")+lower_name2.count("e"))

love_score= int(first_dig+sec_dig)
if love_score<10 or love_score>90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40<love_score<50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
