# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 10:34:30 2021

@author: YOGENDRA SINGH
"""

li=[1,23,23,4,55,"yogendra","hello"]
li.append("yogi")
l2=li.copy()
l2.clear()
x=li.count(23)
print(x)
l2.extend(li)
print(li.index(23))
li.insert(5,99)
y=li.pop()
print("The popped item is:",y)
l2.remove(55)
li.reverse()
l3=[2,35.56,85,45,969,66,25]
l3.sort(reverse=True)
l3.sort(reverse=False)
