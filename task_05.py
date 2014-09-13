#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Loan repayment"""

from decimal import Decimal
NAME = raw_input("What is your name?")
P = int(raw_input("What is the amount of your principal (the amount being borrowed)?"))
t = int(raw_input("For how many years is this loan being borrowed?"))
Qual = raw_input("Are you prequalified for this loan?")
q = Qual.lower()
Q = q[0]

if P <= 199999:
    if t >= 1 and t <= 15:
        if Q == "y":
            r = "0.0363"
        elif Q == "n":
            r = "0.0465"
    elif t >= 16 and t <= 20:
        if Q == "y":
            r = "0.0404"
        elif Q == "n":
            r = "0.0498"
    elif t >= 21 and t <= 30:
        if Q == "y":
            r = "0.0577"
        elif Q == "n":
            r = "0.0639"
    else:
        r = None
elif P >= 200000 and P <= 999999:
    if t >= 1 and t <= 15:
        if Q == "y":
            r = "0.0302"
        elif Q == "n":
            r = "0.0398"
    elif t >= 16 and t <= 20:
        if Q == "y":
            r = "0.0327"
        elif Q == "n":
            r = "0.0408"
    elif t >= 21 and t <= 30:
        if Q == "y":
            r = "0.0466"
        if Q == "n":
            r = None
    else:
        r = None
elif P >= 1000000:
    if t >= 1 and t <= 15:
        if Q == "y":
            r = "0.0205"
        if Q == "n":
            r = None
    elif t >= 16 and t <= 20:
        if Q == "y":
            r = "0.0262"
        if Q == "n":
            r = None
else:
    r = None
            
n = 12
FINAL = P*((1+(Decimal(r))/n))**(n*t)
TOTAL = round(FINAL)
