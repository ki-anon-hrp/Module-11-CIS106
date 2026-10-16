# Kirill M11P5 10/16/2026

# Define function
def compute(quantity, unit_price):
# Calculate total and tax
    global tax, total
    total = quantity * unit_price
    tax = total * 0.07

# Entering quantity and unit price
quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))

# Calling for function compute
compute(quantity, unit_price)

# Printing final statement
print(f"Total: ${total:,.2f}")
print(f"Tax: ${tax:,.2f}")