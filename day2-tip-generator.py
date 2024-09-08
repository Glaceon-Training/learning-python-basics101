print("Welcome to tip calculator!")

bill = float(input("What was the total bill? $"))
percent_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_pays = int(input("How many people to split the bill? "))
bill_and_tip = bill + (bill * (percent_tip / 100))
split_bill = round((bill_and_tip / people_pays), 2)

print(f"Each person should pay: ${split_bill}")
