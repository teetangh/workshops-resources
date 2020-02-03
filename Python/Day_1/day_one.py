'''
Day 1 of workshop.
'''
print("Hello World")  # prints things out to the console


print("Luigi was travelling in a local train in Texas.")
print('"Hey you look new here,are you a tourist?"asked Chad.')
print('Luigi:"Yes I will be in Texas for 8 days and Utah for 3 days."')
print('"So,how do you find America?"asked Chad.')
print("\"Turn left at Greenland.\" said Lugi.")


tourist_name = "Luigi"
print(tourist_name)
print(tourist_name + " was travelling in a local train in Texas.")
print('"Hey you look new here,are you a tourist?"asked Chad.')
print(tourist_name + ':"Yes I will be in Texas for 8 days and Utah for 3 days."')
print('"So,how do you find America?"asked Chad.')
print("\"Turn left at Greenland.\" said", tourist_name, '.')


tourist_name = "Luigi"
t_days = '3'
u_days = '5'
print(tourist_name + " was travelling in a local train in Texas.")
print('"Hey you look new here,are you a tourist?"asked Chad.')
print(tourist_name + ':"Yes I will be in Texas for ' +
      t_days + ' days and Utah for ' + u_days + ' days."')
print('"So,how do you find America?"asked Chad.')
print("\"Turn left at Greenland.\" said " + tourist_name + '.')


total_days = t_days + u_days
print(tourist_name + " stayed in America for " + total_days + " days.")

print(14 % 5)

num_1 = 9
num_2 = 4
num_3 = 6.813

