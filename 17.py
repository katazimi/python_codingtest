from collections import deque

def solution(cards1, cards2, goal):
    queue = deque()
    cards1_queue = deque(cards1)
    cards2_queue = deque(cards2)
    goal_queue = deque(goal)
    result = ""
    
    for i in range(len(goal)):
        if len(cards1_queue) > 0:
            word1 = cards1_queue.popleft()
        if len(cards2_queue) > 0:
            word2 = cards2_queue.popleft()
        if len(goal_queue) > 0:
            word3 = goal_queue.popleft()

        if word3 == word1:
            queue.append(word1)
            goal_queue.append(word3)
            cards2_queue.appendleft(word2)
        
        elif word3 == word2:
            queue.append(word2)
            goal_queue.append(word3)
            cards1_queue.append(word1)
        
        elif word3 != word1 and word3 != word2:
            result = "No"
        
    if result != "No":
        result = "Yes"
    
    print(result)

cards1 = ["i", "water", "drink"]
#cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
solution(cards1, cards2, goal)