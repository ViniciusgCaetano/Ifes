import pickle
from is_ahead import is_ahead

with open('bins/entrada100000.bin', 'rb') as arq:
    dict_classroom = pickle.load(arq)
    list_of_registrations = list(dict_classroom.items())


# n = len(list_of_registrations)
# for i in range(n):
#     for j in range(0,n-1):
#         if not is_ahead(list_of_registrations[j], list_of_registrations[j+1]):
#             list_of_registrations[j], list_of_registrations[j+1] = list_of_registrations[j+1], list_of_registrations[j]

        


def mergeSort(l):
    if len(l) > 1:
        middle = len(l) // 2
        l_left = l[:middle]
        l_right = l[middle:]

        mergeSort(l_left)
        mergeSort(l_right)

        merge(l, l_left, l_right)


def merge(l, l_left, l_right):
    i = 0
    j = 0
    k = 0

    while i < len(l_left) and j < len(l_right):
        if is_ahead(l_left[i], l_right[j]):
            l[k] = l_left[i]
            i += 1
        else:
            l[k] = l_right[j]
            j += 1
        k += 1

    while i < len(l_left):
        l[k] = l_left[i]
        i += 1
        k += 1
    
    while j < len(l_right):
        l[k] = l_right[j]
        j += 1
        k += 1

mergeSort(list_of_registrations)

print(list_of_registrations)

for i in list_of_registrations:
    if (i[1][3] > 0) and (sum(i[1][2]) <= 100):
        print(f'{i[1][0]} - {sum(i[1][2])}')
    else:
        
        total_grade = sum(i[1][2]) + 2
        if total_grade == 101:
            print(f'{i[1][0]} - {sum(i[1][2])} + 1')    
        else:
            print(f'{i[1][0]} - {sum(i[1][2])} + 2')