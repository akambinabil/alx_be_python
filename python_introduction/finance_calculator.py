montly_income = input("Enter your montly income: ")
montly_expenses = input("Enter your montly expenses: ")

montly_savings = float(montly_income) - float(montly_expenses)

projected_savings = montly_savings * 12 + (montly_savings * 12 * 0.05)

print("Your montly saving are ", montly_savings)
print("Projected savings after one year, with interest, is: ", projected_savings, ".")
