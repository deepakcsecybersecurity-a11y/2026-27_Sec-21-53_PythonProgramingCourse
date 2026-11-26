def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(name="Rahul", Python=90, Java=85, HTML=95)