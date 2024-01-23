def solution(lst):
    unique_list = list(set(lst))
    unique_list.sort(reverse=True)
    print(unique_list)
lst = [4,2,2,1,3,4]
solution(lst)
