# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 12:08:12 2018

@author: aasup
"""

#fruit = "banana"
#pple = fruit + " " + "orange"
#print(fruit)
#print(apple)

#looping through an index
#fruit="banana"
#index=0
#while index<len(fruit):
 #   letter = fruit[index]
  #  print(index,letter)
   # index=index+1
   
#for loop
#fruit='banana'
#for letter in fruit:
 #   print(letter)
  #  
#print('b' in fruit)

#count number of a's
#fruit="banana"
#index=0
#for letter in fruit:
 #   if letter == 'a':
  #      index=index+1
#print(index)

#editing strings
# =============================================================================
# fruit="Banana"
# 
# zap=fruit.lower()
# 
# print(zap)
# print(fruit)
# =============================================================================
# =============================================================================
# #replace with 'find' with 'count' 'replace' or tons of other options
# fruit='banana'
# 
# pos=fruit.find('na')
# 
# print(pos)
# =============================================================================

# =============================================================================
# greet1='              hey'
# greet2='hey            '
# greet3='       hey       '
# 
# print(greet1.lstrip())
# =============================================================================
# =============================================================================
# x=[1,2]
# 
# print(type(x))
# 
# print(x[0])
# =============================================================================
# =============================================================================
# x=[1,2]
# 
# x[0:1]=[3,4] #0:1 edits the first number in the list, making it 0:2 would do 2
# 
# print(x)
# =============================================================================
# =============================================================================
# x_files=['scully', 'mulder']
# 
# for i in range(len(x_files)):           #looping through list items
#     agent=x_files[i]
#     print('case solved', agent)
# =============================================================================
# =============================================================================
# x=[1,2,3,4,4]
#   
# print(x.count(4))          #printing number of 4's in list
#   
# print(dir(x))       #lists all methods available
# =============================================================================

# =============================================================================
# stuff=list() #is the same as 
# stuff=[]
# 
# stuff.append('book')
# 
# print(stuff)  
# 
# print('book' in stuff)          #asks is book in stuff, returns true or false
# =============================================================================
# =============================================================================
# x=[3,2,1] 
#   
# print(sum(x)/len(x))         #to find average, more stuff in numpy
# =============================================================================
# =============================================================================
# abc='with three words'
# 
# stuff=abc.split()        #turns stuff into a list
# 
# print(stuff)
# 
# abc='andrew@regions.com'
# 
# stuff=abc.split('@')      #splits at the at symbol
# 
# print (stuff)
# =============================================================================
fhand=open('open file saved in the same folder.txt')

for line in fhand:
    line=line.rstrip()
    if not line.startswith('From:'):continue
    words=line.split()
    print(words[2])          #returns all items with second position of from:
    
  
  
  
  
  




















