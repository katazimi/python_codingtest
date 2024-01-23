def solution(answers):
    arr1 = [1,2,3,4,5]
    arr2 = [2,1,2,3,2,4,2,5]
    arr3 = [3,3,1,1,2,2,4,4,5,5]
    student1 = []
    student2 = []
    student3 = []
    highest_student = []
    score1 = 0
    score2 = 0
    score3 = 0
    for i in range(0,len(answers)):
        student1.append(arr1[i%5])
        student2.append(arr2[i%8])
        student3.append(arr3[i%10])
        if student1[i] == answers[i]:
            score1 = score1 + 1
        if student2[i] == answers[i]:
            score2 = score2 + 1
        if student3[i] == answers[i]:
            score3 = score3 + 1
    max_value = max(score1, score2, score3)
    if max_value == score1:
        highest_student.append(1)
        if max_value == score2:
            highest_student.append(2)
            if max_value == score3:
                highest_student.append(3)
    elif max_value == score2:
        highest_student.append(2)
        if max_value == score3:
            highest_student.append(3)
    elif max_value == score3:
        highest_student.append(3)
    print(highest_student)
answers = [1,3,2,4,2]
solution(answers)
    
