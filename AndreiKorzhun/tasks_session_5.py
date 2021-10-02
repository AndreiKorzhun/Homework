# Task 5.1
import os

unsorted_names = os.path.join(os.path.dirname(__file__), "..", "data", "unsorted_names.txt")
sorted_names = os.path.join(os.path.dirname(__file__),"..","data","sorted_names.txt")

with open(unsorted_names, "r") as file:
    names = sorted(file.readlines())

with open(sorted_names, "w") as file:
    for name in names:
        file.write(name)


# Task 5.2
import re
from collections import Counter


def most_common_words(filepath, number_of_words=3):
    filepath = os.path.join(os.path.dirname(__file__), "..", "data", filepath)
    with open(filepath) as file:
        text = file.read()

    # the list of words without punctuation marks
    words = [word.lower() for word in re.findall(r'\w+', text)]

    # list of tuples [(word, word count), ]
    word_counts = Counter(words).most_common(number_of_words)
    lst = []
    for i in word_counts:
        lst.append(i[0])
    return lst


# Task 5.3
import os
import csv


# 1)
def get_top_performers(filename, number_of_top_students=5):
    with open(os.path.join(os.path.dirname(__file__), "..", "data", filename)) as file:
        reader = csv.reader(file)
        students = []
        for row in reader:
            students.append(row)
        sort_students = sorted(students[1:], key=lambda student: float(student[2]), reverse=True)
    return [student[0] for student in sort_students[:number_of_top_students]]


# 2)
def write_students(filename):
    with open(os.path.join(os.path.dirname(__file__), "..", "data", filename)) as file:
        reader = csv.reader(file)
        rows = []
        for row in reader:
            rows.append(row)
    fields = rows[0]
    students = rows[1:]
    sort_students = sorted(students, key=lambda student: float(student[1]), reverse=True)

    with open(os.path.join(os.path.dirname(__file__), "..", "data", "sorted_students.csv"), "w") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(fields)
        csvwriter.writerows(sort_students)


# Task 5.4
# 1
a = "I am global variable!"
inner_function = None


def enclosing_function():
    global inner_function
    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"
        print(a)


enclosing_function()
print(inner_function())

# # 2.1
# # legb.py
# def inner_function():
#     global a
#
#
# # 2.2
# # legb.py
# def inner_function():
#     nonlocal a


# Task 5.5
from functools import reduce


def remember_result(func):
    def wrapper(*args):
        print(f"Last result = '{wrapper.last_result}'")
        current_result = func(*args)
        wrapper.last_result = current_result
        return current_result

    wrapper.last_result = None
    return wrapper


@remember_result
def sum_list(*args):
    result = reduce(lambda a, b: a + b, args)
    print(f"Current result = '{result}'")
    return result


sum_list("a", "b")
sum_list("abc", "cde")
sum_list(3, 4, 5)


# Task 5.6
def call_once(func):
    cache = dict()

    def wrapper(*args):
        if wrapper.args:
            return func(*wrapper.args)
        wrapper.args = args
        return func(*args)

    wrapper.args = None
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(13, 42))
print(sum_of_numbers(999, 100))
print(sum_of_numbers(134, 412))


# Task 5.7
"""When the module mod_с and mod_с is imported, run and initialize all variables, 
functions, etc. of the imported modules"""

"""If you replace the value of a variable in the mod_c module with a sheet, 
the value output at mod_a startup does not change, since when importing modules into mod_a, 
the mod_c module is imported first, and then the mod_b module. because mod_c.x is initialized in the mod_b module"""

"""Same idea with previous explonation"""
