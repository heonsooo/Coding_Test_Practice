
array = [6,8,0,1,3,5,74,3,7,85,36]
# print(type(array))

for i in range(len(array)):
    currrent_index = i
   
    for j in range(i+1,len(array)):
        if array[currrent_index] > array[j]:
            currrent_index = j
            
            
    if array[i] != array[currrent_index]:
        array[i], array[currrent_index] = array[currrent_index], array[i],

        print(array)

print('최종 배열 :', array)