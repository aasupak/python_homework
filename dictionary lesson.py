# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 11:06:31 2018

@author: aasup
"""

# =============================================================================
# purse=dict()
# purse['money']=1200000000
# purse['candy']=3
# purse['tissue']=75
# 
# print(purse)
# 
# print(purse['money'])
# 
# purse['money']=purse['money']+100
# 
# print (purse)
# 
# =============================================================================

# =============================================================================
# j={'chuck':1, 'fred':2}
# 
# print(j['chuck'])
# 
# =============================================================================

# =============================================================================
# hist=dict()
# 
# while True:
#     inp=input(':')
#     if inp == 'done':break
#     if inp in hist:
#         hist[inp]=hist[inp]+1
#     else:
#         hist[inp]=1
# print(hist)
# =============================================================================
# =============================================================================
# counts=dict()
# 
# print('Enter a line of text:')
# 
# line=input('>')
# 
# words=line.split()
# 
# print('words:' ,words)
# 
# print('counting...')
# 
# for word in words:
#     counts[word]=counts.get(word,0)+1
#     
# #print('Counts=',counts)
# 
# #print(list(counts))
# =============================================================================
# =============================================================================
# counts={'apple':2,'bananan':1}
# 
# for key,value in counts.items():
#     print(key,value)
#     
#     
# =============================================================================
# =============================================================================
# name=input('enter file:')
# handle=open(name)
# 
# counts=dict()
# 
# for line in handle:
#     words=line.split()
#     for word in words:
#         counts[word]=counts.get(word,0)+1
#         
# bigcount=None
# bigword=None
# 
# for word,count in counts.items():
#     if bigcount is None or count>bigcount:
#         bigword=word
#         bigcount=count
#         
# print(bigword,bigcount)
# 
# =============================================================================
#Tuples similar to lists, indexes (0 is the first place) items just like lists
#use double underscores "__" for some of these, see: print(dir(l))
#l=(x,y)=(1,2)
#print(dir(l))
#print(max(l))
#d={'apples':1, 'banana':3}
d={'a':10,'b':1,'c':22}
#for k,v in d.items():
#    print(k,v)
T=sorted(d.items())    
print(T)
    

c={'a':10,'b':1,'c':22}

temp=list()

for k,v in c.items():
    temp.append((v,k))
    
temp=sorted(temp,reverse=True)

print(temp)


    

    





















