#!usr/bin/env python
# -*- coding: utf-8 -*-

BASE = raw_input("Choose a base color: Seattle Gray or Manatee ")

if BASE == "Seattle Gray":
    ACCENT = raw_input("Choose an accent color: Ceramic Glaze or Cumulus Nimbus ")
    if ACCENT== "Ceramic Glaze":
        HIGHLIGH = raw_input("Choose a highlight color: Basically White or White ")
    elif ACCENT == "Cumulus Nimbus":
        THIRDCHOICE = raw_input("Choose a highlight color: Off-White or Paper White ")

else:
    if BASE == "Manatee":
        ACCENT = raw_input("Choose an accent color: Platinum Mist or Spartan Sage ")
        if ACCENT == "Platinum Mist":
            HIGHLIGH = raw_input("Choose a highlight color:Bone White or Just White ")
        elif ACCENT == "Spartan Sage":
            HIGHLIGHT = raw_input("Choose an accent color: Fractal White or Not White ")

SELECTION = "Your color selections are: {0} for the base color, {1} for the accent color, and {2} for the highlight color."
print(SELECTION.format(BASE, ACCENT, HIGHLIGHT))
