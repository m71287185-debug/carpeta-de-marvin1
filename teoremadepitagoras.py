AZUL =  "\033[36m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
RESET = "\033[0m"
#definimos la funcion para limpiar 
import os
def limpiar():
        os.system('cls' if os.name == 'nt' else 'clear')
# lo siguiente se ejecutara en bucle infinito hasta un break
while True :
    limpiar()
    print(f"{AMARILLO}------- CALCULADORA DE PITAGORAS -------{RESET}") 
    pregunta_inicial = input(f"Presiona {AZUL}ENTER{RESET} para iniciar: ")
  #abre la entrada para el tipo de dato
    entrada1 = input(f"¿Qué quieres calcular, cateto ({AZUL}C{RESET}) ó hipotenusa ({AZUL}H{RESET})? :")
    if entrada1.upper() == "C":
       #TRATA DE REALIZAR LO SIGUIENTE 
       try:
            hipotenusa = float(input("Valor de la hipotenusa (en cm):"))
            if hipotenusa <= 0:
                 print(f"❌¡Triángulo imposible! {ROJO}Las medidas deben ser mayores a cero.{RESET}")
                 input(f"Presiona {AZUL}ENTER{RESET} para intentar de nuevo...")
                 continue      
            cateto_conocido =  float(input("Valor de cateto conocido(en cm):")) 
            if cateto_conocido <= 0:
                 print(f"❌¡Triángulo imposible! {ROJO}Las medidas deben ser mayores a cero.{RESET}")
                 input(f"Presiona {AZUL}ENTER{RESET} para intentar de nuevo...")                                                                  
            elif hipotenusa <= cateto_conocido : 
                print(f"⚠️¡ATENCIÓN! {ROJO}La hipotenusa debe ser mayor que el cateto.{RESET}")
                input(f"Presiona {AZUL}ENTER{RESET} para intentar de nuevo...")  
            # TAMBIEN PUEDE SER QUE SI, EN ESE CASO EJECUTA LO SIGUIENTE 
            else :
                cateto_faltante = (hipotenusa ** 2 - cateto_conocido ** 2) ** 0.5
                print(f"{VERDE}El valor del cateto faltante es de {cateto_faltante} cm{RESET}")
                input(f"Presiona {AZUL}ENTER{RESET} para volver...")
                #DESPUES DEL INPUT SE REINICIA EL BUCLE 
       #SI DA UN ERROR DE VALOR REALIZA LO SIGUIENTE 
       except ValueError:
             print(f"❌ ENTRADA INVÁLIDA: {ROJO}Por favor, usa solo números{RESET}.")
             input(f"Presiona {AZUL}ENTER{RESET} para volver al menú...") 
             #DESPUES DEL INPUT SE REINICIA EL BUCLE            
                   #EN CONTRUCCION
    elif entrada1.upper() == "H":
           #TRATA DE REALIZAR LO SIGUIENTE 
           try:
               cateto_conocidoh = float(input("Valor del cateto 1 (en cm):"))
               if cateto_conocidoh <= 0 : 
                   print(f"❌¡Triángulo imposible! {ROJO}Las medidas deben ser mayores a cero.{RESET}")
                   input(f"Presiona {AZUL}ENTER{RESET} para intentar de nuevo...")
                   continue 
               cateto_conocido2h = float(input("valor de cateto 2 (en cm):"))
               if cateto_conocido2h <= 0 : 
                  print(f"❌¡Triángulo imposible! {ROJO}Las medidas deben ser mayores a cero.{RESET}")
                  input(f"Presiona {AZUL}ENTER{RESET} para intentar de nuevo...") 
               else:   
                   valordeh = (cateto_conocidoh ** 2 + cateto_conocido2h ** 2) ** 0.5 
                   print(f"{VERDE}El valor de la hipotenusa es de {valordeh} cm{RESET}")
                   input(f"Presiona {AZUL}ENTER{RESET} para finalizar") 
           except ValueError:
                print(f"❌ ENTRADA INVÁLIDA: {ROJO}Por favor, usa solo números{RESET}.")
                input(f"Presiona {AZUL}ENTER{RESET} para volver al menú...") 
    elif entrada1.upper() != "H" and entrada1.upper() != "C":
         pass

         




        
    