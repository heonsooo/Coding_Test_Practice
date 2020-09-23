def solution(s):
    li = []
    a = len(s)
    
    if a >= 1 and a <= 100 :
        li.append(s)
        if a%2 == 0 : 
            b = a//2
            
            answer = li[0][b-1] + li[0][b]

            
        else :
            b = a//2
            answer = li[0][b]
            
    return answer