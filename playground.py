"""a=["ab","ab","nt"]
length=len(a[0])
for i in range(len(a)):
    if len(a[i]) < length:
        length = len(a[i])
a=[i[0:length] for i in a]
result=""
if len(a) > 1:
    for i in range(len(a[0])):
        count = 0
        cmpr=a[0][i]
        for j in a:
            if cmpr == j[i]:
                count +=1
        if count == len(a):
            result = result+cmpr
        else:
            print(result)
    print(result)
else:
    print (a[0])


    """
