def solution(numbers):
    lst = []
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            lst.append(numbers[i] + numbers[j])
    lst = sorted(set(lst))
    print(lst)
numbers = [2,1,3,4,1]
solution(numbers)

