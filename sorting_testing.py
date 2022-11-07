import math
import random
import time
# import matplotlib.pyplot as plt


def Insertion_Sort(array):
    for j in range(len(array)):
        key = array[j]
        i = j - 1

        while i > 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1

        array[i + 1] = key


def Merge(array, p, q, r):  # p = first index, q = middle of array, r = last index
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(0, n1):  # Get left half of array
        L[i] = array[i]

    for j in range(0, n2):  # Get right half of array
        R[j] = array[q + j + 1]

    L[n1] = math.inf  # Last index for left = sentinel value
    R[n2] = math.inf  # Last index for right = sentinel value

    i = j = 0

    for k in range(p, r + 1):  # Merge arrays

        if L[i] <= R[j]:
            array[k] = L[i]
            i = i + 1

        else:
            array[k] = R[j]
            j = j + 1


def Merge_Sort(array, p, r):
    if p < r:
        q = math.floor((p + r) / 2)  # Middle of array (roughly)
        Merge_Sort(array, p, q)  # Call merge_sort on left half of array
        Merge_Sort(array, q + 1, r)  # Call merge_sort of right half of array
        Merge(array, p, q, r)  # Merge sorted sub_arrays


# ------------------------Build arrays to sort------------------------ #
x = [100, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]

array1_set1 = [0] * x[0]
array1_set2 = [0] * x[1]
array1_set3 = [0] * x[2]
array1_set4 = [0] * x[3]
array1_set5 = [0] * x[4]
array1_set6 = [0] * x[5]
array1_set7 = [0] * x[6]
array1_set8 = [0] * x[7]
array1_set9 = [0] * x[8]
array1_set10 = [0] * x[9]

for a in range(0, x[0]):
    random_num = random.randrange(500)
    array1_set1[a] = random_num

array2_set1 = array1_set1

for a in range(0, x[1]):
    random_num = random.randrange(500)
    array1_set2[a] = random_num

array2_set2 = array1_set2

for a in range(0, x[2]):
    random_num = random.randrange(500)
    array1_set3[a] = random_num

array2_set3 = array1_set3

for a in range(0, x[3]):
    random_num = random.randrange(500)
    array1_set4[a] = random_num

array2_set4 = array1_set4

for a in range(0, x[4]):
    random_num = random.randrange(500)
    array1_set5[a] = random_num

array2_set5 = array1_set5

for a in range(0, x[5]):
    random_num = random.randrange(500)
    array1_set6[a] = random_num

array2_set6 = array1_set6

for a in range(0, x[6]):
    random_num = random.randrange(500)
    array1_set7[a] = random_num

array2_set7 = array1_set7

for a in range(0, x[7]):
    random_num = random.randrange(500)
    array1_set8[a] = random_num

array2_set8 = array1_set8

for a in range(0, x[8]):
    random_num = random.randrange(500)
    array1_set9[a] = random_num

array2_set9 = array1_set9

for a in range(0, x[9]):
    random_num = random.randrange(500)
    array1_set10[a] = random_num

array2_set10 = array1_set10

# ------------------------End building arrays to sort------------------------ #
# Get times it takes for insert sort to run on all arrays first
# array1_set(n) is used for insertion sort, array2_set(n) merge sort
insert_sort_times = [0] * 10
merge_sort_times = [0] * 10
print("-----Insertion Sort-----")

print("Sorting Set 1")
curr_time = time.time()
Insertion_Sort(array1_set1)
end_time = time.time()
total_time = end_time - curr_time
insert_sort_times[0] = total_time

print("Sorting Set 2")
curr_time = time.time()
Insertion_Sort(array1_set2)
end_time = time.time()
total_time = end_time - curr_time
insert_sort_times[1] = total_time

print("Sorting Set 3")
curr_time = time.time()
Insertion_Sort(array1_set3)
end_time = time.time()
total_time = end_time - curr_time
insert_sort_times[2] = total_time

print("Sorting Set 4")
curr_time = time.time()
Insertion_Sort(array1_set4)
end_time = time.time()
total_time = end_time - curr_time
insert_sort_times[3] = total_time

print("Sorting Set 5")
curr_time = time.time()
Insertion_Sort(array1_set5)
end_time = time.time()
total_time = end_time - curr_time
insert_sort_times[4] = total_time

