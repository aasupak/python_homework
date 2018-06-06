# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 12:03:49 2018

@author: aasup
"""

#def thing():
 #   print("hey")
  #  print("everybody")

#thing()

#big = max('hello world')
#print(big)

#def greet(lang):
 #   if lang=="es":
  #      print("hola ")
   # elif lang=="fr":
    #    print("bon jour ")
 #   else:
  #      print("hello")
        
#l=input("please insert language")
        
#greet(l)

#print("hello")
  
#def addtwo(a,b):
 #   added=a+b
  #  return added

#x=addtwo(3,5)

#print(x)
  
#give 1.5x hourly rate for anything above 40 hours
hour=input("enter hours: ")
rate=input("enter rate: ")
##
if float(hour)<=40:
    print("pay = ", float(hour)*float(rate))
if (float(hour)-40>0):
    print('pay = ', (float(hour) - 40)*1.5*float(rate)+40*float(rate))
print("thank you")




    