#!/usr/bin/env python
# coding: utf-8

# In[1]:


def solution(s):
    words = s.lower().split(' ')
    result = []

    for word in words:
        answer=[]
        for i in range(len(word)):
            if i%2 ==0:
                if word[i].isdigit() :
                    answer.append(word[i])
                else:        
                    answer.append(word[i].upper())
            else:
                answer.append(word[i].lower())
                

        result.append(''.join(answer))
        
    result = ' '.join(result)
    return str(result)
print(solution("try hello world"))

