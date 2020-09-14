#Bill Calculator 

flag = True
to_pay =0

#flag = False

while flag:
    unit = input ("Coloque la cantidad de unidades consumidas :")
   
    if int(unit)>100:
        print("Cargo por las primeras 100 unidades")
        print("Rs.10/Unit")
       
        to_pay=unit*10
        print("TOTAL :"+str(to_pay))
        

   


