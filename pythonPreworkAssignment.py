'''
This program demonstrates my ability to pass the 
introduction section of Coding Temples Self Paced Software Engineering Bootcamp
Author: Karan Patel
'''
# Question 1

'''
Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below
'''
def hello_name(user_name):
    print(f"\nHello {user_name}!" )

hello_name('Karan')

# Question 2

'''
Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
'''
def first_odds():
    for i in range(100):
        if i % 2 == 1:
            print(i)
        else:
            print("nothing")

first_odds()

# Question 3

'''
Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below
'''

def max_num_in_list(a_list):
    maxNum = max(a_list)
    print(f"{maxNum} is the largest number present in the given list")

lst1 = [95,85,46,58,90,9,40,50]
max_num_in_list(lst1)
print('max num should be 95')
# Question 4

'''
Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
'''

def is_leap_year(a_year):
    if a_year % 4 == 0:
        print(f'{a_year} might be a leap year, last check')
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                print(f'{a_year}, you have passed the test to being a leap year!')
                return True
            else:
                print(f"{a_year} is not a leap year")
            return False
    else:
        print('not a leap year')
        return False

is_leap_year(2000)
is_leap_year(2400)
is_leap_year(1800)
is_leap_year(2300)

# Question 5 

'''
Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type
'''

lst1 = [1,2,3,4,5,6,7,8]
lst2 = [1,3,3,4,5,6,8,7]

def is_consecutive3(lst):
    return sorted(lst) == list(range(min(lst), max(lst) +1))

print('\nIs Consecutive')
print(is_consecutive3(lst2))


#print('first list is: ')
#is_consecutive1(lst2true)

#print('next list is:')
#is_consecutive1(lst2false)
