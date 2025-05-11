def mth_to_last_element(arr, m):
    if m < 1 or m > len(arr):
        raise ValueError("m is out of bounds")
    sorted_arr = sorted(arr)
    return sorted_arr[-m]


result = mth_to_last_element(arr=[10, 4, 6, 2, 9, 1], m=3  )
print("m-th to the last element:", result)