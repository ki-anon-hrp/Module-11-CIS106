# Kirill M11P3 10/16/2026

# Define function
def compute(sales):
# Comparing sales with specific value and giving depended comission procent
    if sales > 100000:
        commision = 0.10
    else: 
        commision = 0.05 

# Finding commision 
    commision_calculation = commision * sales

# Finding next year target
    next_year = 0.05 * sales 

    return commision, commision_calculation, next_year

# Entering last name and sales
last_name = input("Enter last name of salesperson: ")
sales = int(input("Enter a sales: "))

# Calling for function compute
commision, commision_calculation, next_year = compute(sales)

# Printing final statment
print(f"Salesperson last name: {last_name}")
print(f"Commision: ${commision_calculation:,.2f}")
print(f"Next year target: ${next_year:,.2f}")