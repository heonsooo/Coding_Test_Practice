def solution(arr, divisor):
    answer = []
    if int(divisor) > 0 and len(arr) >= 1 :
        for i in arr :
            if i % divisor == 0:
                answer.append(i)
            else :
                continue

        if len(answer) == 0:
            answer.append(-1)

    return sorted(answer)

A ,B = [5,9,7,10] , 19
print(solution(A,B))

