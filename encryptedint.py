def encryptedData(data,key):
    ds=str(data)
    dataarr=list(ds)
    res = [eval(i) for i in dataarr]
    ans=[]
    for i in range(len(dataarr)):
        if(i+key<len(dataarr)):
            ans.append(res[i+key])
        else:
            temp=i+key
            while(temp>len(dataarr)):
                temp=(temp)-len(dataarr)
            ans.append(res[(temp)-len(dataarr)])
    new_integer = int(''.join(map(str, ans)))
    return(new_integer)
