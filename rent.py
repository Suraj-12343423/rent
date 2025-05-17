## Input we need from the user
# Rent
# Total food ordered for snacking
# Electricity bill
# charge per unit

## Output 
# total amount to be paid

rent = float(input("Enter the rent amount: "))
food = float(input("Enter the total food ordered for snacking: "))
electricity = float(input("Enter the electricity bill: "))
charge_per_unit = float(input("Enter the charge per unit: "))
person = int(input("Enter the number of persons: "))
total_amount = rent + food + electricity + charge_per_unit
total = total_amount / person
print("The total amount to be paid is: ", total)