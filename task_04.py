#1!user/bin/env python
# -*- coding: utf-8 -*-
"""Wake up alarm!"""

USERDAY = raw_input("What day of the week is it today?")
TODAY = USERDAY.lower()
DAY = TODAY[0:3]
TIME = int(raw_input("What time is it? (exclude the colon symbol in your response.)"))
SNOOZE = "more sleep!"

if DAY == "sat" or DAY == "sun" or TIME <= 600:
    SNOOZE == True
else:
    SNOOZE == False
    print "Beep! Beep! Beep! Beep! Beep!"
