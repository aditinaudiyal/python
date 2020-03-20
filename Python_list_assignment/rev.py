#reverse the list without using reverse function
l=[1,8,3,2,6,4,24,5]
rev_l=[]
#executing loop from last index 
for i in range(len(l)-1,-1,-1):
    rev_l.append(l[i])
print('list is :',l)
print('reversed list is : ',rev_l)