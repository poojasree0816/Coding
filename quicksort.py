def partition(a,l,u):
    pivot=a[l]
    start=l
    end=u
    while(start<end):
        while(a[start]<=pivot):
            start=start+1
        while(a[end]>pivot):
            end=end-1
        if(start<end):
            a[start],a[end]=a[end],a[start]
    a[l],a[end]=a[end],a[l]
    return end
def quicksort(arr,l,u):
    if(l<u):
        loc=partition(arr,l,u)
        partition(arr,l,loc-1)
        partition(arr,loc+1,u)
arr=[2,4,1,5,3]
quicksort(arr,0,4)
print(arr)
