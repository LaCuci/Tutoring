anno = int(input("inserisci anno : "))

if anno<=0 : 
    print("Errore")
elif anno <= 1582 : 
    if anno%4==0 :
        print("Leap")
    else : 
        print("Not Leap")
elif anno%400 == 0 :
    print("Leap")
elif anno%100 == 0 : 
    print("Not Leap")
elif anno%4 == 0 : 
    print("Leap")
else :
    print("Not Leap")
