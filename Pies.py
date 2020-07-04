pie_list =[ 
    "Apple pie",
    "Cherry pie",
    "Banana pie",
    "Coconut pie",
    "Strawberry pie",
    "Key Lime pie",
]
pie_cart = []

print("Welcome to the House of Pies! These are our pies:")
print("-"*10)
for i in range(len(pie_list)):
    print("[" + str(i) + "]" + pie_list[i])

answer = "y"
while answer =="y":

    selected = input("Which pie would you like to order? ")
    pie_cart.append(pie_list[int(selected)])
    print("Great! We'll have " + pie_list[int(selected)] + " right out for you")

    answer = input("Would you like to order another pie? y/n" ).lower()

print("Here is your order sugah ...")
for pie in pie_cart:
    print(pie)