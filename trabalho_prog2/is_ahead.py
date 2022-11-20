from calculate_grade import calculate_grade_without_bonus, calculate_grade_with_bonus

def is_ahead(registration_code_1, registration_code_2, dict_classroom):
    
    #recebe duas matrículas e pega as informações de cada matrícula
    m1_tuple = dict_classroom[registration_code_1]
    m2_tuple = dict_classroom[registration_code_2]

    # Pegar as informações e armazena as informações em suas respectivas variáveis
    name1, name2 = m1_tuple[0], m2_tuple[0]
    date1, date2  = m1_tuple[1], m2_tuple[1]
    year1, year2 = date1[0], date2[0]
    semester1, semester2 = date1[1], date2[1]
    grades1, grades2 = m1_tuple[2], m2_tuple[2]
    absences1, absences2 = m1_tuple[3], m2_tuple[3]

    #Comparar notas com bônus
    if calculate_grade_with_bonus(grades1, absences1) > calculate_grade_with_bonus(grades2, absences2):
        return True
    elif calculate_grade_with_bonus(grades1, absences1) < calculate_grade_with_bonus(grades2, absences2):
        return False
    
    #Comparar notas sem bônus
    if calculate_grade_without_bonus(grades1) > calculate_grade_without_bonus(grades2):
        return True
    elif calculate_grade_without_bonus(grades1) < calculate_grade_without_bonus(grades2):
        return False
    
    
    if year1 > year2:
        return True
    elif year1 < year2:
        return False
    
    #Comparar semestre
    if semester1 > semester2:
        return True
    elif semester1 < semester2:
        return False
    
    #Comparar nome
    if name1 != name2:
        ordered_names = [name1, name2]
        ordered_names.sort()
        if ordered_names[0] == name1:
            return True
        else:
            return False
    
    #Comparar matrícula
    ordered_codes = [registration_code_1, registration_code_2]
    ordered_codes.sort()
    if ordered_codes[0] == registration_code_1:
        return True
    else:
        return False
