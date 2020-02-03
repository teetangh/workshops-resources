"""
Day 2 of workshop.
"""

print(3 < 5)
print(1.8 > 4)
print(5 == 5.0)
print('a' != 'A')
print(3.14 <= 3.13)
print('B' >= 'A')
print('A' == "A")

num_list = [45, 63, 21, 9, 75]
print(num_list)
print(21 in num_list)
print(5 in num_list)
print(5 not in num_list)
print()
#
word = "Metropolitan"
print(word)
print('p' in word)
print('metro' in word)
print('Metro' in word)
print()

month_conversions = {"jan": "January", "mar": "March", "dec": "December"}
print(month_conversions)
print('mar' in month_conversions)
print("March" in month_conversions.values())
print()

bool_true = True
bool_false = False
#
print(bool_true and bool_false)
print(bool_true and bool_true)
print(bool_true or bool_false)
print(bool_false and bool_false)
print(not bool_true)
print(not bool_false and bool_true)

example = {1: 10, 'True': 23, True: 2}

print(example)
print(example[True])
print(example['True'])


is_present = True
if is_present:
    print("You are present in class!")
else:
    print("You are absent!")

is_present = False
is_sleeping = False

if is_present and is_sleeping:
    print("You are present in class but you are sleeping!")
elif is_present and not is_sleeping:
    print("You are present in class but you are not sleeping!")
elif not is_present and is_sleeping:
    print("You are sleeping in your room!")
else:
    print("You have lots of attendence!")


num_list = [4, 7, 1, 2, 5]
number = 10

if number in num_list:
    if number == max(num_list):
        print("The given number is the largest number in the list.")
    else:
        print("The given number is not the largest number in the list.")
else:
    print("Error: number not in list.")


print("The number is 1")
print("The number is 2")
print("The number is 3")
print("The number is 4")
print("The number is 5")
print()

num = 1
print("The number is {}".format(num))
num = 2
print("The number is {}".format(num))
num = 3
print("The number is {}".format(num))
num = 4
print("The number is {}".format(num))
num = 5
print("The number is {}".format(num))
print()

num = 1
while num <= 20:
    print("The number is {}".format(num))
    num += 1

print("End of loop")
print()


for a in "Python loop":
    if a == ' ':
        break
    else:
        print(a)
print(a)
print("End of loop")
print()

friends = ["Ross", "Rachel", "Joey", "Monica", "Chandler", "Phoebe"]

for friend in friends:
    print(friend)
print()

months_conversion = {"jan": "January",
                     "feb": "Febuary",
                     "nov": "November",
                     "dec": "December",
                     "oct": "October"}

for month_code, month in months_conversion.items():
    print(month_code, month)
print()

for month in months_conversion.values():
    print(month)
print()

for month_code, month in months_conversion.items():
    print(month_code, month)
print()

for month_code, month in months_conversion.items():
    if(month_code == "feb"):
        print("{} has 28 days".format(month))
    elif(month_code == "nov"):
        print("{} has 30 days".format(month))
    else:
        print("{} has 31 days".format(month))
print()


for num in range(11, 20, 5):
    print(num)
print()

num_list = list(range(1, 11))
print(num_list)


friends = ["Ross", "Rachel", "Joey", "Monica", "Chandler", "Phoebe"]
for index in range(len(friends)):
    print(index)
print()

car_releases = {1967: "Chevrolet Camero",
                1965: "Ford Mustang",
                1969: "Dodge Charger",
                1961: "Jaguar E-Type",
                1964: "Aston Martin DB5"}
#
year_list = list(car_releases.keys())
print(year_list)
year_list.sort()
print(year_list)
for year in year_list:
    print(year, car_releases[year])


print(range(1, 10))

num_list = list(range(1, 10))
print(num_list)

num_list = list(range(1, 10))
print(num_list)
num_sq_list = []
for n in num_list:
    num_sq_list.append(n**2)
print(num_sq_list)

# I want n**2 for each n in num_list

num_sq_list = [n**2 for n in num_list if n != 3]
print(num_sq_list)
num_sq_list = [n**2 for n in num_list]
print(num_sq_list)

# I want n for each n in num_list if n is even

num_even_list = [n for n in num_list if n % 2 == 0]
print(num_even_list)

word = "walk"
number = "1234"

new_list = []
for letter in word:
    for n in number:
        new_list.append((letter, n))
print(new_list)
print()

new_list = [(letter, n) for letter in word for n in number]
print(new_list)


countries = ["India", "China", "England", "France", "Australia"]
capitals = ["New Delhi", "Beijing", "London", "Paris", "Canberra"]
#
country_capital = list(zip(countries, capitals))
print(country_capital)
print()

country_capital_dict = {}
for country, capital in country_capital:
    country_capital_dict[country] = capital
print(country_capital_dict)

country_capital_dict = {country: capital for country,
                        capital in zip(countries, capitals)}
print(country_capital)
