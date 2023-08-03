# Function to calculate the Rule of 72
def rule_of_72(capital, interest_rate):
    years = 0
    while capital < 2 * capital:
        capital *= (1 + interest_rate / 100)
        years += 1
    return years

# User input
capital_investment = float(input("Enter the capital investment: "))
interest_rate = float(input("Enter the interest rate (in percentage): "))

# Calculate and print the result
years_to_double = rule_of_72(capital_investment, interest_rate)
print("It will take approximately", years_to_double, "years to double your investment.")

# Pause for user to view output
input("Press Enter to exit...")