#name= "Luis"
#Country= "Mexico"
#Age= 37
#hourly_wage = 1000
#Satisfied = True
#daily_wage = hourly_wage * 8

#print ("Your name is " + name)
#print("you live in " + Country )
#print("You are " + str(Age) + " years old")
#print("You make " + str(daily_wage) + " per day")
#print("Are you satisfied with your current wage? " + str(Satisfied))

# 1.
x = 5
y = 10
if 2 * x > 10:
    print("Question 1 works!")
else:
    print("oooo needs some work")
# ooo needs some work

# 2.
x = 34
y = 10
if len("supercalifragilisticespiralidocious") < x:
    print("Question 2 works!")
else:
    print("Still missing out")
#question 2 works

# 3.
x = 2
y = 5
if (x ** 3 >= y) and (y ** 2 < 26):
    print("GOT QUESTION 3!")
else:
    print("Oh good you can count")
#Got question 3!

# 4.
name = "Dan"
group_one = ["Greg", "Tony", "Susan"]
group_two = ["Gerald", "Paul", "Ryder"]
group_three = ["Carla", "Dan", "Jefferson"]

if name in group_one:
    print(name + " is in the first group")
elif name in group_two:
    print(name + " is in group two")
elif name in group_three:
    print(name + " is in group three")
else:
    print(name + " does not have a group")
#Dan is in group three


# 5.
height = 66
age = 22
adult_permission = True

if (height > 70) and (age >= 18):
    print("Can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("Can ride light roller coasters")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    print("Can ride bumper cars")
else:
    print("Stick to lazy river")
#Can ride bumper cars
