
# # # # # # Python: Real-World Challenge Set
# # # # # #                 Level 1 — Online Shopping
# # # # # #      Medium
# # # # # #  Problem 1: Shopping Cart Bill Calculator
# # # # # # An online store has these product prices:

# # # # # # prices = [499, 1200, 200, 799, -100, 2500, 350]

# # # # # # # Requirements:
# # # # # # # - Use a for loop to process every price.
# # # # # # # - If the price is 0, skip it using continue.
# # # # # # # - If the price is negative, stop processing using break.
# # # # # # # - Otherwise, add the price to the total bill.
# # # # # # # - Print the total bill and the number of valid products processed.
# # # # # # # Challenge: Don't count skipped or invalid products.
# # # # # # total_bill = 0
# # # # # # count =0
# # # # # # for price in prices:
# # # # # #     if price <=0:
# # # # # #         continue

# # # # # #     total_bill += price
# # # # # #     count += 1
# # # # # # print(total_bill)
# # # # # # print(f"total count:{count}")


# # # # # # Level 2 — Banking System

# # # # # # Problem 2: ATM Transaction Processor

# # # # # # transactions = [500, 1000, -200, 0, 1500, 2000, 300]
# # # # # # balance = 5000
# # # # # # with_draw =int(input("Enter the amount to draw:"))
# # # # # # final_balance=0

# # # # # # Requirements:
# # # # # # - Positive amount → withdraw it if sufficient balance exists.
# # # # # # - Zero amount → skip using continue.
# # # # # # - Negative amount → treat it as invalid and stop using break.
# # # # # # - If withdrawal exceeds the balance, print "Insufficient balance" and continue to the next transaction.
# # # # # # - Print the final balance and successful withdrawal count.
# # # # # # Challenge: Update the balance only after a successful withdrawal.


# # # # # transactions = [500, 1000, -200, 0, 1500, 2000, 300]
# # # # # balance = 5000
# # # # # count = 0

# # # # # for transaction in transactions:

# # # # #     if transaction == 0:
# # # # #         continue

# # # # #     if transaction < 0:
# # # # #         print("Invalid transaction")
# # # # #         break   

# # # # #     if transaction > balance:
# # # # #         print("Insufficient balance")
# # # # #         continue
    

# # # # #     balance = balance - transaction
# # # # #     count += 1

# # # # # print("Final balance:", balance)
# # # # # print("Successful withdrawals:", count)

# # # #         # Level 3 — Software Logs
# # # # # Problem 3: Application Log Analyzer

# # # # logs = [
# # # #     "INFO: Server started",
# # # #     "INFO: User logged in",
# # # #     "WARNING: Memory usage high",
# # # #     "",
# # # #     "ERROR: Database failed",
# # # #     "INFO: Retry started",
# # # #     "ERROR: Connection lost",
# # # #     "STOP"
# # # # ]


# # # # # Requirements:
# # # # # - Empty strings → skip using continue.
# # # # # - Count INFO, WARNING, and ERROR messages separately.
# # # # # - When the log equals "STOP", stop processing using break.
# # # # # - Print the count of each log type.
# # # # # Challenge: Use startswith() to identify the log categories.

# # # # info_count = 0
# # # # warning_count = 0
# # # # error_count = 0

# # # # for log in logs:
# # # #     if log =="":
# # # #         continue
    
# # # #     if (log =="STOP"):
# # # #         break

# # # #     if log.startswith("INFO"):
# # # #         info_count += 1
# # # #     elif log.startswith("WARNING"):
# # # #         warning_count += 1
# # # #     elif log.startswith("ERROR"):
# # # #         error_count += 1
# # # # print("INFO:", info_count)
# # # # print("WARNING:", warning_count)
# # # # print("ERROR:", error_count)

# # # emails = [
# # #     "admin@gmail.com",
# # #     "spam@example.com",
# # #     "",
# # #     "user@gmail.com",
# # #     "STOP",
# # #     "boss@gmail.com"
# # # ]

# # # # Requirements:
# # # # 1. Skip empty strings using continue.
# # # # 2. Stop when you find "STOP" using break.
# # # # 3. Count emails that end with "gmail.com" using .endswith().
# # # # 4. Print the final Gmail count outside the loop.
# # # gmail_count =0

# # # for email in emails:
# # #     if email =="":
# # #         continue
# # #     if email== "STOP":
# # #         break
# # #     if email.endswith("gmail.com"):
# # #         gmail_count +=1

# # # final_gmail =gmail_count
# # # print(final_gmail)



# # Level 4 — HR System
# # Very hard
# # Problem 4: Employee Attendance Report

# # attendance = [
# #     ("Ravi", 8),
# #     ("Priya", 0),
# #     ("Kiran", 7),
# #     ("Anu", -1),
# #     ("Rahul", 9),
# #     ("Sita", 6)
# # ]

# # # Each tuple contains an employee's name and hours worked.
# # # Requirements:
# # # - 0 hours → employee is absent; skip using continue.
# # # - Negative hours → invalid attendance data; stop using break.
# # # - Hours of 8 or more → print "Full day".
# # # - Hours below 8 but above 0 → print "Short day".
# # # - Count full days, short days, and absent employees encountered before stopping.
# # # Challenge: Print a final HR report with all three counts.
# # full_day =0
# # short_day =0
# # absent =0
# # for name,hours in attendance:
# #     if (hours == 0):
        
# #         print("employee is absent")
# #         absent +=1
# #         continue
# #     elif hours <=0 :
# #         print("Invalid attendance")  
# #         break;
# #     elif hours >=8:
# #         print("full day")
# #         full_day +=1
# #     elif 0 <hours< 8:
# #         print("short day")
# #         short_day +=1
# # print(full_day)
# # print(short_day)
# # print(absent)
# # all_three = full_day+short_day



# attendance = [
#     ("Ravi", 8),
#     ("Priya", 0),
#     ("Kiran", 7),
#     ("Anu", -1),
#     ("Rahul", 9),
#     ("Sita", 6)
# ]

# full_day = 0
# short_day = 0
# absent = 0

# for name, hours in attendance:
#     if hours < 0:
#         print("Invalid attendance:", name)
#         break

#     if hours == 0:
#         print(name, "is absent")
#         absent += 1
#         continue

#     if hours >= 8:
#         print(name, "Full day")
#         full_day += 1
#     elif hours > 0 and hours < 8:
#         print(name, "Short day")
#         short_day += 1

# print("\n--- HR Report ---")
# print("Full days:", full_day)
# print("Short days:", short_day)
# print("Absent employees:", absent)


# Level 5 — Fraud Detection

# Problem 5: Suspicious Transaction Detector

transactions = [
    500, 700, 12000, 300, 15000,
    0, 800, 25000, 400
]


# Requirements:
# - Ignore zero-value transactions using continue.
# - If a transaction is greater than ₹10,000, mark it suspicious.
# - Stop processing when you encounter a transaction greater than ₹20,000 using break.
# - Count valid transactions processed and suspicious transactions found.
# - Calculate the total value of valid transactions processed before stopping.
# Challenge: Make sure the transaction that triggers break is not included in your total.
valid_transcations =0
suspicious_transcations =0
total =0
for transcation in transactions:
    if transcation ==0:
        continue
    if transcation >20000:
            break
    if transcation >10000:
        print("Suspicious:",transcation)
        suspicious_transcations +=1
    valid_transcations +=1
    total +=transcation
    
print(valid_transcations)
print(suspicious_transcations)
print(total)