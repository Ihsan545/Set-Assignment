"""
Program: set_membership.py
Author: Ihsanullah Anwary
Date:   10/14/2020
This program is an example of function accept a set and return a boolean.
 """




def in_set(my_set):
    """"accept a set and return a boolean"""
    for i in my_set:
        return 5 in my_set  # returning true or fals.


if __name__ == '__main__':
    print(in_set({0, 1, 2, 3, 4}))
    """" calling the function"""
