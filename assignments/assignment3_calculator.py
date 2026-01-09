from loguru import logger

a=float(input("enter the first Number: "))

while True :
  
  operatorr=input("enter the function + - / *")
  
  c = float(input("enter the next number "))

  if operatorr == "+":
      a = a + c
  elif operatorr == "-":
      a = a - c
  elif operatorr == "*":
      a = a * c
  elif operatorr == "/":
      a = a / c      
  z=int(input("if u want the result enter 0 else enter 1"))
  if(z==0):
    break
    

print("the Final result",a)