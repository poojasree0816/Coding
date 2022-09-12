def charEncrypt(character,key):
    asc=ord(character)
    ans=""
    if(asc<=90 and asc>=65):
        asc=asc-65
        if(asc+key<=26):
            ans=chr(asc+key+65)
        else:
            temp=asc+key
            while(temp>=26):
                temp=(temp)-26
            ans=chr(temp+65)
    else:
        if(asc+key<=122):
            ans=chr(asc+key)
        else:
            asc=asc-97
            temp=asc+key
            while(temp>=26):
                temp=(temp)-26
            ans=chr(temp+97)
            
    return ans
print(charEncrypt("h",23))

    
