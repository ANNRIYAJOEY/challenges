f=0
t=0
change=True

bills=[5,5,5,5,5]

for bill in bills:
    if bill==5:
        f=f+1
    elif bill==10:
        if f>0:
            f=f-1
            t=t+1
        else:
            change=False
            break
    elif bill==20:
        if f>3:
            f=f-3
        elif f>0 and t>0:
            f=f-1
            t=t-1
        else:
            change=False
            break
    else:
        change=False

if change:
    print(True)
else:
    print(False)
        
