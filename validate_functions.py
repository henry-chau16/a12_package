
def validate_gender(gender: str):
    try:
        if gender and (gender == 'M' or gender == 'F'):
            return True
        return False
    except Exception as e:
        return False

def validate_age(age: int):
    try:
        if age and age >= 1 and age <= 100:
            return True
        return False
    except Exception as e:
        return False