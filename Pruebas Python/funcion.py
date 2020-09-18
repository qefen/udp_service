#Programa con una fucion que devuelve el numero mayor de una lista de numeros indeterminada
num =[10,15,60,8,1,30]

def max(num):
    result=0
    count=0
    for i in num:
        if num[count] >= result:
            result=num[count]
        count=count+1
    return result

print(max(num))