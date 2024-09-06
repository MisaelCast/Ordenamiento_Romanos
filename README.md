# 📜 Conversor de Letras Romanas

Este proyecto contiene un programa en Python que busca letras en una cadena de texto, verifica si corresponden a números romanos, valida las reglas de repetición de letras, y convierte dichas letras en su valor numérico correspondiente. Posteriormente, procesa estos valores según las reglas de los números romanos, para producir un resultado final.

## 🔍 Funciones principales

### 1. 🔡 `encontrar_letras(prueba, numeros_romanos)`
   - **Descripción**: Busca letras de números romanos (`i`, `v`, `x`, `l`, `c`, `d`, `m`) en una cadena de texto y las almacena en una lista.
   - **Parámetros**:
     - `prueba`: Cadena de texto donde se buscarán las letras.
     - `numeros_romanos`: Diccionario con las letras romanas y sus valores numéricos.
   - **Devuelve**: Lista con las letras encontradas que son números romanos.

### 2. 🚫 `validar_repeticiones(letras_encontradas)`
   - **Descripción**: Valida que no haya más de tres repeticiones de las mismas letras romanas consecutivas.
   - **Parámetros**:
     - `letras_encontradas`: Lista de letras encontradas.
   - **Devuelve**: Lista de letras que pasan la validación de repetición.

### 3. 🔢 `convertir_a_valores(letras_encontradas, numeros_romanos)`
   - **Descripción**: Convierte las letras romanas a sus valores numéricos y aplica reglas para eliminar combinaciones no válidas.
   - **Parámetros**:
     - `letras_encontradas`: Lista de letras encontradas.
     - `numeros_romanos`: Diccionario con las letras romanas y sus valores numéricos.
   - **Devuelve**: Lista de valores numéricos después de aplicar validaciones.

### 4. ➕➖ `procesar_valores(valores_numericos)`
   - **Descripción**: Procesa los valores numéricos de acuerdo a las reglas de los números romanos, sumando o restando según corresponda.
   - **Parámetros**:
     - `valores_numericos`: Lista de valores numéricos correspondientes a las letras romanas encontradas.
   - **Devuelve**: El resultado final después de procesar los valores.

### 5. 🚀 `main()`
   - **Descripción**: Función principal que ejecuta el programa. Define una cadena de prueba, realiza las conversiones, y muestra los resultados.
   - **Cadena de prueba**: `"ximena"`

## 🛠 Ejecución del programa

Para ejecutar el programa, asegúrate de tener instalado Python en tu sistema. Luego, simplemente corre el archivo:

```bash
python bueno.py
