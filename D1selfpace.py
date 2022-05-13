#Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name (username):
    """Print hello to the user"""
    print(" Hello, " + username + '!')
    
hello_name(username='Alex')


#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    """Print only odds"""
    for i in range(1,101):
        if i % 2 == 1:
            print(i)
first_odds()

#Question 3: Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    max = a_list[0]
    for max_num in a_list:
        if max_num > max:
            max = max_num
    return max
print(max_num_in_list([1, 2, 3, 4]))

#Question 4: Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if (a_year%4==0 and a_year%100!= 0) or (a_year%400 == 0):
     return True
    return False
print(is_leap_year(2004))

#Question 5: Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    num_list = set(a_list)
    return len(a_list) == len(num_list) and num_list == set(range(min(a_list), max(a_list)+1))

is_consecutive([1, 2, 3, 4])