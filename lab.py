import math
import point
#import numpy as np
# Problem 1: Quadratic Evaluation
#
# Hint: Remember that this problem asks you to print
# the solution.

"""
Evaluates and prints the solution to a quadratic
equation. Quadratic is in standard ax**2 + bx + c
form.

Parameters:
a (float) real number x**2 coefficient
b (float) real number x coefficient
c (float) real number constant term
x (float) x to evaluate at
"""
def quadratic_eval(a, b, c, x):
    print(a*x**2 + b*x + c)


# Problem 2: Distance Formula
#
# Hint: This problem asks you to print your solution,
# as well. You may want to look up the distance formula
# if it is unfamiliar to you.

"""
Finds and prints the distance between two points
p1 and p2.

Parameters:
p1 (Point) first point
p2 (Point) second point
"""
def find_distance(p1, p2):
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    distance = math.sqrt((x1-x2)**2 +((y1-y2)**2))
    print(distance)


# Problem 3: Arithmetic Mean
#
# Hint: The arithmetic mean is the mean we usually think of
# when we take an average. This problem now asks you to return
# your solution.

"""
Calculates and returns the arithmetic mean of
the given numbers.


Parameters:
numbers (set) set of numbers which may be empty

Returns:
float: arithmetic mean of numbers or None if none exists
"""
def arithmetic_mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


# Problem 4: Geometric Mean
#
# Hint: Remember you need to return the solution.

"""
Calculates and returns the geometric mean of 
the given numbers.

Parameters:
numbers (list) list of numbers which may be empty

Returns:
float: geometric mean of numbers or None if none
exists
"""
def geometric_mean(numbers):
    geo_product = 1
    num_length = len(numbers)
    if num_length == 0:
        return
    else:
        for y in numbers:
            geo_product = geo_product * y
        return float (geo_product**(1/num_length))



# Problem 5: Second Largest Number
#
# Hint: Take a look at Python's indexing documentation
# or our slides about this. You might use a for loop.

"""
Finds the second largest number in a list of input 
numbers.

Parameters:
numbers (list) list of numbers which may be empty

Returns:
float: second largest number in numbers or None 
if none exists
"""
def second_largest_number(numbers):
    second_largest_num = list(numbers)
    second_largest_num.sort()
    number_len = len(second_largest_num)
    if number_len == 0:
        return
    else:
        return second_largest_num[number_len-2]


# Problem 6: Number of Unique Names
# 
# Hint: A set is a collection of unique items!

"""
Finds the number of unique names in a list of 
names.

Parameters: 
names (list) list of names which may contain
duplicates

Returns: 
int: number of unique entries in list names
"""
def num_unique_names(names):
    # insert the list to the set
    list_set = set(names)
    # convert the set to the list
    unique_list = (list(list_set))
    return len(unique_list)



# Problem 7: Dictionary Swap
#
# Hint: When iterating through a dictionary, 
# you can access both the key and the value
# at the same time with .items()

"""
Given a one-to-one dictionary d of key-value
pairs, return a dictionary where the values of
d are the keys and the keys of d are the values.

Parameters:
d (dictionary) one-to-one dictionary of key-value
paris
ex. d = {
    "kampala" : "uganda", 
    "nairobi" : "kenya", 
    "kigali" : "rwanda"
}

Returns: 
dictionary: a swapped one-to-one dictionary with
d's values as keys, and the associated keys from
d as values
ex. return_dictionary = {
    "uganda" : "kampala", 
    "kenya" : "nairobi", 
    "rwanda" : "kigali"
}
"""
def dictionary_swap(d):
    d = dict((v, k) for k, v in d.items())

    return d



# Problem 8: Electric Bill
#
# You are running an electric company and need to
# make sure you are charging you customers fairly.
# Each month you know exactly how many kilowatt hours
# each of your customers used. However, customers get
# charged higher rates if they use a lot of electricity.
# Here are the rates:
#
# 0    - 1000 kWh: 2000 / kWh
# 1001 - 5000 kWh: 3500 / kWh
# 5001+       kWh: 4500 / kWh
#
# For example, if you used 6000 kWh, you would be charged:
# - 1000 * 2000 for the first 1000 kWhs,
# - 4000 * 3500 for the next 4000 kWhs,
# - 1000 * 4500 for the last 1000 kWhs.

"""
Calculates and returns the total monthly bill for one
customer based on their electricity usage.

Parameters:
kWh_used (int) usage rounded to the nearest integer

Returns:
int: electric bill in Ugandan Shillings for the month
"""
def electric_bill(kWh_used):
    if kWh_used <= 1000:
        total = kWh_used * 2000
        return total
    elif kWh_used > 1000 and kWh_used <= 5000:
        total = (1000*2000)+(kWh_used-1000)*3500
        return total
    else:
        total = (1000 * 2000) + (4000 * 3500) + (kWh_used - 5000) * 4500
        return total


