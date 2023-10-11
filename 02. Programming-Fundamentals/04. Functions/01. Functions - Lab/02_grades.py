def result_of_grade(grade: float) -> str:
    output = ""
    if 2 <= grade <= 2.99:
        output = "Fail"
    elif 3 <= grade <= 3.49:
        output = "Poor"
    elif 3.50 <= grade <= 4.49:
        output = "Good"
    elif 4.50 <= grade <= 5.49:
        output = "Very Good"
    elif 5.50 <= grade <= 6.00:
        output = "Excellent"

    return output


input_gardes = float(input())
print(result_of_grade(input_gardes))
