print("Welcome to tip calculator!")

bill=float(input("enter the bill amount: $"))
tip=int(input("enter the % of tip: 10 15 20"))
people=int(input("enter the number of people to split bill with:"))
print(bill)
print(tip)
print(people)

total_bill = tip/100 * bill + bill
print(total_bill)