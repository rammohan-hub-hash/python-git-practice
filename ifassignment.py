# # # # # # # # # Q1. Voter eligibility check (Election Commission)
# # # # # # # # # Read a person's age and citizenship (Indian / other). Print Eligible to vote only if age is 18 or above and
# # # # # # # # # citizenship is Indian. Otherwise print the exact reason.
# # # # # # # # # • Test: 17, Indian → Not eligible: under 18
# # # # # # # # # • Test: 25, Nepali → Not eligible: not an Indian citizen

# # # # # # # # # age = int(input("Enter a age:"))
# # # # # # # # # citizen =input("Enter the Citizenship:")

# # # # # # # # # if age >=18 and citizen =="India" :
# # # # # # # # #     print(f"Age is {age} and Eligible to vote in {citizen}")
# # # # # # # # # else:
# # # # # # # # #     print(f"They are {citizen} and can't able to vote")


# # # # # # # # # Q2. ATM withdrawal
# # # # # # # # # Read account balance and withdrawal amount. Allow the withdrawal only if the amount is a multiple of 100,
# # # # # # # # # at most ₹10,000 per transaction, and not more than the balance. Print the new balance or the reason for
# # # # # # # # # failure.

# # # # # # # # # account_balance =100000
# # # # # # # # # withdraw_amount =int(input("Enter the amount to withdraw:"))



# # # # # # # # # if withdraw_amount % 100 != 0:
# # # # # # # # #        print(f"Failure: Amount must be a multiple of 100")
# # # # # # # # # elif withdraw_amount > 10000:
# # # # # # # # #     print(f"Failure: Maximum withdrawal limit is 10000")
# # # # # # # # # elif withdraw_amount > account_balance:
# # # # # # # # #     print(f"Failure: Insufficient balance")

# # # # # # # # # elif withdraw_amount <= 0:
# # # # # # # # #     print(f"Failure: Enter a valid positive amount")
# # # # # # # # # else:
# # # # # # # # #     new_balance = account_balance - withdraw_amount
# # # # # # # # #     print("Withdrawal successful!")
# # # # # # # # #     print(f"Remaining balance: {new_balance}")

# # # # # # # # # Q3. Traffic signal assistant
# # # # # # # # # Read the signal colour (red, yellow, green) in any case (RED, Green). Print Stop, Slow down or Go. Any other
# # # # # # # # # input prints Invalid signal — proceed with caution.
# # # # # # # # # Concept: normalise input with .lower() and .strip() before comparing.

# # # # # # # # signal_color = input("Enter the signal color:")
# # # # # # # # signal_color = signal_color.strip().lower()
# # # # # # # # if signal_color.lower() == "red" :
# # # # # # # #      print("Stop")
# # # # # # # # elif signal_color.lower()=="yellow":
# # # # # # # #      print("Be ready")
# # # # # # # # elif signal_color.lower() =="green":
# # # # # # # #      print("go")
# # # # # # # # else:
# # # # # # # #      print(f"Invalid Signal -proceed with caution")



# # # # # # # # Q4. Mobile data alert (Jio / Airtel style)
# # # # # # # # Read daily data limit (GB) and data used (GB). Calculate percentage used and print:
# # # # # # # # Usage
# # # # # # # # Message
# # # # # # # # Below 50%
# # # # # # # # 50% to below 90%
# # # # # # # # You're good
# # # # # # # # Half used — plan wisely
# # # # # # # # 90% to below 100%
# # # # # # # # 100% or more
# # # # # # # # Only a little left!
# # # # # # # # Limit reached — speed reduced to 64 Kbps

# # # # # # # daily_data = int(input("Enter the daily_data limit(GB):"))
# # # # # # # data_use = float(input("Enter the data used(GB):"))

# # # # # # # percentage_used = (data_use /daily_data) * 100
# # # # # # # print(percentage_used)
# # # # # # # if percentage_used < 50:
# # # # # # #     print(f"You're good")
# # # # # # # elif percentage_used >=50 and percentage_used < 90:
# # # # # # #     print(f"Half used -plan wisely")
# # # # # # # elif 90 <=percentage_used <100:
# # # # # # #     print("only a little bit")
# # # # # # # elif percentage_used >=100:
# # # # # # #     print(f"Limit reached-speed reduce to 64 kbps")
     

