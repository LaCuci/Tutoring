primo=int(input("Inserire primo orario  "))
secondo=int(input("Inserire secondo orario  "))

primo_ore = int((primo - primo%100)/100)
primo_minuti = primo%100

secondo_ore = int((secondo - secondo%100)/100)
secondo_minuti = secondo%100

intervallo_ore = 0
intervallo_minuti = 0

if primo_minuti>secondo_minuti :
    intervallo_minuti = 60-primo_minuti+secondo_minuti
    intervallo_ore = -1
else :
    intervallo_minuti = secondo_minuti-primo_minuti

if primo_ore>secondo_ore :
    intervallo_ore = intervallo_ore + 24 - primo_ore + secondo_ore
else : 
    intervallo_ore = intervallo_ore + secondo_ore-primo_ore

if intervallo_ore < 0 :
    intervallo_ore = 23
    
print(" Sono passate " , intervallo_ore , " e ", intervallo_minuti, " minuti.")
    

    
