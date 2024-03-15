def print_grade(mark):
    if mark >= 80:
        print("High Distinction")
        return
    if mark >= 70:
        print("Distinction")
        return
    if mark >= 60:
        print ("Credit")
        return
    if mark >= 50:
        print ("Pass")
        return
    else:
        print ("Fail")