# # # # # # # Q5. Movie ticket pricing (BookMyShow style)
# # # # # # # Read age and show time (24-hour, e.g. 14). Base price ₹200. Children under 12 get 50% off; senior citizens
# # # # # # # 60+ get 30% off; morning shows (before 12) get an extra ₹30 off for everyone. Print the final price

# # # # # # print("BookMyShow")

# # # # # # age = int(input("Enter the age:"))
# # # # # # show_time = int(input("Enter the show time(hr):"))
# # # # # # base_price =200


# # # # # # if age <12 :
# # # # # #     dis_price = base_price * 50 / 100
# # # # # #     final_price = base_price - dis_price
# # # # # #     print(f"Children got 50% discount")


# # # # # # elif  age >=60 :
# # # # # #     dis_price = base_price * 30 / 100
# # # # # #     final_price = base_price - dis_price
    
# # # # # #     print(f"Senior citizens who are above 60 will get flat 30% discount, final price is:{dis_price}")

# # # # # # if show_time <12:
# # # # # #     final_price = base_price -30
# # # # # #     print(f"extra 30% off everyone")

# # # # # # print(f"final price,{final_price}")


# # # # # #                            Level 2 — Intermediate (5 problems)

# # # # # # Q6. Electricity bill calculator (slab tariff)


# # # # # units = int(input("Enter the units consumed:"))
# # # # # fixedcharge = 50

# # # # # if units <0:
# # # # #      print("Invalid Units")

# # # # # else:

# # # # #  if units in range(0,101):
# # # # #     price = units * 1.50
   
# # # # #  elif units in range(101,201):
# # # # #     price = (100 *1.5) + ((units -100) *2.50)
    
# # # # #  elif units in range(201,301):
# # # # #     price = (100 *1.5) + (100 * 2.50) +((units -200) *4)

    
# # # # #  elif units >300:
# # # # #      price = (100 * 1.50) + (100 * 2.50) + (100 * 4) + ((units - 300) * 6)

# # # # #  if units >0:
# # # # #     subtotal = price + fixedcharge

# # # # #     surcharge =0

# # # # #  if subtotal >1000:
# # # # #         surcharge = subtotal * 0.05
       

# # # # # total = subtotal + surcharge

# # # # # print("Energy charge:", price)
# # # # # print("Fixed charge:", fixedcharge)
# # # # # print("Surcharge:", surcharge)
# # # # # print("Total bill:", total)



# # # # # Q7. Bank loan eligibility (simplified)
# # # # # Read monthly salary, CIBIL score, age and existing EMI. Approve only if all hold: salary ≥ ₹25,000; CIBIL ≥
# # # # # 700; age 21–58; existing EMI ≤ 40% of salary. If rejected, print every rule that failed, not just the first one.
# # # # # Hint: use separate if statements (not elif) to collect all failures


# # # # Monthly_Salary = int(input("Enter Monthly Salary:"))
# # # # Cibil_score = int(input("Enter the Cibil score:"))
# # # # age = range(21,59)
# # # # age1 = int(input("Enter the age:"))
# # # # existing_emi = int(input("Enter the Existing EMI Amount:"))

# # # # Allowed_emi = (Monthly_Salary * 40 ) / 100

# # # # print(Allowed_emi)

# # # # if Monthly_Salary > 2500 and Cibil_score >700 and 21 <age1 <59 and existing_emi <= Allowed_emi:
# # # #     print("You are eligible bro")

# # # # if Monthly_Salary <25000:
# # # #     print(f"Not Eligible because of salary")
# # # # if Cibil_score <700:
# # # #     print(f"cibil score is less")
# # # # if age1 < 21:
# # # #     print(f"age is too less to get loan ")
# # # # if existing_emi >Allowed_emi:
# # # #     print(f"Your Existing loan is higher than the 40% of your salary")

