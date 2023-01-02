# Reto #0: EL FAMOSO "FIZZ BUZZ"
#### Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23

## Enunciado

# ```
# /*
#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */
# ```

for n in range(1,101):
    if n % 15 == 0:
        print(f"{n}-fizzbuzz")
    elif n % 3 == 0:
        print(f"{n}-fizz")
    elif n % 5 == 0:
        print(f"{n}-buzz")
    else: 
        print(n)    
