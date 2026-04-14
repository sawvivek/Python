# nested loop
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()
    

# palindrome number checker in python
# n=input("Enter a number :")
# n=int(n)
# ori=n
# rev=0
# while(n>0):
#     rev=rev*10+(n%10)
#     n //=10
    
# if(rev==ori):
#     print("Palindrome")
# else:
#     print("Not palindrome")

# smart discount calculator


# def calculate_discount(purchase_amount, customer_type):
#     # Initialize discount variables
#     purchase_discount = 0
#     premium_discount = 0
#     final_discount = 0

#     # 1. Purchase Amount Based Discount (10%)
#     if purchase_amount >= 1000:
#         purchase_discount = 0.10 * purchase_amount

#     # 2. Customer Type Based Discount (5%)
#     # Only applicable for premium customers with purchase >= 2000
#     if customer_type == "premium" and purchase_amount >= 2000:
#         premium_discount = 0.05 * purchase_amount

#     # 3. Final Discount Selection Rule
#     # Apply only the higher benefit (higher discount value)
#     final_discount = max(purchase_discount, premium_discount)

#     # 4. Safety Rules
#     if final_discount > purchase_amount:
#         final_discount = purchase_amount
    
#     final_payable = purchase_amount - final_discount
    
#     if final_payable < 0:
#         final_payable = 0

#     return purchase_amount, final_discount, final_payable

# # Example Usage:
# amount = float(input("Enter the purchase amount: "))
# amount=float(amount)
# c_type = input("Enter the customer type (regular/premium): ")
# original, discount, total = calculate_discount(amount, c_type)

# print(f"Original Amount: ₹{original}")
# print(f"Discount Applied: ₹{discount}")
# print(f"Final Payable: ₹{total}")



# Programming Assignment

# 1. Get input as a list of strings
# L = input().split()

# # 2. Manually convert strings to integers using a loop
# nums = []
# for x in L:
#     nums.append(int(x))

# # 3. Manually calculate the total sum
# total = 0
# for x in nums:
#     total += x

# # 4. Calculate average
# avg = total / len(nums)

# # 5. Count numbers greater than average
# count = 0
# for x in nums:
#     if x > avg:
#         count += 1

# print(count)


# # 2. Temperature Alert System
# L = input().split() 
# result = []

# for x in L:
#     if int(x) > 50:
#         result.append(x)

# if len(result) == 0:
#     print(0)
# else:
#     print(" ".join(result))

# 3.Signal Checker

L=input().split()
result=[]

for x in L:
    result.append(int(x))
flag =True
for i in range(len(result)-1):
    if(result[i]>=result[i+1]):
        flag =False
        break
print(flag)