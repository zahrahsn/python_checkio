# Creating a bubble sort function
def bubble_sort(lis):
    # Outer loop for traverse the entire list
    for i in range(len(lis)- 1):
        for j in range(len(lis) - 1):
            if (lis[j] > lis[j + 1]):
                temp = lis[j]
                lis[j] = lis[j + 1]
                lis[j + 1] = temp
    return lis


lis = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", lis)
# Calling the bubble sort function
print("The sorted list is: ", bubble_sort(lis))