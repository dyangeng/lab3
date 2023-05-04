import Lab3

print("Test_Lab3")
def len_checker(arr):
    n = len(arr)
    if n > 10:
        return 1
    elif n == 0:
        return 0
    else:
        return 2

def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]
    len_checker(input_arr)
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]
    len_checker(input_arr)
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    len_checker(input_arr)
    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

