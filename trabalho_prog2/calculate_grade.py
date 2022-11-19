def calculate_grade_with_bonus(grades: tuple, absences: int ) -> int:
    MAXIMUM_GRADE = 100
    grade_without_bonus = calculate_grade_without_bonus(grades)
    final_grade = grade_without_bonus + calculate_bonus(absences)

    if final_grade > MAXIMUM_GRADE:
        final_grade = 100
    
    return final_grade

def calculate_grade_without_bonus(grades: tuple) -> int:
    final_grade = sum(grades)
    return final_grade

def calculate_bonus(absences: int) -> int:
    if absences == 0:
        bonus = 2
    else:
        bonus = 0
    
    return bonus
