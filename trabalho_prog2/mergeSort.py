from is_ahead import is_ahead

def mergeSort(l, dict_classroom):
    if len(l) > 1:
        middle = len(l) // 2
        l_left = l[:middle]
        l_right = l[middle:]

        mergeSort(l_left, dict_classroom)
        mergeSort(l_right, dict_classroom)

        merge(l, l_left, l_right, dict_classroom)


def merge(l, l_left, l_right, dict_classroom):
    i = 0
    j = 0
    k = 0

    while i < len(l_left) and j < len(l_right):
        if is_ahead(l_left[i], l_right[j], dict_classroom): #is_ahead recebe duas matrículas e diz qual deveria estar na frente da outra.
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