print("Sorting Set 6")
curr_time = time.time()
Insertion_Sort(array1_set6)
end_time = time.time()
total_time = end_time - curr_time
insert_sort_times[5] = total_time

print("Sorting Set 7")
curr_time = time.time()
Insertion_Sort(array1_set7)
end_time = time.time()
total_time = end_time - curr_time
insert_sort_times[6] = total_time

print("Sorting Set 8")
curr_time = time.time()
Insertion_Sort(array1_set8)
end_time = time.time()
total_time = end_time - curr_time
insert_sort_times[7] = total_time

print("Sorting Set 9")
curr_time = time.time()
Insertion_Sort(array1_set9)
end_time = time.time()
total_time = end_time - curr_time
insert_sort_times[8] = total_time

print("Sorting Set 10")
curr_time = time.time()
Insertion_Sort(array1_set10)
end_time = time.time()
total_time = end_time - curr_time
insert_sort_times[9] = total_time

print("\n---Insert sort times---")
print(insert_sort_times)

'''
plt.plot(x, insert_sort_times)
plt.xlabel("# of items being sorted")
plt.ylabel("Time taken to sort (seconds)")
plt.title("Insertion Sort Times")
plt.show()
'''

print("\n-----Merge Sort-----")
print("Sorting Set 1")
curr_time = time.time()
Merge_Sort(array2_set1, 0, len(array2_set1) - 1)
end_time = time.time()
total_time = end_time - curr_time
merge_sort_times[0] = total_time

print("Sorting Set 2")
curr_time = time.time()
Merge_Sort(array2_set2, 0, len(array2_set2) - 1)
end_time = time.time()
total_time = end_time - curr_time
merge_sort_times[1] = total_time

print("Sorting Set 3")
curr_time = time.time()
Merge_Sort(array2_set3, 0, len(array2_set3) - 1)
end_time = time.time()
total_time = end_time - curr_time
merge_sort_times[2] = total_time

print("Sorting Set 4")
curr_time = time.time()
Merge_Sort(array2_set4, 0, len(array2_set4) - 1)
end_time = time.time()
total_time = end_time - curr_time
merge_sort_times[3] = total_time

print("Sorting Set 5")
curr_time = time.time()
Merge_Sort(array2_set5, 0, len(array2_set5) - 1)
end_time = time.time()
total_time = end_time - curr_time
merge_sort_times[4] = total_time

print("Sorting Set 6")
curr_time = time.time()
Merge_Sort(array2_set6, 0, len(array2_set6) - 1)
end_time = time.time()
total_time = end_time - curr_time
merge_sort_times[5] = total_time

print("Sorting Set 7")
curr_time = time.time()
Merge_Sort(array2_set7, 0, len(array2_set7) - 1)
end_time = time.time()
total_time = end_time - curr_time
merge_sort_times[6] = total_time

print("Sorting Set 8")
curr_time = time.time()
Merge_Sort(array2_set8, 0, len(array2_set8) - 1)
end_time = time.time()
total_time = end_time - curr_time
merge_sort_times[7] = total_time

print("Sorting Set 9")
curr_time = time.time()
Merge_Sort(array2_set9, 0, len(array2_set9) - 1)
end_time = time.time()
total_time = end_time - curr_time
merge_sort_times[8] = total_time

print("Sorting Set 10")
curr_time = time.time()
Merge_Sort(array2_set10, 0, len(array2_set10) - 1)
end_time = time.time()
total_time = end_time - curr_time
merge_sort_times[9] = total_time

print("\n---Merge Sort Times---")
print(merge_sort_times)

difference_between_times = [0] * 10

for i in range(0, 10):
    difference_between_times[i] = insert_sort_times[i] - merge_sort_times[i]

print("\nWhen is Merge Sort faster?")
print(x)
print(difference_between_times)



# These lines plot insertion sort times against merge sort. Uncomment and run with Anaconda or with matplotlib installed
'''
plt.plot(x, merge_sort_times)
plt.xlabel("# of items being sorted")
plt.ylabel("Time taken to sort (seconds)")
plt.title("Merge Sort Times")
plt.show()

plt.plot(x, insert_sort_times, label="Insertion Sort")
plt.plot(x, merge_sort_times, label="Merge Sort")
plt.xlabel("# of items being sorted")
plt.ylabel("Time taken to sort (seconds)")
plt.title("Merge Sort vs. Insertion Sort Times")
plt.legend()
plt.show()
'''
