def solution(array, commands):
    answer = []
    n = len(commands)                           #command가 몇 개 일지 모르기 때문에 모든 command 포함하기 위하여 개수 파악
    for nn in range(0,n):                       #첫 번째 command부터 n번째(맨 끝 커맨드)까지 차례대로 진행
        
        i = commands[nn][0]-1                   #list의 index 는 0부터 시작하기때문에 -1을 더해줌
        j = commands[nn][1]                     

        sol = array[i:j]                        # i번째 부터 j번째 까지 array 자르기 
        sol = sorted(sol)                       # 자른 array를 오름차순으로 정렬
        soll = sol[commands[nn][2]-1]           # 정렬 된 array에서 k번째 수 soll에 저장
        answer.append(soll)                     # 저장 된 k번째 수 answer에 append 
        

    
    return answer
