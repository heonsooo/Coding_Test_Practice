#!/usr/bin/env python
# coding: utf-8

# # 두 수 비교하기
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

# In[ ]:


a = list(map(int, input().split()))
if a[0] > a[1]:
    print('>')
elif a[0] < a[1]:
    print('<')
else:
    print('==')


# # 알람 시계
# 
# 첫째 줄에 두 정수 H와 M이 주어진다.  
# (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.  
#   
# 입력 시간은 24시간 표현을 사용한다.   
# 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다.   
# 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.  

# In[6]:


time = list(map(int,input().split()))

if time[1]<45:
    time[1] = 60+time[1]-45
    if time[0] == 0:
        time[0] = 23
    else:
        time[0]-=1
elif time[1] >= 45:
    time[1] -= 45
    
print(time[0], time[1])


# # 사분면 고르기
# 
# 예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다.  
# 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.  
# 
# 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오.  
# 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.   
# 
# 

# In[12]:


x = int(input())
y = int(input())

if x>0and y>0:
    print(1)
elif x > 0 and y < 0 :
    print(4)
    
elif x < 0 and y < 0 :
    print(3)
elif x < 0 and y > 0 :
    print(2)


# # 윤년
#  
# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.  
#   
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.  
#   
# 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다.   
# 하지만, 2000년은 400의 배수이기 때문에 윤년이다.  

# In[20]:


N = int(input())

if N%4 == 0 :
    if N%100 != 0 or N%400 ==0 :
        print(1)
    else:
        print(0)
else:
    print(0)


# # 시험 성적
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

# In[23]:


Score = int(input())

Grade = 'A' if 90 <=Score<=100 else 'B' if 80<=Score <90 else 'C' if 70<= Score<80 else 'D' if 60<=Score<70 else 'F'

print(Grade)

