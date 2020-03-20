#print exception,sucess,fail from list with index
l=["exception occured",'failed','success','Pass',"executed",'exception','completed','success','successful']
for i in range(0,len(l)):
#check for given words in each element of the list
    if(('exception' in l[i]) or ('success' in l[i]) or ('fail' in l[i])):
        print(l[i],'index value is:',i)