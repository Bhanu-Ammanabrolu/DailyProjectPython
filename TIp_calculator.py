print("Welcome to the tip calculator. ")

total_bill = float(input("What was the total bill? $"))

tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

bill_with_percentage = tip_percentage / 100 * total_bill + total_bill

people = int(input("How many people to split the bill? "))

split_bill = round((bill_with_percentage / people), 2)

print(f"Each person should pay: ${split_bill}")
