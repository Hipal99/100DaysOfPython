student_scores = {"Paal": 100,
                   "Tom": 60,
                   "retard": 72,
}




def score(dic):
    student_grade = {}
    for key in dic:
        if dic[key] >= 91:
            student_grade[key] = "The smartest for sure, no cap"
        elif dic[key] <= 90 and student_scores[key] >= 71:
            student_grade[key] = "As expected of a retard?"
        elif dic[key] <= 70:
            student_grade[key] = "Less than a retard OMEGALOL"
    print(student_grade)

score(student_scores)