def clave(password):

        validar=False #que se vayan cumpliendo los requisitos uno a uno.
        long=len(password) #Calcula la longitud de la contraseña
        espacio=False  #variable para identificar espacios
        alfaNum =password.isalnum()#si es alfanumérica retorna True
        
        for carac in password: #ciclo for que recorre caracter por caracter en la contraseña

            if carac.isspace()==True: #Saber si el caracter es un espacio
                espacio=True #si encuentra un espacio se cambia el valor user
                     
        if espacio==True: #hay espacios en blanco
                print("La contraseña no puede contener espacios")
                  
        else:
            validar=True #se cumple el primer requisito que no hayan espacios
                       
        if long <8 and validar==True:
            print("Mínimo 8 caracteres")
            validar=False #cambia a False si no se cumple el requisito minimo de caracteres
           
        if validar == True:
    
           return True