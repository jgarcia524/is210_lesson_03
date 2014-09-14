#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Loan repayment"""

from decimal import Decimal
NAME = raw_input("What is your name?")
P = int(raw_input(
    "What is the amount of your principal (the amount being borrowed)?"))
T = int(raw_input("For how many years is this loan being borrowed?"))
QUAL = raw_input("Are you prequalified for this loan?")
QU = QUAL.lower()
Q = QU[0]
R = None

if P >= 0 and P <= 199999:
    if T >= 1 and T <= 15:
        if Q == "y":
            R = "0.0363"
        elif Q == "n":
            R = "0.0465"
    elif T >= 16 and T <= 20:
        if Q == "y":
            R = "0.0404"
        elif Q == "n":
            R = "0.0498"
    elif T >= 21 and T <= 30:
        if Q == "y":
            R = "0.0577"
        elif Q == "n":
            R = "0.0639"
elif P >= 200000 and P <= 999999:
    if T >= 1 and T <= 15:
        if Q == "y":
            R = "0.0302"
        elif Q == "n":
            R = "0.0398"
    elif T >= 16 and T <= 20:
        if Q == "y":
            R = "0.0327"
        elif Q == "n":
            R = "0.0408"
    elif T >= 21 and T <= 30:
        if Q == "y":
            R = "0.0466"
elif P >= 1000000:
    if T >= 1 and T <= 15:
        if Q == "y":
            R = "0.0205"
    elif T >= 16 and T <= 20:
        if Q == "y":
            R = "0.0262"
N = 12
if R is None:
    TOTAL = None
else:
    FINAL = P*((1+(Decimal(R))/N))**(N*T)
    TOT = round(FINAL)
    TOTAL = int(TOT)

DASHES = "-" * 78
REPORT = """
\n Loan Report for: {0} \n {1}
    Principal: {6:>10}{2}
    Duration: {3:>12}yrs
    Pre-qualified?: {4:>9} \n
    Total: {6:>14}{5}"""

print REPORT.format(NAME,DASHES,P,T,QUAL,TOTAL,"$")
