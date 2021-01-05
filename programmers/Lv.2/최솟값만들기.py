def solution(A,B):
    answer = []
    A.sort()
    B.sort(reverse =True)
    for _ in range(len(A)):
        result = A.pop()*B.pop()
        answer.append(result)
        
    return sum(answer)
print(solution([1,4,2],[5,4,4]))