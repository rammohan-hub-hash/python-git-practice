# Q1. Voter eligibility check (Election Commission)
# Read a person's age and citizenship (Indian / other). Print Eligible to vote only if age is 18 or above and
# citizenship is Indian. Otherwise print the exact reason.
# • Test: 17, Indian → Not eligible: under 18
# • Test: 25, Nepali → Not eligible: not an Indian citizen

age = int(input("Enter a age:"))
citizen =input("Enter the Citizenship:")

if age >=18 and citizen =="India" :
    print(f"Age is {age} and Eligible to vote in {citizen}")
else:
    print(f"They are {citizen} and can't able to vote")
