print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill: ₹"))
people = int(input("How many people you want to split this with?:"))
percent = int(input("What percentage of tip would you like to give? 10, 12 or 15? "))
percent_pay = (total_bill*percent)/100
final_pay = (total_bill + percent_pay)/people
print("Everyone should pay ₹"+str(final_pay))