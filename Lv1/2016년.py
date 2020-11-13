def solution(a, b):
    
    Day = []
    day_alpha= ['SUN','MON','TUE','WED','THU','FRI','SAT']                               
    last_day = [31,29,31,30,31,30,31,31,30,31,30,31]         
      

    # 각 달의 시작 요일 설정해놓기. 
      #여기서 k는 나중에 요일을 설정할 때 사용합니다.
    if  a == 5 :                       
        k = 0
    elif a == 2 or a == 8  :             
        k = 1
    elif a == 3 or a == 11 :            
        k = 2
    elif a == 6  :                       
        k = 3
    elif a == 12 or a == 9  :            
        k = 4
    elif a == 1 or a == 4 or a==7  :     
        k = 5
    elif a == 10 :                        
        k = 6     
    
    #첫 째날에 1일 부터 7일 간격으로 채워넣기.
    for i in range(1, last_day[a-1]+1, 7):
        Day.append(i)                  

    # j = [1일 8일 15일 22일 29일]과 입력 날짜(b)와 비교하여 
    # j 의 element와 하나씩 비교
    #  j > b 이면 다음 j 호출
    #  j == b 이면, 그 날짜의 요일 호출
    #  j < b 이면, j에서 1씩 줄이면서 b와 비교하고 j==b 가 될때의 요일을 호출
    for j in Day:
        answer = ''
        if j == b :            
            answer = day_alpha[k]

        elif j > b :
            count = 0
            while j > b:
                j -= 1
                count += 1

            answer = day_alpha[k-count]
            break
   
        elif b == 30 :
            if k <= 5 : 
                
                answer = day_alpha[k+1]
            elif k == 6:
                k = 0
                answer = day_alpha[0]
        elif b == 31 :
            if k <= 4 :
                k +=2 
                answer = day_alpha[k]
            elif k >= 5 :
                answer = day_alpha[k-5]





        else:
            continue

    return answer

    



/
