# Author: Ediel Lopez
# Date: 6/29/2019
# Course: MIT 6.00.1x - Week 2 Problem 2 - Paying Debt Off in a Year
# Description: Write a program to calculate the credit card balance after one year if
# a person only pays the minimum monthly payment required by the credit card company each month.
# IMPORTANT NOTE: I solved this problem after the deadline. Major thank you to Nicholas Perez-Aguilar
# for helping me debug my code.

# ============ VARIABLES ==============
original = outstandingBalance = unpaidBalance = 3741
annualInterestRate = 0.04
monthlyInterestRate = annualInterestRate / 12.0
minimumFixedMonthlyPayment = 10
# =====================================

# =============== MAIN FUNCTION ==================
# We want to pay off the entire balance using minimum fixed monthly payments, so we keep
# iterating until we find that value.
while (outstandingBalance > 0):
     for month in range(12): # Check to see if we can actually pay off the debt with the minimumFixedMonthlyPayment.
          unpaidBalance = outstandingBalance - minimumFixedMonthlyPayment
          outstandingBalance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
    # If the current minimumFixedMonthlyPayment doesn't pay off the debt, increment it by 10 and run it again.
     if (outstandingBalance > 0):
          minimumFixedMonthlyPayment += 10
          outstandingBalance = original # Reset to the original oustanding balance
     else:  # Congrats! You've found the minimumFixedMonthlyPayment that will help you pay your debt in 12 months.
          break

print("Lowest Payment: ", minimumFixedMonthlyPayment)
# =================================================


# ============ Test Cases ==============
# Debt = 4773
# AnnualInterestRate = 0.2
# Solution = 440

# Debt = 529
# AnnualInterestRate = 0.18
# Solution = 50

# Debt = 3741
# AnnualInterestRate = 0.04
# Solution = 320
# ======================================
