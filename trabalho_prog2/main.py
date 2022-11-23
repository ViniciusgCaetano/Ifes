import pickle
from mergeSort import mergeSort
from binary_search import buscaBin

with open('entrada.bin', 'rb') as arq:
    """
    Realizar a leitura do arquivo e armazenar em um dicionário 
    e em uma lista com apenas as matrículas.
    """
    dict_classroom = pickle.load(arq)
    list_of_registrations = list(dict_classroom.keys())

mergeSort(list_of_registrations, dict_classroom) #Realizar Merge Sort da lista de matrículas.

notas = []
with open('saida.txt', 'w') as arq:
    """
    Realizar escrita no arquivo saída.txt
    Criar lista apenas com as notas
    """
    for code in list_of_registrations:
        registration = dict_classroom[code]

        total_grade = sum(registration[2])
        if (registration[3] > 0) or ((total_grade) >= 100):
            
            arq.write(f'{registration[0]} - {sum(registration[2])}\n')
        else:
            
            total_grade = sum(registration[2]) + 2
            if total_grade == 101:
                arq.write(f'{registration[0]} - {sum(registration[2])} + 1\n')    
            else:
                arq.write(f'{registration[0]} - {sum(registration[2])} + 2\n')


        notas.append(total_grade)

print(buscaBin(59.5, notas)) 
