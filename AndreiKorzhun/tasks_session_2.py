# Task 1.1
def length(line=""):
    """ Returns the number of characters in the string. """
    if isinstance(line, str):
        count = 0
        for i in line:
            count += 1
        return count
    else:
        print("Please, enter the string")


# Task 1.2
line = input("Task 1.2: Enter a string ").lower()
d = {}
for char in line:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1

print(d)


# Task 1.3.1
s = input("Task1.3.1: Enter a string like a list ").strip("[]")
lst = s.replace("'", "").split(", ")
lst = sorted(set(lst))

print(lst)


# Task 1.3.2
num = int(input("Task 1.3.2: Enter a number "))
divisors = set()
for i in range(1, num//2+1):
    if num % i == 0:
        divisors.add(i)
divisors.add(num)

print(divisors)


# Task 1.4
d = {'ab':'ba', 'aa':'aa', 'bb':'bb', 'ba':'ab'}
sorted_dict = {}
for key in sorted(d):
    sorted_dict[key] = d[key]

print(sorted_dict)


# Task 1.5
lst = [{"V":"S001"}, {"V":"S002"}, {"VI":"S005"}, {"V":"S005"}, {"VI":"S009"}, {"V":"S007"}]
values = set()

for dict in lst:
    for value in dict.values():
        values.add(value)

print(values)


# Task 1.6.1
values = (1, 2, 3, 4)
str_values = "".join(str(i) for i in values)
int_values = int(str_values)

print(int_values)


# Task 1.6.2
lst = []
for i in range(4):
    lst.append(input("Enter a number "))
a, b, c, d = (int(i) for i in lst)

for i in range(a-1, b+1):
    # Where i is the line
    for j in range(c-1, d+1):
        # Where j is the column
        if i == a-1:
            if j == c-1:
                print(" ", end=" ")
            else:
                print(j, end=" ")
        elif j == c-1:
            print(i, end=" ")
        else:
            print(i*j, end=" ")

    print()
