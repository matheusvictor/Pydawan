# - * - coding: utf-8 - * - [Defines the use of some special characters, such as ~, ^, etc.]

def tempconv(): #function that converts temperature from Fahrenheit to celcius 
  tempinF = float(input("Enter the temperature in Fahrenheit "))   #takes and stores the temperature in Fahrenheit
  tempinC = ((tempinF - 32) * 5) / 9 
  print ("The temperature {} F in C is {:.2f}".format(tempinF,tempinC)) #prints temperature in Celsius

tempconv()
