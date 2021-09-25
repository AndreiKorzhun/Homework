# Task 4.1
def func(text):
    txt = ""
    for char in text:
        if char == "\"":
            char = "\'"
        elif char == "\'":
            char = "\""
        txt += char
    return txt


# Task 4.2
def chech_palindrom(text):
    txt = ""
    for char in text:
        if char.isdigit() or char.isalpha():
            txt += char.lower()
    return txt == txt[::-1]


# Task 4.3
def split_copy(text, sep=None, maxsplit=-1):
    lst = []
    if sep is None:
        [lst.append(char) for char in text[:maxsplit]]
    else:
        prev_ind = 0
        count_sep = 0
        for ind, char in enumerate(text):
            if count_sep == maxsplit:
                break
            if char == sep:
                lst.append(text[prev_ind:ind])
                prev_ind = ind + 1
                count_sep += 1
        lst.append(text[prev_ind:])

    return lst


# Task 4.4
def split_by_index(text, indices):
    lst = []
    prev_ind = 0
    for index in indices:
        if index > len(text):
            break
        lst.append(text[prev_ind:index])
        prev_ind = index
    lst.append(text[prev_ind:])
    return lst


# Task 4.5
def get_digits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    digits.reverse()
    return tuple(digits)


# Task 4.6
def get_shortest_word(text):
    lst = text.split(" ")
    ind_max = 0
    for ind in range(len(lst)):
        if len(lst[ind]) > len(lst[ind_max]):
            ind_max = ind
    return lst[ind_max]


# Task 4.7
def foo(lst):
    lst_out = []
    for i in range(len(lst)):
        result = 1
        for ind, num in enumerate(lst):
            if ind == i:
                continue
            result *= num
        lst_out.append(result)
    return lst_out


# Task 4.8
def get_pairs(lst):
    lst_out = []
    first_num = lst[0]
    for num in lst[1:]:
        lst_out.append((first_num, num))
        first_num = num
    return lst_out


# Task 4.9
import string
test_strings = ["hello", "world", "python"]


def test_1(*strings):
    result = set()
    for char in strings[0]:
        flags = []
        for string in strings:
            if char in string:
                flag = True
            else:
                flag = False
            flags.append(flag)
        if all(flags):
            result.add(char)
    return result


def test_2(*strings):
    result = set()
    for string in strings:
        for char in string:
            result.add(char)
    return result


def test_3(*strings):
    result = set()
    for char in strings[0]:
        flags = []
        for string in strings:
            if char in string:
                flag = True
            else:
                flag = False
            flags.append(flag)
        if flags.count(True) >= 2:
            result.add(char)
    return result



def test_4(*strings):
    alph = list(string.ascii_lowercase)
    for word in strings:
        for char in word:
            if char in alph:
                alph.remove(char)
    return set(alph)


# Task 4.10
def generate_squares(num):
    d = {i: i**2 for i in range(1,num+1)}
    return d


#Task 4.11
def combine_dicts(*args):
    result_dict = {}
    for arg in args:
        for key, value in arg.items():
            if key not in result_dict:
                result_dict[key] = value
            else:
                result_dict[key] += value
    return result_dict
