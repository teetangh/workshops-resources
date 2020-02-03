"""
Day 3 of workshop
"""

a = input("Input first number")
a = int(a)
b = input("Input second number")
b = int(b)
print(a+b)


def greetings_func(greeting="Hi", name="Mike", age=10):
    return "{} {} you are {}.".format(greeting, name, age)


sentence = greetings_func("Hello", age=20)
print(greetings_func())


def sayhi(name):
    print("Hi " + name)


sayhi("Mike")


def sayhi(name, age):
    print("Hi " + name + " you are " + str(age))


sayhi("Mike", 30)


def sayhi(name, age=20):
    print("Hi " + name + " you are " + str(age))


sayhi("Mike")

x = "global x"


def test(x):
    #    global x
    x = "outer x"

    def test2():
        #        nonlocal x
        x = "inner x"
        print(x)
    test2()
    print(x)


test(x)
print(x)


# Local,Enclosing,Global
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isleap(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


print(isleap(2020))


def printdays(year, month):
    if month < 1 or month > 12:
        return "Invalid month"
    elif isleap(year) and month == 2:
        return 29
    else:
        return days[month]


print(printdays(2020, 2))

'''
Python program to check if a string
contains all unique characters
'''


def uniqueCharacters(s):
    char_list = []
    for c in s:
        if c not in char_list:
            char_list.append(c)
        else:
            return False
    return True

#s = "management"
#s = "across"
#s = "algorithms"
# print(uniqueCharacters(s))


def uniqueCharacters(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[j] == s[i]:
                return False
    return True


s = "algorithms"
print(uniqueCharacters(s))


'''
Python program to check if a string is palindrome or not
'''


def isPalindrome(s):
    char_list = [c for c in s]
    char_list_copy = char_list.copy()
    char_list_copy.reverse()
    for i in range(len(char_list)):
        if char_list[i] != char_list_copy[i]:
            return False
    return True


#s = "bottle"
#s = "radar"
print(isPalindrome(s))

# def isPalindrome(s):
#
#    for i in range(0, len(s)//2):
#        if s[i] != s[len(s)-i-1]:
#            return False
#    return True


'''
Python program to check if a number is prime or not
'''


def isPrime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % 2 == 0:
            return False
    return True


num = 11
#num = 36
#num = 113
print(isPrime(num))
