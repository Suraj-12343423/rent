rent = float(input("Enter the rent amount: "))
food = float(input("Enter the total food ordered for snacking: "))

electricity_units = float(input("Enter electricity units used: "))
charge_per_unit = float(input("Enter charge per unit: "))

persons = int(input("Enter number of persons: "))

# Electricity bill calculation
electricity_bill = electricity_units * charge_per_unit

# Total bill
total_amount = rent + food + electricity_bill

# Split per person
per_person = total_amount / persons

print("\n-------------------------")
print("Total Bill: ", total_amount)
print("Each person should pay: ", per_person)
print("-------------------------")
