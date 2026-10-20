numero = int(input("Inserisci il numero "))
if numero%2==0 :
    numero = int(input("inserisci di nuovo il numero"))
    if numero%2==0 : 
        print("non va bene")
    else:
        print("ok")
else :
    print("ok")