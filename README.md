# Conversión y Validación de Números Romanos

Este proyecto convierte secuencias de letras en valores numéricos romanos, valida repeticiones y procesa estos valores según las reglas del sistema romano.

## Funciones

### `encontrar_letras(prueba, numeros_romanos)`
Encuentra y devuelve letras romanas en una cadena de texto.

**Parámetros:**
- `prueba` (str): Cadena de texto.
- `numeros_romanos` (dict): Diccionario de letras romanas a valores numéricos.

**Retorna:** Lista de letras romanas encontradas.

### `validar_repeticiones(letras_encontradas)`
Valida repeticiones de letras romanas permitiendo hasta 3 repeticiones para algunas y solo 1 para otras.

### `casos_con_1(valores_numericos)`
Ajusta valores numéricos si el valor 1 está acompañado por 5 o 10.

### `modificar_lista(valores_numericos)`
Ajusta la lista de valores numéricos según comparaciones entre ellos.

### `convertir_a_valores(letras_encontradas, numeros_romanos)`
Convierte letras en valores numéricos y ajusta la lista según reglas específicas.

**Parámetros:**
- `letras_encontradas` (list): Lista de letras válidas.
- `numeros_romanos` (dict): Diccionario de letras romanas a valores numéricos.

**Retorna:** Lista de valores numéricos ajustados.

### `procesar_valores(valores_numericos)`
Suma o resta valores numéricos basándose en su orden.

**Parámetros:**
- `valores_numericos` (list): Lista de valores numéricos.

**Retorna:** Resultado final del procesamiento.

### `main()`
Función principal que ejecuta el programa y solicita entradas del usuario.

## Ejecución

Para ejecutar el programa, corre el archivo Python:

```bash
python Bueno.py
