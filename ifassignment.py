# # # Q1. Voter eligibility check (Election Commission)
# # # Read a person's age and citizenship (Indian / other). Print Eligible to vote only if age is 18 or above and
# # # citizenship is Indian. Otherwise print the exact reason.
# # # • Test: 17, Indian → Not eligible: under 18
# # # • Test: 25, Nepali → Not eligible: not an Indian citizen

# # # age = int(input("Enter a age:"))
# # # citizen =input("Enter the Citizenship:")

# # # if age >=18 and citizen =="India" :
# # #     print(f"Age is {age} and Eligible to vote in {citizen}")
# # # else:
# # #     print(f"They are {citizen} and can't able to vote")


# # # Q2. ATM withdrawal
# # # Read account balance and withdrawal amount. Allow the withdrawal only if the amount is a multiple of 100,
# # # at most ₹10,000 per transaction, and not more than the balance. Print the new balance or the reason for
# # # failure.

# # # account_balance =100000
# # # withdraw_amount =int(input("Enter the amount to withdraw:"))



# # # if withdraw_amount % 100 != 0:
# # #        print(f"Failure: Amount must be a multiple of 100")
# # # elif withdraw_amount > 10000:
# # #     print(f"Failure: Maximum withdrawal limit is 10000")
# # # elif withdraw_amount > account_balance:
# # #     print(f"Failure: Insufficient balance")

# # # elif withdraw_amount <= 0:
# # #     print(f"Failure: Enter a valid positive amount")
# # # else:
# # #     new_balance = account_balance - withdraw_amount
# # #     print("Withdrawal successful!")
# # #     print(f"Remaining balance: {new_balance}")

# # # Q3. Traffic signal assistant
# # # Read the signal colour (red, yellow, green) in any case (RED, Green). Print Stop, Slow down or Go. Any other
# # # input prints Invalid signal — proceed with caution.
# # # Concept: normalise input with .lower() and .strip() before comparing.

# # signal_color = input("Enter the signal color:")
# # signal_color = signal_color.strip().lower()
# # if signal_color.lower() == "red" :
# #      print("Stop")
# # elif signal_color.lower()=="yellow":
# #      print("Be ready")
# # elif signal_color.lower() =="green":
# #      print("go")
# # else:
# #      print(f"Invalid Signal -proceed with caution")



# # Q4. Mobile data alert (Jio / Airtel style)
# # Read daily data limit (GB) and data used (GB). Calculate percentage used and print:
# # Usage
# # Message
# # Below 50%
# # 50% to below 90%
# # You're good
# # Half used — plan wisely
# # 90% to below 100%
# # 100% or more
# # Only a little left!
# # Limit reached — speed reduced to 64 Kbps

# daily_data = int(input("Enter the daily_data limit(GB):"))
# data_use = float(input("Enter the data used(GB):"))

# percentage_used = (data_use /daily_data) * 100
# print(percentage_used)
# if percentage_used < 50:
#     print(f"You're good")
# elif percentage_used >=50 and percentage_used < 90:
#     print(f"Half used -plan wisely")
# elif 90 <=percentage_used <100:
#     print("only a little bit")
# elif percentage_used >=100:
#     print(f"Limit reached-speed reduce to 64 kbps")
     

# Q5. Movie ticket pricing (BookMyShow style)
# Read age and show time (24-hour, e.g. 14). Base price ₹200. Children under 12 get 50% off; senior citizens
# 60+ get 30% off; morning shows (before 12) get an extra ₹30 off for everyone. Print the final price

print("BookMyShow")

age = int(input("Enter the age:"))
show_time = int(input("Enter the show time(hr):"))
base_price =200


if age <12 :
    dis_price = base_price * 50 / 100
    final_price = base_price - dis_price
    print(f"Children got 50% discount")


elif  age >=60 :
    dis_price = base_price * 30 / 100
    final_price = base_price - dis_price
    
    print(f"Senior citizens who are above 60 will get flat 30% discount, final price is:{dis_price}")

if show_time <12:
    final_price = base_price -30
    print(f"extra 30% off everyone")

print(f"final price,{final_price}")



