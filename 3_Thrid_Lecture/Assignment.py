# The Shortest Codeword of Lexicon City
# L = input().split(',')

# min_word = L[0]
# min_len = len(L[0])

# for w in L:
#     if len(w) <= min_len:
#         min_len = len(w)
#         min_word = w

# print(min_word)

# Cargo Weight Floor Converter
L = input().split()

for i in range(len(L)):
    L[i] = int(float(L[i]))

for i in range(len(L)):
    if i != len(L) - 1:
        print(L[i], end=",")
    else:
        print(L[i])
    
    
# import math

# nums = list(map(float, input().split()))

# result = [str(math.floor(x)) for x in nums]

# print(",".join(result))