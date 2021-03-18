def get_best_student(students):
    best_student = None
    best = 0
    for name, scores in students.items():
        average = sum(scores) / len(scores)
        if average >= best:
            best = average
            best_student = name
    return best_student

print(get_best_student({
    "John": [100, 90, 80], 
    "Peter": [100, 70, 80]
})) # prints "John"

print(get_best_student({
    "Susan": [67, 84, 75, 63], 
    "Mike": [87, 98, 64, 71], 
    "Jim": [90, 58, 73, 86]
})) # prints "Mike"
