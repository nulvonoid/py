#def collatz(n):
#    if n % 2 == 0:
#        print (n // 2)
#        return n // 2
#    elif n % 2 == 1:
#        result=3*n +1
#        print (result)
#        return result
#
#try:
#    n = int(input("Masukin angka : "))
#except ValueError:
#    print ('Masukin angka boy')
#
#while n != 1:
#    n = collatz(int(n))
def validate_user_input():
   while True:
       try:
           number = int(input("Enter a positive integer (minimum 2): "))
       except KeyboardInterrupt:
           print('\nSee you next time!')
           break
       except ValueError:
           print("That was not even a valid integer!")
       else:
           if number < 0:
               print("Positive integer, please!")
           elif number < 2:
               print("Integer should be at least equal to 2 !")
           else:
               return number 

def collatz(n):
    if n == 1:
        return
    else :
        newNumber = n // 2 if newNumber % 2 == 0 else n * 3 + 1
        print (newNumber)
        collatz (newNumber)

n = int(input('Masukin nomer '))

if __name__ == '__main__':

   print('Collatz Conjecture Collatz Conjecture')
   number = validate_user_input()
   collatz(number)
