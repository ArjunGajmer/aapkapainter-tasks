#Write a code that prints out the first occurrence of a duplicate in a given array of integers

def first_duplicate_occurance(arr):
    mp = {}
    for index, element in enumerate(arr):
        if mp.get(element):
            return element
        mp[element] = index + 1
    return None

arr = [1, 2, 3,4, 4]
assert first_duplicate_occurance(arr) == 4

arr = [1, 2, 2,4, 4, 1]
assert first_duplicate_occurance(arr) == 2

arr = []
assert first_duplicate_occurance(arr) is  None

arr = [1, 1, 2, 3,4, 4]
assert first_duplicate_occurance(arr) == 1

arr = [1, 5, 3,4, 5, 4, ]
assert first_duplicate_occurance(arr) == 5
