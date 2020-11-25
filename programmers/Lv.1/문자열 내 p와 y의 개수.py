def solution(s):
    s = s.upper()

    num_p = s.count('p')
    num_y = s.count('y') 

    if num_p == num_y :
        answer = True
    else :
        answer = False
    return answer
