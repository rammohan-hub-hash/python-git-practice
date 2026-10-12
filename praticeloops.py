
# Python: Real-World Challenge Set
#                 Level 1 — Online Shopping
#      Medium
#  Problem 1: Shopping Cart Bill Calculator
# An online store has these product prices:

prices = [499, 1200, 200, 799, -100, 2500, 350]

# Requirements:
# - Use a for loop to process every price.
# - If the price is 0, skip it using continue.
# - If the price is negative, stop processing using break.
# - Otherwise, add the price to the total bill.
# - Print the total bill and the number of valid products processed.
# Challenge: Don't count skipped or invalid products.
total_bill = 0
count =0
for price in prices:
    if price <=0:
        continue

    total_bill += price
    count += 1
print(total_bill)
print(f"total count:{count}")


