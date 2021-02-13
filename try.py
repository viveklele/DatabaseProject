# you need to guess this number
number = 10
# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError as v:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError as c:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")

# class MyError is derived from super class Exception 
class MyError(Exception): 
  
    # Constructor or Initializer 
    def __init__(self, value): 
        self.value = value 
  
    # __str__ is to print() the value 
    def __str__(self): 
        return(repr(self.value)) 
  
try: 
    raise(MyError(3*2)) 
  
# Value of Exception is stored in error 
except MyError as error: 
    print('A New Exception occured: ',error.value)