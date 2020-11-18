def solution(answers):
    answer = []
    a_1 = [1,2,3,4,5]
    b_1 = [2,1,2,3,2,4,2,5]
    c_1 = [3,3,1,1,2,2,4,4,5,5]

    a_11 , b_11, c_11 = [], [], []

    while len(a_11) <= 10000-5:
        for i in a_1:
            a_11.append(i)

    while len(b_11) <= 10000-8:
        for i in b_1:
            b_11.append(i)

    while len(c_11) <= 10000-5:
        for i in c_1:
            c_11.append(i)
    print(len(a_11),len(b_11),len(c_11))
    count_a , count_b , count_c = 0, 0, 0
    
    for k in range(0,len(answers)):
        a ,b, c= a_11[k], b_11[k], c_11[k]
        
        if a == answers[k] :
            count_a += 1
        if b == answers[k] : 
            count_b += 1
        if c == answers[k] : 
            count_c += 1


    count = [count_a , count_b , count_c]
    

    if count[0] > count[1] : 

        if count[0] > count[2] :
            answer.append(1)
        elif count[0] == count[2] :
            answer.append(1)
            answer.append(3)
        else :
            answer.append(3)

    elif count[0] < count[1] : 

        if count[1] > count[2] :
            answer.append(2)
        elif count[1] == count[2] :
            answer.append(2)
            answer.append(3)
        else :
            answer.append(3)

    elif count[0] == count[1] : 

        if count[1] > count[2] :
            answer.append(1)
            answer.append(2)
        elif count[1] == count[2] :
            answer.append(1)
            answer.append(2)
            answer.append(3)
        else :
            answer.append(3)


    return answer

a = [1,2,3,4,5]
print(solution(a))
