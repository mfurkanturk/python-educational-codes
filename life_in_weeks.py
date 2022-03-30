age = input("What is your current age?")

age = int(age)
age_in_days = age*365
age_in_weeks = age*52
age_in_months = age*12

x=90*365
y=90*52
z=90*12

days_remaining = x- age_in_days
weeks_remaining= y-age_in_weeks
months_remaining= z - age_in_months

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")


