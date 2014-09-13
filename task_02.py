#!/usr/bin/env python
# -*- coding: utf-8 -*-

BLOODPRESSURE = int(raw_input("What is your blood pressure?" ))

if BLOODPRESSURE <= 89:
    BP_STATUS = "Low"
elif BLOODPRESSURE > 89 and BLOODPRESSURE <= 119:
    BP_STATUS = "Ideal"
elif BLOODPRESSURE > 119 and BLOODPRESSURE <= 139:
    BP_STATUS = "Warning"
elif BLOODPRESSURE > 139 and BLOODPRESSURE <= 159:
    BP_STATUS = "High"
else:
    BP_STATUS = "Emergency"

Status = "Your blood pressure status is {}."
print Status.format(BP_STATUS)
