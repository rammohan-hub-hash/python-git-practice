
#                                                 Level 1: Basic (1–10)
#   Print numbers from 1 to 10.
# for i in range(1,11):
#     print( i ,end = "-"  )

    # 2 Print numbers from 10 to 1 in reverse order.
# for i in range(10,0,-1):
#     print(i ,end =" ")

# # 3 Print all even numbers from 2 to 20.
# for i in range (2,20,2):
#     print(i,end=" ")

# 4 Print all odd numbers from 1 to 19.
# for i in range (1,19,2):
#     print(i,end=" ") 

# 5 Print the multiplication table of 7, from 7 × 1 to 7 × 10.
# for i in range(1,11):
#     print (f"7 * {i} = { 7 * i}")

 # 6Calculate the sum of numbers from 1 to 10.
# for i in range(1,11):
#     print(i+i,end=" ")

# 7 Print the squares of numbers from 1 to 10.

# print("square:",end="")
# for i in range(1,11):
#     print((i *i),end=" ")

# 8 Print the cubes of numbers from 1 to 5.
# print("cube:",end="")
# for i in range (1,6):
#     print((i *3) ,end=" ")

# 9 Count how many numbers from 1 to 50 are divisible by 5.
# count =0
# for i in range(1,51):
#     if i % 5 ==0:
#         count +=1
# print("count:",count)

# # 10 Calculate the sum of all even numbers from 1 to 100.

# sum =0
# for i in range(1,101):
#     if i % 2==0:
#         sum +=i
# print("sum of even numbers:",sum)


                                         # Level 2: Easy to Medium (11–20)
# Focus: conditions inside loops, counting, and accumulating values.      

# 11 Print every number between 1 and 100 that is divisible by both 3 and 5.                                   
# count =0
# for i in range(1,100):
#     if i % 3 ==0 and i % 5 ==0:
#         print(i,end=" ")
#         count +=1
# print()
# print(f"total numbers that are divisible by 3 and 5:",count)

# # 12 Find the sum of numbers from 1 to a user-entered number n.
# user_entered =int(input("Enter a number:"))
# total =0
# for i in range (1,user_entered+1):
#     total +=i
# print(" sum ofnumbers:",total)

# 13 Find the factorial of a user-entered number. Example: 5! = 120.
user_entered =int(input("Enter a number:"))
factorial =1
for i in range(1,user_entered):
    factorial *= i
print("Factorial:", factorial)



