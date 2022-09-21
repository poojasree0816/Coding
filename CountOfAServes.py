def getSum(array):
    count=0
    for i in range(0,len(array),2):
        tempsum=array[i]+array[i+1]
        t1=tempsum%2
        t=tempsum//2
        if(t==0):
            count=count+1
        elif(t==1 and t1==0):
            count=count
        else:
            if(t1==0):
                if(t%2==1):
                    count=count+1
            else:
                if(t%2==0):
                    count=count+1
    return count
