# import random
# year = random.randint(1993,2026)
# print("The year is: ",year)
# if((year%4==0 and year%100!=0) or year %400==0):
#     print("The year is a leap year")
# else:
#     print("The year is not a leap year") 
    

# # 1. Generate a random Year and Month
# year = random.randint(1993, 2018)
# month = random.randint(1, 12)

# # 2. Check for Leap Year first (to handle February)
# is_leap = False
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     is_leap = True

# # 3. Generate Day based on the specific conditions shown in the video
# if month == 2 and is_leap:
#     # February in a leap year
#     day = random.randint(1, 29)
# elif month == 2 and not is_leap:
#     # February in a non-leap year
#     day = random.randint(1, 28)
# elif month % 2 == 0 and month < 7:
#     # Even months before July (April, June)
#     day = random.randint(1, 30)
# elif month % 2 == 0 and month > 7:
#     # Even months after July (August, October, December)
#     day = random.randint(1, 31)
# elif month % 2 != 0 and month <= 7:
#     # Odd months up to July (Jan, March, May, July)
#     day = random.randint(1, 31)
# elif month % 2 != 0 and month > 7:
#     # Odd months after July (September, November)
#     day = random.randint(1, 30)

# print(f"Generated Date: {day}/{month}/{year}")
    
import random
import datetime
brithday=[]
i=0
while(i<50):
    year =random.randint(1993, 2026)
    
    if(year%4==0 and year%100!=0) or year %400==0:
        leap=1
    else:
        leap=0
    month=random.randint(1,12)
    if(month==2 and leap==1):
        day=random.randint(1,29)
    elif(month==2 and leap==0):
        day=random.randint(1,28)
    elif(month==7 and month ==8):
        day=random.randint(1,31)
    elif(month%2!=0 and month<7):
        day=random.randint(1,31)
    elif(month%2!=0 and month>7 and month<=12):
        day=random.randint(1,30)
    else:
        day=random.randint(1,30)
        
    dd=datetime.date(year,month,day)
    day_of_year=dd.timetuple().tm_yday
    brithday.append(day_of_year)
    i=i+1

brithday.sort()
i=0
while(i<50):
    print(brithday[i])
    i=i+1