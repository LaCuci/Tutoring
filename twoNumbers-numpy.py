import numpy as np

primo = int(input("inserisci il primo numero : "))
secondo = int(input("inserisci il secondo numero : "))

arr = np.array([primo,secondo])

print("somma : ", np.sum(arr))
print("prodotto : ", np.prod(arr))
print("Media : ", np.mean(arr))
print("Massimo : ", np.max(arr))
print("Minimo : ", np.min(arr))
print("differenza : ", np.diff(arr))