#Exercise 1

name = str(input("What is your full name? "))
address = str(input("What is your home address? "))
phone_number = str(input("What is your phone number? "))
college_major = str(input("What is your college major? "))

#Exercise 2

print("Name =" + name)
print("Address = " + address)
print("Phone number = " + phone_number)
print("College major = " + college_major)

#Exercise 3

revenue = (int(input("What is the total revenue of the past year? ")))
profit = revenue * 0.23
print("Projected profit is: " + (str("$")) + (str(profit)))

#Exercise 3

square_footage = int(input("What is the square footage? "))
acres = square_footage / 43560

print("This is equal to " + str(acres) + " acres. ")

#Exercise 4

item_1 = int(input("What is the cost of the 1st item? "))
item_2 = int(input("What is the cost of the 2nd item? "))
item_3 = int(input("What is the cost of the 3rd item? "))
item_4 = int(input("What is the cost of the 4th item? "))
item_5 = int(input("What is the cost of the 5th item? "))

total_purchase = (item_1 + item_2 + item_3 + item_4 + item_5) * 1.07

print("Total purchase cost = " + str(total_purchase) + ". ")

#Exercise 5

speed = int(input("What is your speed in MPH? "))
distance_after_six_hours = (speed * 6)
distance_after_ten_hours = (speed * 10)
distance_after_fifteen_hours = (speed * 15)

print("Your distance after 6 hours will be: " + str(distance_after_six_hours))
print("Your distance after 10 hours will be: " + str(distance_after_ten_hours))
print("Your distance after 15 hours will be: " + str(distance_after_fifteen_hours))

#Exercise 6

initial_cost = int(input("What is the pre-tax cost of the items? "))
county_sales_tax = 1.025
state_sales_tax = 1.05
final_cost = initial_cost * county_sales_tax * state_sales_tax
print("Final cost is $" + str(final_cost) + ". ")

#Exercise 7

miles_driven = int(input("How many miles have you driven? "))
gallons_used = int(input("How many gallons of gas have you used? "))
MPG = miles_driven / gallons_used
print("Your MPG is " + str(MPG) + ".")

#Exercise 8

subtotal = int(input("What is the subtotal? "))
tax = 1.07
tip = 1.18
total = subtotal * tax * tip
print("Total = " + str(total) + ".")

#Exercise 9

farenheit = int(input("What is the temperature in farenheit? "))
celsius = farenheit * (9/5) + 32
print("In celcius, this is: " + str(celsius) + ".")

#Exercise 10

sugar_for_48 = 1.5 #cups
butter_for_48 = 1 #cups
flour_for_48 = 2.75 #cups

sugar_for_1 = sugar_for_48 / 48
butter_for_1 = butter_for_48 / 48
flour_for_1 = flour_for_48 / 48

number_of_cookies = int(input("How many cookies? "))
sugar_for_number_of_cookies = sugar_for_1 * number_of_cookies
butter_for_number_of_cookies = butter_for_1 * number_of_cookies
flour_for_number_of_cookies = flour_for_1 * number_of_cookies

print("Cups of sugar needed: " + str(sugar_for_number_of_cookies))
print("Cups of butter needed: " + str(butter_for_number_of_cookies))
print("Cups of flour needed: " + str(flour_for_number_of_cookies))

#Exercise 11

lions = 8
tigers = 12
number_of_cats = 20
lions_percentage = lions / number_of_cats
tigers_percentage = tigers / number_of_cats

print("% of tigers: " + str(tigers_percentage))
print("% of lions: " + str(lions_percentage))

#Exercise 12

Joes_initial_purchase = 2000
initial_stock_price = 40
final_stock_price = 42.75
pre_commission_earnings = (Joes_initial_purchase * final_stock_price) - (Joes_initial_purchase * initial_stock_price)
post_commission_earnings = pre_commission_earnings / 1.03

print("Joe's final earnings are: $" + str(post_commission_earnings))

#Exercise 13

length_of_row = int(input("What is the length of the row? "))
end_post_assembly = int(input("What is the length of the end post assembly in feet? "))
space_between_vines = int(input("What is the distance between the vines in feet? "))

number_of_grapevines = (length_of_row - (2 * end_post_assembly)) / space_between_vines
print("The number of grapevines possible is: " + str(number_of_grapevines))

#Exercise 14

principal_amount = int(input("What is principal amount?: "))
interest_rate = int(input("What is the interest rate? "))
interest_compound_per_year = int(input("How many times does the interest compound per year? "))
number_of_years = int(input("How many years have passed? "))
compound_interest = int((principal_amount * (1 + (interest_rate / interest_compound_per_year)) ^ (interest_compound_per_year * number_of_years)))

print("After " + str(number_of_years) + " years, your principal plus interest would be $: " + str(compound_interest))