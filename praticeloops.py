
# Python: Real-World Challenge Set
#                 Level 1 — Online Shopping
#      Medium
#  Problem 1: Shopping Cart Bill Calculator
# An online store has these product prices:

# prices = [499, 1200, 200, 799, -100, 2500, 350]

# # Requirements:
# # - Use a for loop to process every price.
# # - If the price is 0, skip it using continue.
# # - If the price is negative, stop processing using break.
# # - Otherwise, add the price to the total bill.
# # - Print the total bill and the number of valid products processed.
# # Challenge: Don't count skipped or invalid products.
# total_bill = 0
# count =0
# for price in prices:
#     if price <=0:
#         continue

#     total_bill += price
#     count += 1
# print(total_bill)
# print(f"total count:{count}")


# Level 2 — Banking System

# Problem 2: ATM Transaction Processor

# transactions = [500, 1000, -200, 0, 1500, 2000, 300]
# balance = 5000
# with_draw =int(input("Enter the amount to draw:"))
# final_balance=0

# Requirements:
# - Positive amount → withdraw it if sufficient balance exists.
# - Zero amount → skip using continue.
# - Negative amount → treat it as invalid and stop using break.
# - If withdrawal exceeds the balance, print "Insufficient balance" and continue to the next transaction.
# - Print the final balance and successful withdrawal count.
# Challenge: Update the balance only after a successful withdrawal.


transactions = [500, 1000, -200, 0, 1500, 2000, 300]
balance = 5000
count = 0

for transaction in transactions:

    if transaction == 0:
        continue

    if transaction < 0:
        print("Invalid transaction")
        break   

    if transaction > balance:
        print("Insufficient balance")
        continue
    

    balance = balance - transaction
    count += 1

print("Final balance:", balance)
print("Successful withdrawals:", count)

        
