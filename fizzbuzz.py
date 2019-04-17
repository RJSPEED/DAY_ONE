def fizz_buzz(input_number):
    for num in range(1,input_number,1):
        if num % 3 == 0 and num % 5 == 0:
            print ("FizzBuzz")
        elif num % 5 == 0 :
            print ("Buzz")
        elif num % 3 == 0:
            print ("Fizz")            
        else:
            print (num)            

#fizz_buzz(20)
