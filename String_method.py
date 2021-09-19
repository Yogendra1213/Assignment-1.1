# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 11:21:24 2021

@author: YOGENDRA SINGH
"""

st="yogendra1213"
a=st.capitalize()
print(a)
b=st.casefold()
print(b)
c=st.center(50)
print(c)
d=st.center(50,"a")
print(d)
e=st.count("1")
print(e)
f=st.encode()
print(f)
print(st.endswith("12"))
print(st.endswith("13"))
print(st.endswith("gen",2,4))
print(st.endswith("gen",2,5))
g="h\te\tl\tl\to"
print(g.expandtabs(10))
print(st.find(g))
stt="My Name is {}"
h=stt.format("Yogendra")
print(h)
print(st.index("y"))
print(st.isalnum())
print(st.isalpha())
print(st.isdecimal())
print(st.isdigit())
print(st.isidentifier())
print(st.islower())
print(st.isnumeric())
print(st.isprintable())
print(st.isspace())
print(st.istitle())
print(st.isupper())
i='#$'.join(st)
print(i)
print(st.ljust(20),"is my name")
print(h.lower())
tx="                hello   worldd.."
print(tx.lstrip())
t1="oge"
t2="fib"
t3="123"
transed=st.maketrans(t1,t2,t3)
print(transed)
print(st.translate(transed))
print(st.upper())
print(st.title())
print(h.swapcase())
print(st.startswith('y'))
print(st.startswith("g",2,5))
print(tx.strip())
print(h.partition("is"))
j=h.replace("Yogendra","Ram")
print(j)
print(st.rfind("1"))
print(st.rindex("1"))
print(tx.rjust(10))
txx="hello"
print(txx.rjust(20))
print(h.rpartition("is"))
print(h.rsplit())
txxx="hello                 "
print(txxx.rstrip(),"world")
print(h.split())
print(h.splitlines())
txt="man"
print(txt.zfill(10))





