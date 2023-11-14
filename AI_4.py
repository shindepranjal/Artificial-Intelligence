
# Pranjali Shinde(TA63)  Experiment 4: Selection Sort

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


user_input = input("Enter a list of integers separated by spaces: ")
arr = [int(x) for x in user_input.split()]
selection_sort(arr)
print("Sorted array is:", arr)
