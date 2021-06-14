s=[[1,2,3,4,5,6,7,8,9],[2,3,4,5,1,6,7,8,9]]
l=[4,3,5,6,7,8,9,1,2]


for i in s:
    count=0
    #count = 0
    #for k in l:
    for j,k in zip(i,l):
        if j!=k:
            count+=1
    print(count)

     #       if k != j:
      #          count += 1
       # print("from first innerlist: ",count)