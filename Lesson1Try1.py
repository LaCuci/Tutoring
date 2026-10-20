def boo(foo):
            roo        =       False
            if        foo         :
                    poo        =        foo.split(     "@"     )
                    if    len(      poo      )    ==    2    :
                            uoo     =     poo[    0    ]
                            doo    =     poo[    1    ]
                            if    doo    ==    "studenti.unipd.it"    :
                                    soo    =    uoo.split(    "."    )
                                    if    len(    soo    )    ==    2    or    len(    soo    )    ==    3    :
                                            if    soo[    0    ].isalpha()    and    soo[    1    ].isalpha()    :
                                                    if    len(    soo    )    ==    2    :
                                                            roo    =    True
                                                    elif    soo[    2    ].isdigit()    :
                                                            roo    =    True
            return    roo
        
# Funzione che ritorna true se la stringa inserita ha la struttura di una mail studentesca
def controllo_email_unipd_studenti(email): 
    
    #Controllo input valido : se non c'è niente dentro l'input o se non c'è @ allora non è una mail
    if not email or "@" not in email:                                  
        return False
    # pezzi è un vettore che contiene tutte le sottostringhe separate dalle varie @ nell'input 
    pezzi = email.split("@")
    #controllo seconda parte : deve essere xxx@studenti.unipd.it quindi se ci sono piu di due parti
    #o se la seconda parte non è studenti.unipd.it allora non è nel formato che cerchiamo 
    if len(pezzi) != 2 or pezzi[1] != "studenti.unipd.it":
        return False
    #sotto pezzi è un altro vettore che contiene le varie parti della prima metà della stringa
    #che sono separate da punti 
    sotto_pezzi = pezzi[0].split(".")
    #controllo prima parte : nome.cognome o nome.cognome.numero
    #se ci sono solo due parti devono essere nome e cognome quindi entrambe composte solo da lettere
    if len(sotto_pezzi) == 2:
        return (sotto_pezzi[0].isalpha() and sotto_pezzi[1].isalpha())
    #se ci sono tre parti allora l'ultima deve essere un numero, come mario.rossi.1
    elif len(sotto_pezzi) == 3:
        return (sotto_pezzi[0].isalpha() and sotto_pezzi[1].isalpha() and sotto_pezzi[2].isdigit())
    #se non ha soddisfatto nessuno dei requisiti allora non è nella forma che cerchiamo
    return False



def MiniProva():
    lettera = int(input("Metti la lettera"))
    if not lettera : 
        return False
    
    return lettera+2
    
    
print(boo("martina.naldoni@studenti.unipd.it"))
print(controllo_email_unipd_studenti("martina.naldoni@studenti.unipd.it"))
print(MiniProva())
