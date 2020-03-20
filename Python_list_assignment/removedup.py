#remove duplicate from list
l=[1,4,3,4,2,4,2,1,6]
temp_l=[]
for i in l:
    if(i not in temp_l):
        temp_l.append(i)
print('orignal list is : ',l)
l=temp_l
print('unique_list is : ',l)

