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
DICT_DATA={"I"  : 1,"V"  : 5,"X":10,"L":50,"C":100,"D":500,"M":1000}


input = "MCM"
def datas(input):
    roman_range=["I","V","X","L","C","D","M"]
    values=[i for i in input]
    integer=0
    for current_roman_index in range(0,len(values)):
        if current_roman_index == 0:
            integer = integer + DICT_DATA.get(values[current_roman_index])
            continue
        current_roman = values[current_roman_index]

        if current_roman_index < len(values)-1:


            if roman_range.index(current_roman) == roman_range.index(values[current_roman_index+1]):
                integer = integer + DICT_DATA.get(current_roman)
                continue
            if roman_range.index(current_roman) > roman_range.index(values[current_roman_index+1]):
                integer = integer + (roman_range.index(values[current_roman_index+1]) - DICT_DATA.get(current_roman))
            if roman_range.index(current_roman) < roman_range.index(values[current_roman_index+1]):
                integer = integer + DICT_DATA.get(current_roman) + roman_range.index(values[current_roman_index+1])
    return integer
print(datas(input=input))

