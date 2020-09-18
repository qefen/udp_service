#Programa que recibe una lista y retorna el tamaño de esta

fruits=["Banana","Apple","Watermelon","Lemond"] 
numbers=[1,2,3,4,5,6,7,8] 

def my_len(list):
    count=0
    for i in list:
        count=count+1
    return count

print("Cantidad de datos en la lista friuts : "+str(my_len(fruits)))
print("Cantidad de datos en la lista numbers : "+str(my_len(numbers)))