# Author: Ediel Lopez
# Date: 6/22/2019
# Course: MIT 6.00.1x - Week 2 Problem 1 - Paying Debt Off in a Year
# Description: Write a program to calculate the credit card balance after one year if
# a person only pays the minimum monthly payment required by the credit card company each month.

# ============ VARIABLES ===============
balance = 42

# You have an annual interest rate of 20%, which is split into 12 months
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0

# A minimum of 0.04% of the balance is due every month.
monthlyPaymentRate = 0.04
# =====================================

# =============== MAIN FUNCTION ==================
for index in range(12): # 12 months in a year
    # The minimum monthly payment of n% is required
    minMonthlyPayment = balance * monthlyPaymentRate

    # Subtract the minimum monthly payment from the balance
    balance = balance - minMonthlyPayment
    interest = monthlyInterestRate * balance

    # Update the Balance. Adding the Interest
    balance = round(balance + interest, 2)

    print("Month " + str(index+1) + " remaining balance: " + str(balance))

# Print the final balance after a year.
print("Remaining balance: " + str(balance))
# =================================================
