#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(s):
    
    # count : 변환횟수, zero : 0의 개수
    count, zero= 0,0
    while True:
        
        # 1의 개수
        num = s.count('1')
        #변환 횟수 +1 
        count += 1
        
        # zero 개수 더하기
        zero += len(s)-num
        
        # 변환 후 문자열
        s = bin(num)[2:]
        if s == '1':
            break
    return [count,zero]

