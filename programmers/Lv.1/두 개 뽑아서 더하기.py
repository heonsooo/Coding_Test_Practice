def solution(numbers):
    answer = []
    if len(numbers) >= 2 and len(numbers) <=100:
        for ii in numbers : 
            if ii >= 0 and ii <=100 :
                
                for i in numbers:
                    n = numbers.index(i)
                    

                    for j in numbers[n+1:]:
                        a = i+j
                        if a not in answer:
                                
                            answer.append(a)
                        else : 
                            continue
            else :
                break

        answer.sort()
        # print(answer)
    return answer

solution([5,9,15,49,2,47,4])
