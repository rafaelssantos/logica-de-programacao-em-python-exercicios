for num in range(1, 51):  
    if num % 3 == 0 and num % 5 == 0:  
        print("FizzBuzz")  
        continue  
    if num % 3 == 0:  
        print("Fizz")  
        continue  
    if num % 5 == 0:  
        print("Buzz")  
        continue