# Author: Ediel Lopez
# Date: 6/30/2019
# Course: MIT 6.00.1x - Week 2 Problem 3 - Paying Debt Off in a Year Using Bisection Search
# Description: Write a program that uses a Lower and Upper Bound and Bisection Search to find the smallest
# monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year.
# IMPORTANT NOTE: I solved this problem after the deadline.

# ============ VARIABLES ==============
original = balance = unpaidBalance = 187850
annualInterestRate = 0.22
monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12.0                                   # Initial Monthly Payment Lower Bound
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0 # Initial Monthly Payment Upper Bound
fixedMonthlyPayment = 0.0
# =====================================

# =============== MAIN FUNCTION ==================
# We want to pay off the entire balance using fixed monthly payments, so we keep
# iterating until we find that value that is correct or a few cents off in either direction.
while (not(balance > -0.1 and balance < 0.1)):
     fixedMonthlyPayment = (lowerBound + upperBound) / 2.0            # Midpoint
     # print("Fixed Monthly Payment = " + str(fixedMonthlyPayment))

     balance = original      # Reset the balance
     for index in range(12): # Check to see if we can actually pay off the debt with the fixed monthly payment.
          unpaidBalance = balance - fixedMonthlyPayment
          balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
     # print("The Remaining Balance is = " + str(balance))

     if (balance >= 0.1): # If the balance is greater than 10 cents, make the fixed monthly payment the new low.
          lowerBound = fixedMonthlyPayment
     elif (balance <= -0.1): # If the balance is less than 10 cents, make the fixed monthly payment the new high.
          upperBound = fixedMonthlyPayment

print("Lowest Payment: ", round(fixedMonthlyPayment,2))
# =================================================

# ============ Test Cases ==============
# Debt = 320000
# AnnualInterestRate = 0.2
# Solution = 29157.09

# Debt = 999999
# AnnualInterestRate = 0.18
# Solution = 90325.03

# Debt = 187850
# AnnualInterestRate = 0.22
# Solution = 17265.17
# ======================================