print(num_1 + num_2)
print(num_3 + num_2)
print(num_2 * num_3 - num_1)
print(num_2 * (num_3 - num_1))
print(num_1 % num_2)
print(num_1**num_2)
print(num_1 / num_2)
print(num_1 // num_2)
print(num_3 / num_2)
print(num_3 // num_2)


tourist_name = "Luigi"
t_days = 3
u_days = 5
print(tourist_name + " was travelling in a local train in Texas.")
print('"Hey you look new here,are you a tourist?"asked Chad.')
print(tourist_name + ':"Yes I will be in Texas for ' +
      str(t_days) + ' days and Utah for ' + str(u_days) + ' days."')
print('"So,how do you find America?"asked Chad.')
print("\"Turn left at Greenland.\" said ", tourist_name, '.')

total_days = t_days + u_days
print(tourist_name + " stayed in America for ", total_days, " days.")


tourist_name = "Luigi"
t_days = 3
u_days = 5
print("{} was travelling in a local train in Texas.".format(tourist_name))
print('"Hey you look new here,are you a tourist?" asked Chad.')
print('{1}:"Yes I will be in Texas for {0} days and Utah for {2} days."'.format(
    t_days, tourist_name, u_days))
print('"So,how do you find America?"asked Chad.')
print("\"Turn left at Greenland.\" said {}.".format(tourist_name))

total_days = t_days + u_days
print("{} stayed in America for {} days.".format(total_days, tourist_name))


tourist_name = "Luigi"
t_days = 3
u_days = 5
paragraph = """{0} was travelling in a local train in Texas.
"Hey you look new here,are you a tourist?" asked Chad.
{0}:"Yes I will be in Texas for {1} days and Utah for {2} days."
"So,how do you find America?"asked Chad.
"Turn left at Greenland.\" said {0}."""

print(paragraph.format(tourist_name, t_days, u_days))


print("\t Mighty Mighty MIT")
print("Mighty Mighty MIT \n")
print("Mighty Mighty MIT \n" * 3)
print(r"\t Mighty Mighty MIT \n")


print(min(3, 5, 11, 1))
print(max(12.23, 34.43, 29, 45))
print(len("Breaking Bad"))
print("ALL small".lower())
print("all BIG".upper())


friends = ["Ross", "Rachel", "Joey", "Monica"]

print(friends)
print()
print(type(friends))
print()
print(friends[2])
print()
print(type(friends[2]))
print()
print(friends[-1])
print()
print(friends[1:3])
print()
print(friends[1:])
print()
print(friends[:3])
print()

friends[0] = "Chandler"
print(friends)
print()


friends = ["Ross", "Rachel", "Joey", "Monica"]
numbers = [7, 36, 11, 9, 23]


friends.append("Phoebe")
print(friends)
print()
friends.insert(2, "Chandler")
print(friends)
print()
friends.remove("Ross")
print(friends)
print()
friends.pop()
print(friends)
print()
friends.pop(0)
print(friends)
print()
friends.append(numbers)
print(friends)
print(friends[-1])
print(friends[-1])
print()
friends.pop()
friends.extend(numbers)
print(friends)
print()
print(friends[-1])
print()


friends = ["Ross", "Rachel", "Joey", "Rachel", "Monica"]
numbers = [7, 36, 11, 9, 23]

print(friends.count("Rachel"))
print()

print(len(friends))
print()

friends.sort()
print(friends)
print()

numbers.sort()
print(numbers)
print()

print(numbers.index(9))
print()

numbers.reverse()
print(numbers)
print()

numbers.clear()
print(numbers)
print()


friends = ["Ross", "Rachel", "Joey", "Rachel", "Monica"]
friends_2 = friends

print(friends)
print(friends_2)
print()

friends_2.pop()
print(friends)
print(friends_2)
print()
friends_copy = friends.copy()
print(friends)
print(friends_copy)
print()

friends_copy.pop()
print(friends)
print(friends_copy)
print()
#
friends_copy_new = list(friends)
friends_copy_new.pop()
print(friends)
print(friends_copy_new)
print()


coordinates = (1, 2, 3)
print(coordinates)
print(coordinates[1])
print()

#coordinates[1] = 3

list1 = [1, 2, 3]
tuple1 = tuple(list1)
print(tuple1)

number_list = [5, 3, 1, 7, 1]
number_tup = tuple(number_list)
print(number_tup)

coordinate_list = [(1, 3), (6, 8), (4, 2)]
coordinate_list.append((5, 5))
print(coordinate_list)


months_conversion = {"jan": "January", "feb": "February",
                     "nov": "November", "dec": "December", "oct": "October"}

print(months_conversion["feb"])
print()

print(len(months_conversion))
print()

print(months_conversion["jan"])
print()

# print(months_conversion["aug"])
# print()

print(months_conversion.get("jan", "Invalid key"))
print()

months_conversion["ju"] = "June"
print(months_conversion)
print()

months_conversion["ju"] = "July"
print(months_conversion)
print()

print(months_conversion.values())
print()

print(months_conversion.keys())
print()

print(months_conversion.items())
months_tup = list(months_conversion.items())
print(months_tup[1])
print()

# months_conversion.sort()

months_conversion.pop("jan")
print(months_conversion)
print()

months_new = dict(months_conversion)
months_new["aug"] = "August"
print(months_conversion)
print(months_new)
print()


# software_products = {["Apple","Mobile"]:"iOS",
#                    ["Google","Mobile"]:"Android",
#                    ["Google","Computer"]:"ChromeOS",
#                    ["Microsoft","Computer"]:"Windows"}


software_products = {("Apple", "Mobile"): "iOS",
                     ("Google", "Mobile"): "Android",
                     ("Google", "Computer"): "ChromeOS",
                     ("Microsoft", "Computer"): "Windows"}
print(software_products)
print()
print(software_products[("Microsoft", "Computer")])
print()


word = "Management"
print(word[2])
print()
print(word[-1])
print()
print(word[0:3])
print()
print(word[-7:-4])
print()
print(word[6:])
print()
sentence = "The dog, which was brown in color, jumped over the wall."
word_list = sentence.split()
print(word_list)
print()
phrase_list = sentence.split("b")
print(phrase_list)
print()
sentence_new = " ".join(word_list)
print(sentence_new)
print()


word = "apple"
print(word)
print("{} address is:{} ".format(word, id(word)))

word = "orange"
print(word)
print("{} address is:{} ".format(word, id(word)))

#word[2] = 'A'
# print(word)

num = 1
print("{} address is:{} ".format(num, id(num)))

num = 99
print("{} address is:{} ".format(num, id(num)))

list1 = [1, 2, 3, 4, 5]
print("{} address is:{} ".format(list1, id(list1)))
list1 = [6, 2, 3, 4, 5]
print("{} address is:{} ".format(list1, id(list1)))

list1[0] = 6
print("{} address is:{} ".format(list1, id(list1)))
#
list2 = list1
print("{} address is:{} ".format(list2, id(list2)))

list3 = list1.copy()
print("{} address is:{} ".format(list3, id(list3)))
