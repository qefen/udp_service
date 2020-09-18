#Programa con una fucion que devuelve el numero mayor 
num =[10,15,60,8,1,30]

def max(num):
    result=0
    count=0
    for i in num:
        if num[count] >= result:
            result=num[count]
        count=count+1
    return result

         
#for x in num:
#    if num[count] > result:
#        result=num[count]
#    count=count+1

print(max(num))



