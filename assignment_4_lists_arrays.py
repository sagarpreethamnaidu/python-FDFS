# =========================================================
# Assignment-4: Lists (Arrays) in Python
# =========================================================




# =========================================================
# 1. Sum of Elements
# =========================================================

print("1. Sum of Elements")


def sum_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total

nums = [10, 20, 30, 40]
print(sum_elements(nums))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 2. Average of Elements
# =========================================================

print("2. Average of Elements")


def average(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst)

nums = [10, 20, 30, 40]
print(average(nums))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 3. Find Index of an Element
# =========================================================

print("3. Find Index of an Element")

lst = [10, 20, 30, 40]
element = 30

if element in lst:
    print("Index:", lst.index(element))
else:
    print("Element not found")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 4. Check Element Presence
# =========================================================

print("4. Check Element Presence")


def contains(lst, value):
    return value in lst

nums = [10, 20, 30]
print(contains(nums, 20))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 5. Remove an Element
# =========================================================

print("5. Remove an Element")


def remove_element(lst, value):
    if value in lst:
        lst.remove(value)
    return lst

nums = [10, 20, 30, 40]
print(remove_element(nums, 20))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 6. Copy a List
# =========================================================

print("6. Copy a List")


def copy_list(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
    return new_list

nums = [1, 2, 3]
print(copy_list(nums))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 7. Insert Element at Position
# =========================================================

print("7. Insert Element at Position")


def insert_element(lst, index, value):
    lst.insert(index, value)
    return lst

nums = [10, 20, 40]
print(insert_element(nums, 2, 30))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 8. Find Minimum and Maximum
# =========================================================

print("8. Find Minimum and Maximum")


def min_max(lst):
    minimum = min(lst)
    maximum = max(lst)
    return minimum, maximum

nums = [5, 8, 2, 10]
print(min_max(nums))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 9. Reverse a List
# =========================================================

print("9. Reverse a List")


def reverse_list(lst):
    return lst[::-1]

nums = [1, 2, 3, 4]
print(reverse_list(nums))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 10. Find Duplicate Elements
# =========================================================

print("10. Find Duplicate Elements")


def find_duplicates(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

nums = [1, 2, 3, 2, 4, 1]
print(find_duplicates(nums))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 11. Count Even and Odd Numbers
# =========================================================

print("11. Count Even and Odd Numbers")


def count_even_odd(lst):
    even = 0
    odd = 0

    for num in lst:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd

nums = [1, 2, 3, 4, 5, 6]
print(count_even_odd(nums))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 12. Common Elements Between Two Lists
# =========================================================

print("12. Common Elements Between Two Lists")

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = []

for item in list1:
    if item in list2:
        common.append(item)

print(common)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 13. Remove Duplicates
# =========================================================

print("13. Remove Duplicates")


def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

nums = [1, 2, 2, 3, 4, 4]
print(remove_duplicates(nums))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 14. Second Largest Element
# =========================================================

print("14. Second Largest Element")


def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2]

nums = [10, 20, 30, 40, 50]
print(second_largest(nums))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 15. Difference Between Max and Min
# =========================================================

print("15. Difference Between Max and Min")


def difference(lst):
    return max(lst) - min(lst)

nums = [5, 10, 20, 30]
print(difference(nums))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 16. Check for Specific Elements
# =========================================================

print("16. Check for Specific Elements")


def check_values(lst):
    return 12 in lst and 23 in lst

nums = [5, 12, 23, 40]
print(check_values(nums))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 17. Unique Elements Only
# =========================================================

print("17. Unique Elements Only")


def unique_elements(lst):
    unique = []
    for item in lst:
        if lst.count(item) == 1:
            unique.append(item)
    return unique

nums = [1, 2, 2, 3, 4, 4, 5]
print(unique_elements(nums))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 18. Frequency Count
# =========================================================

print("18. Frequency Count")


def frequency(lst):
    freq = {}

    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    return freq

nums = [1, 2, 2, 3, 3, 3]
print(frequency(nums))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 19. List Sorting Without Built-in Functions
# =========================================================

print("19. List Sorting Without Built-in Functions")


def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst

nums = [5, 2, 9, 1, 6]
print(bubble_sort(nums))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 20. Merge Two Lists Without Duplicates
# =========================================================

print("20. Merge Two Lists Without Duplicates")


def merge_lists(list1, list2):
    result = []

    for item in list1:
        if item not in result:
            result.append(item)

    for item in list2:
        if item not in result:
            result.append(item)

    return result

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print(merge_lists(list1, list2))

print("\n" + "=" * 50 + "\n")
