# Task 1: Fill array
def fill_array(n):
    arr = []
    print("Enter the elements: ")
    for _ in range(n):
        arr.append(int(input()))
    return arr

# Task 2: Find max & min
def find_max_min(arr):
    max = arr[0]
    min = arr[0]
    for x in arr[1:]:
        if x > max:
            max = x
        if x < min:
            min = x
    return max, min

# Task 3: Print results
def print_results(max, min):
    print("Max:", max)
    print("Min:", min)


print("Enter the size of the array: ")
n = int(input())
arr = fill_array(n)
max, min = find_max_min(arr)
print_results(max, min)


#Complexity
#Time: O(n)
#Space: O(n)
