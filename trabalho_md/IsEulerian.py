def is_eulerian(matrix):
    print(matrix)
    grades = [True for line in matrix if sum(line) //2 == 0]
    if (len(grades) == len(matrix)) or (len(grades) == len(matrix) - 2):
        print(grades)
        return True
    else:
        print(grades)
        return False