# Kirill M11P1 10/16/2026

# Define function
def compute(quantity, price, discount_rate):
# Finding total value, discount value and final price
    total = quantity * price
    discount = total * (discount_rate / 100)
    final_price = total - discount
    return total, discount, final_price

# Asking to enter quantity, price, and discount rate
quantity = int(input("Enter quantity amount: "))
price = float(input("Enter price amount: "))
discount_rate = float(input("Enter discount rate: "))

# Calling for function compute
total, discount, final_price = compute(quantity, price, discount_rate)

# Print final statement
print(f"Quantity: {quantity}")
print(f"Price: ${price:,.2f}")
print(f"Discount rate: %{discount_rate}")
print(f"Discount amount: ${discount}")
print(f"Discount price: ${final_price}")