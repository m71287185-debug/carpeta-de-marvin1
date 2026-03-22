
#creamos el input para los grados y lo hacemos float
temperatura = float(input("ingrese la temperatura:"))
#hacemos una nueva entrada para el tipo de grados que estamos ingresando
tipo = (input("¿Es celsius (c) o farenheit (f)?"))
#si el tipo es celsius entonces:
if tipo.upper() == "C":
    farenheit = (temperatura * 9 / 5) +32
    print(f"El resultado es : {farenheit}°F")
#una vez exista la variable farenheit y se imprima su valor si es <= 32 entonces...    
    if farenheit <= 32 : 
        print("AGUA CONGELADA")
    #si lo anterior da false entonces...
    elif farenheit >= 212 : 
        print("AGUA HIRVIENDO!!")
#ahora creamos el condicional si el tipo.upper da F
if tipo.upper() == "F" : 
    celsius = (temperatura - 32) * 5 / 9
    print(f"El resultado es : {celsius}°C")
     #una vez se imprima en pantalla el valor convertido, creamos el condicional para agua congelada
    if celsius <= 0 :
        print("AGUA CONGELADA")
    #ahora para agua hirviendo
    elif celsius >= 100 :
        print("AGUA HIRVIENDO!!")
        