for num in range(1,100): # Por cada numero desde el 1 hasta el 100...
    if num%3 == 0 and num%5 == 0:  # Si el numero es divisible de 3 y de 
        print("FizzBuzz") # Mostramos "FizzBuzz"
    elif num%5 == 0: # Si el numero es divisible de 5...
        print("Buzz") # Mostramos "Buzz"
    elif num%3== 0: # Si el numero es divisible de 3...
        print("Fizz") # Mostramos "Fizz"
    else: # Si no es divisible de 3 ni de 5...
        print(num) # Mostramos el numero.
