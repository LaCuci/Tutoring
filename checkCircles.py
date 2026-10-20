import math
x1 = int(input("coordinata x del centro della prima circonferenza  "))
y1 = int(input("coordinata y del centro della prima circonferenza  "))
r1= int(input("raggio della prima circonferenza  "))
x2= int(input("coordinata x del centro della seconda circonferenza  "))
y2 = int(input("coordinata y del centro della seconda circonferenza  "))
r2 = int(input("raggio della seconda circonferenza  "))

euclidean_centers_distance = math.sqrt( (x1-x2)**2 + (y1-y2)**2)

if x1==x2 and y1==y2 and r1==r2 :
    print("Le due circonferenze sono coincidenti")
elif euclidean_centers_distance==r1+r2 :
    print("Le due circonferenze sono tangenti esternamente")
elif euclidean_centers_distance==r1-r2 :
    print("Le due circonferenze sono tangenti internamente")
elif euclidean_centers_distance>r1-r2 and euclidean_centers_distance<r1+r2 :
    print("Le due circonferenze sono secanti")
elif x1==y1 and x2==y2 :
    print("Le due circonferenze sono concentriche (ma non coincidenti)")
elif euclidean_centers_distance<r1-r2 : 
    print("Le due circonferenze sono una interna all'altra, ma non concentriche")
else : 
    print("Le due circonferenze sono (reciprocamente) esterne")