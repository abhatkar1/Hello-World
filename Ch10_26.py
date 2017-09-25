# (Merge two sorted lists) Write the following function that merges two sorted lists
# into a new sorted list:
# def merge(list1, list2):
# Implement the function in a way that takes len(list1) + len(list2) comparisons.
# Write a test program that prompts the user to enter two
# sorted lists and
# displays
# the merged
# list. Here is a sample run:
#
# Enter list1: 1 5 16 61 111
# Enter list2: 2 4 5 6
# The merged list is 1 2 4 5 5 6 16 61 111

# Logic:
# In merge function, you compare first element of list1 with first element of list2 and add the smaller element
# to the new list and increment counter for the same list keeping the counter for other list same.
# In the end, we add the remaining elements of one of the lists to the new list.

def merge(list1, list2):
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i += 1
        else:
            list3.append(list2[j])
            j += 1

    if i < len(list1):
        list3.extend(list1[i:])
    elif j < len(list2):
        list3.extend(list2[j:])

    return list3

def test():
    list1 = [eval(x) for x in input("Enter sorted list1 separated by space:").split()]

    list2 = [eval(x) for x in input("Enter sorted list2 separated by space:").split()]

    mergedList = merge(list1, list2)

    print(mergedList)

test()