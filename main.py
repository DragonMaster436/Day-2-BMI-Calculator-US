# 🚨 Don't change the code below 👇
height = input("enter your height in inch: ")
weight = input("enter your weight in lb: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_height = float(height) ** 2
new_weight = float(weight)
total = round(new_weight / new_height * 703 ,2)

if total <= 18.4:
    print(f"Your BMI is {total}, you are underweight.")
elif total < 25:
    print(f"Your BMI is {total}, you have a normal weight.")
elif total < 30:
    print(f"Your BMI is {total}, you are slightly overweight.")
elif total < 35:
    print(f"Your BMI is {total}, you are obese.")
else:
    print(f"Your BMI is {total}, you are clinically obese.")


# my info is 69 inch and 140 lb output should be 20.7 or something close
# this code is broken and I would like to fix it one day I think I'm running into float problems
# I fixed this code when I moved the * 703 from the new_height variable to the total veriable