# Problem 9: Warehouse Process
#
# In addition to owning an electric company, you also
# own a retail business! To handle all the incoming
# transactions, you decide to keep an inventory of
# your stock in the warehouse in a Python dictionary.
#
# You decide to write a function to handle updating
# this information. Each transaction is included
# three values:
#
# - type: either "buy" or "sell"
# - commodity: type of commodity purchased or sold
# - amount: some nonnegative quantity
#
# For example, if we purchase 10 backpacks, the
# backpack entry in our dictionary should increase by 10.
# On the other hand, if we sell 10, it would decrease by 10.
#
# Hint: This function does not return anything. It only
# updates the inventory dictionary that gets passed in.
# If the transaction is a sell, ensure the warehouse
# has enough of that item to complete the sale. Otherwise,
# you should raise a ValueError.

"""
Takes a single transaction and updates the warehouse
inventory as necessary.

Parameters:
inventory (dictionary) warehouse inventory
transaction (tuple) transaction of the form (type, commodity, amount)
"""
def warehouse_process(inventory, transaction):
    commodity = transaction[1]
    amount = transaction[2]
    if transaction[0] == "buy":
        if commodity in inventory.keys():
            inventory[commodity] += amount
        else:
            inventory[commodity] = amount
    else:
        if commodity in inventory.keys():
            inventory[commodity] -= amount
        else:
            return

# Problem 10: Fibonacci Sequence
#
# Hint: There are two base cases!

"""
Given a positive int n, uses recursion to return
the nth Fibonacci number.
https://en.wikipedia.org/wiki/Fibonacci_sequence

Parameters:
n (int) which Fibonacci number to return

Returns:
int: the nth Fibonacci number
"""
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 1
        # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



    # Problem 11: Hailstone Sequence
#
# Hint: There are two recursive cases!

"""
Given an int x, uses recursion to generate the
appropriate hailstone sequence and then returns
the number of steps to get to 1.
https://en.wikipedia.org/wiki/Collatz_conjecture

Parameters:
x (int) the starting input for the hailstone
sequence

Returns:
int: the number of steps the hailstone sequence
took to get to 1
"""
def hailstone(x):
        if x == 1:
            return 1
        elif x % 2 == 0:
            return 1 + hailstone(x / 2)
        else:
            return 1 + hailstone(3 * x + 1)


# Problem 12: Debts

"""
These methods all center around a dictionary
debts that keeps track of how much money each
person (dictionary keys) has borrowed by 
assigning each a list to track how much is
borrowed at a time (values). One entry might
look like: 
debts = {
    "Emily" : [5, 10, 3, 11]
    "Jeremy" : [2, 7, 5, 10]
}
"""
# Part 1: Borrow Money
# 
# Hint: Check the Python documentation for 
# dictionaries if you're feeling lost.

"""
Given a dictionary debts that tracks everyone's
debts and a string person who borrows int amt
of money, adds the person to the dictionary
with the amount owed (if person is not already
in the dictionary) or adds amt to the end of
the person's associated list (if person is 
already in the dictionary).

Parameters: 
debts (dictionary) a dictionary tracking people
who owe money
person (string) the name of the person who is
borrowing money
amt (int) the amount of money the person is 
borrowing

Returns: 
dictionary: a dictionary updated with the new
information
"""
def borrow_money(debts, person, amt):
    if person not in debts.keys():
        debts[person] = [amt]
    else:
        debts[person].append(amt)
    return debts

# Part 2: Calculate One Person's Debt
# 
# Hint: The sum function is very useful! 

"""
Given a dictionary debts that tracks everyone's
debts and a string person who has borrowed some
amount of money, calculates the total amount of
money the person has borrowed over time.

Parameters:
debts (dictionary) a dictionary tracking people
who owe money
person (string) the name of the person whose
debts we are summing

Returns: 
int: the total amount that the person owes
"""
def amt_owed_by(debts, person):
    if person in debts:
        total = sum(debts[person])
    return total

# Part 3: Calculate Total Amount Owed
# 
# Hint: Again, sum is very helpful! 

"""
Given a dictionary debts that tracks everyone's
debts, calculate the total amount of money
that everyone in it owes. 

Parameters: 
debts (dictionary) a dictionary tracking people
who owe money

Returns: 
int: the total amount owed by all the people in
the dictionary
"""
def total_amt_owed(debts):
    total = 0
    for h, r in debts.items():
        total= total + sum(r)
    return total