# # # # print("Thank you")



# # # Q8. Student grade and scholarship
# # # Read marks in 5 subjects (out of 100). Compute percentage and grade

# # # A student who scored below 35 in any subject fails regardless of percentage. Grade A+ with attendance ≥
# # # 85% earns a 50% scholarship

# # Maths = int(input("Enter the Math Marks:"))
# # Physics = int(input("Enter the Physics Marks:"))
# # Chemistry = int(input("Enter the Chemistry Marks:"))
# # English = int(input("Enter the English Marks:"))
# # Sanskrit = int(input("Enter the Sanskrit Marks:"))

# # attendance = float(input("Enter attendance percentage: "))

# # total_marks = Maths + Physics + Chemistry + English + Sanskrit
# # Percentage = (total_marks /5) 
               
# # if Maths < 35 or Physics < 35 or Chemistry < 35 or English < 35 or Sanskrit < 35:
# #     print("Fail: Scored below 35 in a subject")


# # if Percentage >=90:
# #     if attendance >=85:

# #      print(f"Grade A+ and Earns 50% scholarship")
# # elif 75 < Percentage < 89:
# #     print(f"Grade A")
# # elif 60 <Percentage <74:
# #     print(f"Grade B")
# # elif 40 < Percentage <59:
# #     print("Grade C")
# # elif Percentage <40:
# #     print(f"Fail")

# # Q9. Online shopping discount engine (Flipkart / Amazon style)
# # Read cart value, payment mode (UPI, card, COD) and whether it's the user's first order.
# # • First order: 20% off, max ₹300
# # • Otherwise, cart ≥ ₹5,000: 10% off; cart ≥ ₹2,000: 5% off
# # • Card payment: extra ₹100 off on carts ≥ ₹3,000
# # • COD on carts above ₹10,000 is not allowed — print a message and ask for another mode
# # Print the cart value, each discount applied, and the final amount.

# cart_value = int(input("Enter the Value:"))
# #Payment_mode = input("Enter the Mode of payment")

# first_order =False

# if first_order:
#     discount = cart_value * 20 /100
#     final_price = cart_value - discount
#     price = cart_value- 300
#     print(f"20% off :{final_price},max discount:{price}")

# elif cart_value >=5000:
#     discount = cart_value * 10 /100
    
# elif cart_value >=2000:
#     discount = cart_value * 5/100

# print("Cart value:", cart_value)
# print("Shopping discount:", discount)


# Payment_mode = input("Enter the Mode of payment(UPI/Card/COD):").upper()




# if Payment_mode == "COD" and cart_value >10000:
#     print("Not allowed.Please change the Mode of Payment")


#     Payment_mode = input("Enter another payment mode: ").upper()


# card_discount =0

# if Payment_mode == "Card" and cart_value >=3000:
#     card_discount =100

# print("Card discount:", card_discount)


# total_discount = discount + card_discount
# final_price = cart_value - total_discount

# print("-------------------------")
# print("Cart value:", cart_value)
# print("Shopping discount:", discount)
# print("Card discount:", card_discount)
# print("Total discount:", total_discount)
# print("Final amount:", final_price)


# Q10. Leap year and days-in-month checker
# Read a year and month number. Print how many days the month has. A year is a leap year if divisible by 4,
# except century years, which must be divisible by 400 (so 2000 is a leap year, 1900 is not). Reject month
# numbers outside 1–12.

year = int(input("Enter a year: "))
Month = int(input("Enter a month (1-12): "))


if year % 400 == 0:
    leap_yr = True
    
elif year % 100 == 0:
    leap_yr = False
elif year % 4 == 0:
    leap_yr = True
else:
    leap_yr = False

if Month < 1 or Month > 12:
    print("Invalid Month")
else:
    if Month == 2:
        if leap_yr:
            days = 29
        else:
            days = 28
    elif Month in (4, 6, 9, 11):
        days = 30  
    else:
        days = 31  

    print("Year:", year)
    print("Month:", Month)
    print("Leap year:", leap_yr)
    print("Days in month:", days)