#sort the list in ascending and descending order without using sort
l=[1,8,3,2,6,4,24,5]
temp=0
#ascending order ->  compare two elements in a list , push the min element towards left
#descending order -> compare two elements in a list , push the min element towards right
for j in range(0,len(l)-1):
    for i in range(0,len(l)-1):
        if(l[i]>l[i+1]):
            temp=l[i]
            l[i]=l[i+1]
            l[i+1]=temp
print('list in ascending order is :',l)
l=[1,8,3,2,6,4,24,5]
temp=0
for j in range(0,len(l)-1):
    for i in range(0,len(l)-1):
        if(l[i]<l[i+1]):
            temp=l[i]
            l[i]=l[i+1]
            l[i+1]=temp
print('list in descending order is : ',l)



    