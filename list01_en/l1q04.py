# - * - coding: utf-8 - * - [Defines the use of some special characters, such as ~, ^, etc.]

'''
Develop an algorithm that can read a temperature in degrees Celsius and display it converted to degrees Fahrenheit.
The conversion formula is F ← (9 * C + 160) / 5, where F is the temperature in Fahrenheit and C is the temperature in Celsius.
'''
def tempconv(): #function that converts temperature from celsius to Fahrenheit
  tempinC = float(input("Enter the temperature in Celsius "))   #takes and stores the temperature in Celsius
  tempinF = (9*tempinC + 160)/5 
  print ("The temperature {1} C in Fahrenheit is {0:.2f}".format(tempinF,tempinC)) #prints temperature in Celsius
tempconv()
