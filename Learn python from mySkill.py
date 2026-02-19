## Common Data Structure: List in Python

my_list = []
print("Initial list:", my_list)

my_list = [1,'ady',3.5,True]
print("List after adding elements:", my_list)
print("Length of the list:", len(my_list))
print("First element:", my_list[1])
print("Last element:", my_list[-1])
print("Sliced list (1 to 3):", my_list[1:3])
my_list[1] = 'python'
print("List after updating second element:", my_list)
my_list.append('new element')
print("List after appending an element:", my_list)


## Common Data Structure: Dictionary in Python

my_dict = {"name": "ady", "age": 25, "is_student": True}

print("Initial dictionary:", my_dict)
print("Value for 'name':", my_dict["name"])
my_dict["age"] = 26
print("Dictionary after updating age:", my_dict)


## Common Data Structure: Tuple in Python

my_tuple = (1, 'ady', 3.5, True)

print("Tuple:", my_tuple)
print("First element of tuple:", my_tuple[0])
print("Length of the tuple:", len(my_tuple))
print("Sliced tuple (1 to 3):", my_tuple[1:3])
print("last element of tuple:", my_tuple[-1])
print("Tuple after concatenation:", my_tuple + (False, 42))


## Common Data Structure: Set in Python

my_set = {1, 2, 3, 4, 5, 1, 2}
print("Set:", my_set)
print("Length of the set:", len(my_set))
my_set.add(6)
print("Set after adding an element:", my_set)
print("Is 3 in the set?", 3 in my_set)
my_set.add(3)
print("Set after adding duplicate element 3:", my_set)


## Example: Generating a list of odd numbers from 1 to 20 using WHILE LOOP

num = 1
odd_num = []
while num:
    if num % 2 != 0:
        odd_num.append(num)
    if num >= 20:
        break    
    num += 1
print("Odd numbers from 1 to 20:", odd_num)

## Example: Generating a list of squared numbers from 1 to 5 using FOR LOOP and LIST COMPREHENSION

my_list = [1, 2, 3, 4, 5]
squared_list = [x**2 for x in my_list]
print("Squared list using list comprehension:", squared_list)

for i in squared_list:
    print("Element in my_list:", i)


def power(x, y):
    return x ** y

result = power(2, 3)
print("2 raised to the power of 3 is:", result)


## Played with strings in Python

my_string = '''I'm Haryadi Santoso and my nickname is "Ady".'''
print('\nThe result is:')
print(my_string)

my_reversed_string = my_string[::-1]
print("\nReversed string:")
print(my_reversed_string)
print(my_string[3:7])

my_string_list=list(my_string)
my_string_list[4:11]="Heru"
print(my_string_list)
my_modified_string=''.join(my_string_list)
print("\nModified string after changing characters 4 to 9 to 'Heru':")
print(my_modified_string)

my_string1='''I'm "smart"'''
print(my_string1)

my_string2='I\'m "smart"'
print(my_string2)

my_string3="I\'m \"smart\""
print(my_string3)

my_string4="C:\\new_folder\\test.txt"
print(my_string4)

my_string5="Hi\tthere!"
print(my_string5)

my_string6="Hi\nthere!"
print(my_string6)




## More details about List in Python

my_list = []
print("Initial list:", my_list)

my_list = ["apple","banana","cherry"]
print("List after adding elements:", my_list)

my_list.append("orange")
print("List after appending an element:", my_list)

my_list.insert(1, "orange")
print("List after inserting an element at index 1:", my_list)

my_list.pop(1)
print("List after removing element at index 1:", my_list)

my_tuple = ("kiwi", "mango")
my_list.extend(my_tuple)
print("List after extending with a tuple:", my_list)

i=0
while i < len(my_list):
    print("Element at index", i, "is", my_list[i])
    i += 1

## List comprehension to filter elements containing the letter 'a'
print([x for x in my_list if "a" in x])

## List comprehension to convert all elements to uppercase
print([x.upper() for x in my_list])

## List comprehension to convert non-empty elements to uppercase
print([x.upper() for x in my_list if x != "banana"])




myList = [1,5,4,8,3,15,12,7,10,6,9,11,14,2,13]

new_list = list(filter(lambda x: x % 2 == 0, myList))
print("Even numbers from the list:", new_list)

new_list2 = list(filter(lambda x: x % 2 != 0, myList))
print("Odd numbers from the list:", new_list2)

new_list3 = list(map(lambda x: x * 2, myList))
print("List with elements multiplied by 2:", new_list3)