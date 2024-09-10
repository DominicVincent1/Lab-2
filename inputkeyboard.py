print("Exercise one:")

name = str(input("What is your full name? "))
address = str(input("What is your home address? "))
phone_number = str(input("What is your phone number? "))
college_major = str(input("What is your college major? "))

print("Name =" + name)
print("Address = " + address)
print("Phone number = " + phone_number)
print("College major = " + college_major)

revenue = (int(input("What is the total revenue of the past year? ")))
profit = revenue * 0.23

print("Projected profit is: " + (str("$")) + (str(profit)))

square_footage = int(input("What is the square footage? "))
acres = square_footage / 43560

print("This is equal to " + str(acres) + " acres. ")

item_1 = int(input("What is the cost of the 1st item? "))
item_2 = int(input("What is the cost of the 2nd item? "))
item_3 = int(input("What is the cost of the 3rd item? "))
item_4 = int(input("What is the cost of the 4th item? "))
item_5 = int(input("What is the cost of the 5th item? "))

total_purchase = (item_1 + item_2 + item_3 + item_4 + item_5) * 1.07

print("Total purchase cost = " + str(total_purchase) + ". ")

