students = [
    {"name": "Alice", "subject": "Mathematics", "score": 85},
    {"name": "Bob", "subject": "Computer Science", "score": 78},
    {"name": "Charlie", "subject": "Mathematics", "score": 92},
    {"name": "Diana", "subject": "Computer Science", "score": 79},
    {"name": "Eve", "subject": "Mathematics", "score": 76},
]


# def collect_scores(students): #langere versie
#     result = []
#     for student in students:
#         result.append(student["score"])
#     return result

# print(collect_scores(students))


# [student["score"] for student in students] oneliner versie



# def sorted_scores(students):
#     result = []
#     for student in students:
#         if student["score"] >= 80:
#             result.append(student)
#     return result

# print(sorted_scores(students))

# sorted_score = [student for student in students if student["score"] >= 80 ]

# print(sorted_score)

# sorted1 = [student for student in students if student["score"] >= 90 ]
# sorted2 = [student for student in students if student["subject"] == "Mathematics"]
# sorted3 = [student for student in students if student["subject"] == "Computer Science" ]
# sorted4 = [student for student in students if student["name"] == "Diana" ]


# print(sorted1)
# print(sorted2)
# print(sorted3)
# print(sorted4)


def filter_students(students, filter_function):
    return [student for student in students if filter_function(student)]

filter_1 = lambda student: student["score"] >= 90
filter_2 = lambda student: student["subject"] == "Mathematics"
filter_3 = lambda student: student["subject"] == "Computer Science"
filter_4 = lambda student: student["name"] == "Diana"

# print(filter_students(students, filter_function=filter_1))

# print(filter_students(students, filter_function=filter_2))

# print(filter_students(students, filter_function=filter_3))

# print(filter_students(students, filter_function=filter_4))

math_students = filter_students(students, filter_2)

filter_5 = sorted(math_students,key= lambda student: student["score"], reverse = True)

print(filter_5)






    

        