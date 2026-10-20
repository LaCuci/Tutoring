numero = int(input("inserisci il numero   "))
if numero > 4000 :
    exit()

mille = int((numero - numero%1000)/1000)
numero = numero - mille*1000

cinquecento = int((numero - numero%500)/500)
numero = numero - cinquecento*500

cento = int((numero - numero%100)/100)
numero = numero - cento*100

cinquanta = int((numero - numero%50)/50)
numero = numero - cinquanta*50

dieci = int((numero - numero%10)/10)
numero = numero - dieci*10

cinque = int((numero - numero%5)/5)
numero = numero - cinque*5

uno = int((numero - numero%1)/1)
numero = numero - uno*1

cm = int(0)
cd = int(0)
xc = int(0)
xl = int(0)
ix = int(0)
iv = int(0)

if cento == 4 :
    if cinquecento==1 :
        cm = 1 
        cinquecento = 0
    else : cd = 1
    cento = 0

if dieci == 4 :
    if cinquanta == 1:
        xc = 1
        cinquanta = 0
    else : xl = 1
    dieci = 0

if uno == 4 : 
    if cinque ==1 :
        ix = 1
        cinque = 0
    else : iv = 1
    uno = 0



finale = 'M'*mille + 'CM'*cm + 'D'*cinquecento + 'CD'*cd + 'C'*cento + 'XC'*xc + 'L'*cinquanta + 'XL'*xl + 'X'*dieci + 'IX'*ix + 'V'*cinque + 'IV'*iv + 'I'*uno

print(finale)