# Q1. Voter eligibility check (Election Commission)
# Read a person's age and citizenship (Indian / other). Print Eligible to vote only if age is 18 or above and
# citizenship is Indian. Otherwise print the exact reason.
# • Test: 17, Indian → Not eligible: under 18
# • Test: 25, Nepali → Not eligible: not an Indian citizen

# age = int(input("Enter a age:"))
# citizen =input("Enter the Citizenship:")

# if age >=18 and citizen =="India" :
#     print(f"Age is {age} and Eligible to vote in {citizen}")
# else:
#     print(f"They are {citizen} and can't able to vote")


# Q2. ATM withdrawal
# Read account balance and withdrawal amount. Allow the withdrawal only if the amount is a multiple of 100,
# at most ₹10,000 per transaction, and not more than the balance. Print the new balance or the reason for
# failure.

account_balance =100000
withdraw_amount =int(input("Enter the amount to withdraw:"))



if withdraw_amount % 100 != 0:
       print(f"Failure: Amount must be a multiple of 100")
elif withdraw_amount > 10000:
    print(f"Failure: Maximum withdrawal limit is 10000")
elif withdraw_amount > account_balance:
    print(f"Failure: Insufficient balance")

elif withdraw_amount <= 0:
    print(f"Failure: Enter a valid positive amount")
else:
    new_balance = account_balance - withdraw_amount
    print("Withdrawal successful!")
    print(f"Remaining balance: {new_balance}")



