
# #                             Level 1 — Basic Logic
# # 1. Multiplication table grid
# # Print multiplication tables from 1 to 5, each table showing multipliers from 1 to 10.

# # table = range(1,6)
# # multiplication = range(1,11)
# # for t in table:
# #     for m in multiplication:
# #         print(f'{t} * {m} = {t * m}',end ="\t") 
# #         print()


# # 2. Star rectangle
# # Print 4 rows, each containing 6 stars.

# # ik = range(5)
# # jk =range(6)
# # for i in ik:
# #     for j in jk:
# #         print("*",end="")
# #     print()


# # print("*",end="")
# # print("*",end="")

# # 3. Number triangle
# # Print this pattern:
# # 1
# # 12
# # 123
# # 1234
# # # 12345
# # for i in range(1,6):
# #     for j in range (1,i+1):
# #         print(j,end="")
# #     print()

# # 1
# # 22
# # 333
# # 4444
# # 55555

# # for i in range(1,6):
# #     for j in range(i):
# #         print(i,end="")
# #     print()

# # 4. Coordinate pairs
# # Print every possible pair where x is from 1–3 and y is from 1–3.

# # for i in range(1,4):
# #     for j in range (1,4):
# #         print(i,j)

# # 5. Student marks
# # students = ["Ravi", "Priya", "Kiran"]
# # subjects = ["Maths", "Science", "English"]

# # # Print every student with every subject

# # for s in students:
# #     for sub in subjects:
# #         print(f'student:{s}, subject:{sub}')

#                         # Level 2 — Intermediate
# # 6.Right triangle of stars

# # *
# # **
# # ***
# # ****
# # *****

# # for i in range(1,6):
# #     for j in range(1,i+1):
# #         print("*",end="")
# #     print()

# # 7. Reverse number triangle
# # 12345
# # 1234
# # 123
# # 12
# # 1

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# # 55555
# # 4444
# # 333
# # 22
# # 1

# for i in range(5,0,-1):
#     for j in range(i):
#         print(i,end="")
#     print()

# 1
# 23
# 456
# 78910
# Hint: Use a variable outside both loops to keep track of the next number. Try it yourself first, mama!
# number =1
# for i in range (1,5):
#     for j in range (i):
#      print(number,end="")
#      number +=1
#     print()

# number = 1

# for i in range(1, 5):
#     for j in range(i):
#         print(number, end="")
#         number += 1
#     print()


# 8. Find common items

list1 = [10, 20, 30, 40]
list2 = [20, 40, 50, 60]

# Use nested loops to print common values: 20, 40.

for list in list1:
   for l in list2:
      if list==l:
         print(list)

