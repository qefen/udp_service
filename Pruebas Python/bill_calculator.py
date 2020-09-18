#Bill Calculator 

flag = True
to_pay = 0

while flag:
    unit = int( str(input ("Coloque la cantidad de unidades consumidas : ")))
    
    if unit <=100:
        print("Cargo por las primeras 100 unidades")
        print("Rs.10/Unit")
        to_pay=unit*10
        print("TOTAL : "+str(to_pay))
        flag = False

    elif (unit<=200):
        print("Cargo las 100 a 200 unidades")
        print("Rs.15/Unit")
        to_pay=(100*10)+(unit-100)*15
        print("TOTAL : "+str(to_pay))
        flag = False

    elif(unit<=300):
        print("Cargo las 200 a 250 unidades")
        print("Rs.20/Unit")
        to_pay=(100*10)+(100*15)+(unit-200)*20
        print("TOTAL : "+str(to_pay))
        flag = False
    
    elif(unit>300):
        print("Cargo por encima de 300 unidades")
        print("Rs.25/Unit")
        to_pay=(100*10)+(100*15)+(100*20)+(unit-200)*20
        print("TOTAL : "+str(to_pay))
        flag = False

            
  
        
        

   


