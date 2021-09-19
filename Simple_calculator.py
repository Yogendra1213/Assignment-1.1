# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:46:27 2021

@author: YOGENDRA SINGH
"""
op=input("'+': To add, '-': to  Subtract, '*': To Multiply, '/': to Divide,:")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number :"))
if op=="+":
    print("Addition of your numbers is:",num1+num2)
elif op=="-":
    print("Subraction of your numbers is:",num1-num2)
elif op=="/":
    print("Division of your numbera is:",num1/num2)
elif op=="*":
    print("Multiplication of your numbers is:", num1*num2)
else:
    print("Give the Right command sir, Please")
            