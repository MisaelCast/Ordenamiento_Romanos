#############################  Busca letras Romanas en la palabra  #############################

def encontrar_letras(prueba, numeros_romanos):
    # Convertir la cadena a minúsculas
    prueba = prueba.lower()

    letras_encontradas = []

    # Iterar sobre cada letra en 'prueba'
    for letra in prueba:
        if letra in numeros_romanos:
            letras_encontradas.append(letra)  # Agregar la letra a la lista si está en el diccionario

    return letras_encontradas

##################  Valida si no hay más de 3 letras iguales  #############################

def validar_repeticiones(letras_encontradas):
    letras_validadas = []
    conteo_letras = {}

    for letra in letras_encontradas:
        if letra in conteo_letras:
            conteo_letras[letra] += 1
        else:
            conteo_letras[letra] = 1
        
        if conteo_letras[letra] <= 3:
            letras_validadas.append(letra)

    return letras_validadas

######################  Convertir a números y validar reglas ############################

def convertir_a_valores(letras_encontradas, numeros_romanos):
    valores_numericos = []

    for letra in letras_encontradas:
        valores_numericos.append(numeros_romanos[letra])

    # Verificar la condición y modificar la lista si es necesario
    if len(valores_numericos) >= 3:  # Asegurarse de que hay al menos 3 elementos
        if valores_numericos[0] > valores_numericos[1] < valores_numericos[2]:
            # Eliminar todo después del segundo elemento
            valores_numericos = valores_numericos[:2]
        if valores_numericos[0] < valores_numericos[1] > valores_numericos[2]:
            valores_numericos = valores_numericos[:2]

    return valores_numericos

################ Sumar o restar ####################################

def procesar_valores(valores_numericos):
    if len(valores_numericos) < 2:
        return valores_numericos  # Si la lista tiene menos de 2 elementos, no hay nada que procesar

    resultado = 0
    for i in range(len(valores_numericos) - 1):
        if valores_numericos[i] < valores_numericos[i + 1]:
            resultado -= valores_numericos[i]  # Restar si el primer número es menor que el segundo
        else:
            resultado += valores_numericos[i]  # Sumar si el primer número es mayor o igual que el segundo

    # Añadir el último valor de la lista al resultado
    resultado += valores_numericos[-1]

    return resultado

#########################  Función principal  #################################

def main():
    numeros_romanos = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000
    }

    prueba = "ximena"

    letras = encontrar_letras(prueba, numeros_romanos)
    letras_validadas = validar_repeticiones(letras)
    valores = convertir_a_valores(letras_validadas, numeros_romanos)
    resultado = procesar_valores(valores)

    print("Letras encontradas:", letras)
    print("Valores numéricos validados:", valores)
    print("Resultado del procesamiento:", resultado)

############################  Ejecutar el programa ############################

if __name__ == "__main__":
    main()
