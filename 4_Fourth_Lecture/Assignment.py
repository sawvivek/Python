# Question 1
# At DataWorks, software systems rely on reusable list utility functions to safely extract elements from datasets without causing runtime errors.
# def safe_first(L):
#     if L == []:
#         return None
#     return L[0]

# def safe_last(L):
#     if L == []:
#         return None
#     return L[-1]

# def safe_middle(L):
#     if L == []:
#         return None
#     if len(L) < 3:
#         return []
#     return L[1:-1]
# L = eval(input())

# print(safe_middle(L))

# Question 2
# A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself).

# def is_perfect(n):
#     if n <= 1:
#         return False

#     s = 0
#     for i in range(1, n):
#         if n % i == 0:
#             s += i

#     return s == n
# n = int(input())
# print(is_perfect(n))

# Question 3

# Data validation systems often need to detect duplicate values in datasets to ensure data integrity.
def has_duplicates(L):
    seen = []
    for x in L:
        if x in seen:
            return True
        seen.append(x)
    return False
L = eval(input())
print(has_duplicates(L))