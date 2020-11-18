def solution(num):
    answer = -1                             # default 값
    num < 8000000 and num >= 1              # num 조건
    a = int(num)                            
    count = 0

    while a != 0 and count <500 :
        if a % 2 == 0: 
            a = int(a/2)
            
        elif a%2 == 1 :
            a = (a*3) + 1

        count += 1
        
        if a == 1:
            answer = count
            break
        elif count > 500 : 
            break

    return answer


'''
채점 결과
정확성: 46.9
효율성: 0.0
합계: 46.9 / 50
'''
