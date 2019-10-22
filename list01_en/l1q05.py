# - * - coding: utf-8 - * - [Defines the use of some special characters, such as ~, ^, etc.]

'''
Develop an algorithm that can read a temperature in degrees Fahrenheit and display it converted to degrees Celsius.
The conversion formula is C ← ((F - 32) * 5) / 9, where F is the temperature in Fahrenheit and C is the temperature in Celsius.
'''
def tempconv(): #function that converts temperature from celcius to Fahrenheit
  tempinF = int(input("Enter the temperature in Fahrenheit "))   #takes and stores the temperature in Celsius
  tempinC = ((tempinF - 32) * 5) / 9 
  print ("The temperature {} F in C is {}".format(tempinF,tempinC)) #prints temperature in Celsius
tempconv()
