def son_anagramas (cadenaUno: str, cadenaDos: str)-> bool:
    #aqui se lleva a minusculas ambas cadenas
    cadenaUno_min = cadenaUno.lower()
    cadenaDos_min = cadenaDos.lower()
    
    temp_cadenaUno =[]
    for caracter in cadenaUno_min:
        if not caracter.isspace():
            temp_cadenaUno.append(caracter)
    cadenaUno ="".join (temp_cadenaUno)
    
    if len(cadenaUno)!=len(cadenaUno):
        return False
    
    #aqui se cuenta con los carateres de la cadena 1
    conteo={}
    for caracter in cadenaUno:
        conteo[caracter]=conteo.get(caracter,0)+1
        
    for caracter in cadenaDos:
        if caracter not in conteo:
            return False
        conteo[caracter]-=1
        if conteo[caracter]<0:
            return False
        
    #recorrido final
    for caracter in conteo.values():
        if caracter!=0:
            return False
    return True

respuetaAnagrama=son_anagramas("Aaaamor","Romaaaa")

if  respuetaAnagrama:
    print ("Son anagramas")