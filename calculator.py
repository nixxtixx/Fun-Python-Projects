def adding(x,y):
  print( str(x) + " + " + str(y) )
  print(x + y)
  print("-------------")


def subtracting(x,y):
  print( str(x) + " - " + str(y) )
  print(x - y)
  print("------------")

def multipying(x,y):
  print( str(x) + " * " + str(y) )
  print(x * y)
  print("-------------")

def dividing(x,y):
  if( y == 0):
    print("Cant divide by 0")
  else:
    print( str(x) + " / " + str(y) )
    print( x / y) 


while(True):
  num1 = int( input("First number: ") )
  num2 = int( input("Second number: ") ) 
  operation = input("Do you want to add(a)?, subtract(s)?, multipy(m), or divide(d)? Choose letter a ONLY: ")
  

  if(operation == "a"):
    adding(num1, num2)
  elif(operation == "s"):
    subtracting(num1, num2)
  elif(operation == "m"):
    multipying(num1, num2)
  elif(operation == "d"):
    dividing(num1, num2)
  else:
    print("Invalid Resoponse")
