# Programa que recibe un carater y retorna si es o no una vocal

def my_vowels(character):
    vowels=["a","A","i","I","o","O","e","E","U","u"]
    flag="No es una vocal"
    count=0
    for i in vowels:
        if character==vowels[count]:
            flag="Es una vocal"
            break      
        count=count+1
    return flag

print(my_vowels("A"))