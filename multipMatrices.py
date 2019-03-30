def mulMat(m1,m2):
    r=0
    try:
        mon=m1[0].__len__()
    except:
        mon=1
    if (mon==m2.__len__()):
        long=m2.__len__()
        height=m1.__len__()
        try:
            length=m2[0].__len__()
        except:
            length=1
        mr=[]
        mr=[
            [
                0
                for x in range(length)
                ]
            for y in range (height)
            ]
        for a in m1:
            for b in range(length):
                for c in range(long):
                    if mon==1:
                        if length==1:
                            mr[r][b]+=a*m2[c]
                        else:
                            mr[r][b]+=a*m2[c][b]
                    else:
                        if length==1:
                            mr[r][b]+=a[c]*m2[c]
                        else:
                            mr[r][b]+=a[c]*m2[c][b]
            r+=1
        return mr
    else:
        return 0
    
                
a=[1,2,3]
b=[[1,2]]
print(mulMat(a,b))
