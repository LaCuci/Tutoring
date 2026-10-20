def returnGravity (planet, weight):
    match planet : 
        case "Mercurio":
            return 0.38*weight
        case "Venere":
            return 0.91*weight
        case "Terra": 
            return 1.00*weight
        case "Marte": 
            return 0.38*weight
        case "Giove": 
            return 2.34*weight
        case "Saturno": 
            return 1.06*weight
        case "Urano": 
            return 0.92*weight
        case "Nettuno": 
            return 1.19*weight
        

weight = input("Inserisci il tuo peso : ")
planet = input("Inserisci il pianeta : ")
print("Sulla terra pesi ", weight, " Su ", planet ," pesi ", returnGravity(planet,float(weight)) )