#remove value 4 from the list
l=[1,2,3,4,5,4,6,4]
temp_l=[]
#create a temp list and add element from orignal list only when value is not '4'
for i in l:
    if (i!=4):
        temp_l.append(i)
print('orignal list is : ',l)
l=temp_l
print('new list is : ',l)
