# from pathlib import Path

# file_path = Path(__file__).with_name("file1.txt")
# with file_path.open() as f:
#     print(f.read())

# with file_path.open("a") as f:
#     f.write("This is a new line.\n")
   
# random library

import random

rand_num=random.randint(1,5)
print(rand_num)

rand_odd_num=random.randrange(1,10,2)
print(rand_odd_num)

rand_even_num=random.randrange(0,10,2)
print(rand_even_num)

print(random.random())