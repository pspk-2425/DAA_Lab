# Implement a linear time sorting: Count Sort
def counting_sort(arr):
    # if the arr is empty, returns empty
    if arr == []:
        return []

    # get some information about the arr
    arr_len = len(arr)
    arr_max = max(arr)
    arr_min = min(arr)

    # create the freq array
    freq_arr_length = arr_max + 1 - arr_min
    freq_arr = [0] * freq_arr_length

    # count how much a number appears in the arr
    for number in arr:
        freq_arr[number - arr_min] += 1

    # sum each position with it's predecessors. now, freq_arr[i] tells
    # us how many elements <= i has in the arr
    for i in range(1, freq_arr_length):
        freq_arr[i] = freq_arr[i] + freq_arr[i - 1]

    # create the output arr
    sorted_arr = [0] * arr_len

    # place the elements in the output, respecting the original order (stable
    # sort) from end to begin, updating freq_arr
    for i in reversed(range(0, arr_len)):
        sorted_arr[freq_arr[arr[i] - arr_min] - 1] = arr[i]
        freq_arr[arr[i] - arr_min] -= 1

    return sorted_arr


if __name__ == "__main__":
    user_input = input("Enter numbers separated by space: ").strip()
    unsorted_arr = [int(item) for item in user_input.split(" ")]
    print("sorted Order : ",end=" ")
    print(counting_sort(unsorted_arr))