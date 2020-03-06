# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 00:30:02 2019

@author: purva patel
"""

value = int(input("enter the value: "))
islessthanzero = 0
if(value < 0):
    value = -value
    islessthanzero = 1

def checkGL(value, power):
    if(value < 0):
        return 1
    return 1

def abc(value):
    takechekGL = 0
    finalis = ""
    maxvalue = 0
    valuedifference = 0
    
    if(value <= 1):
        maxvalue = 1
    elif(value <= 4):
        maxvalue = 3
    elif(value <= 13):
        maxvalue = 9
    elif(value <= 40):
        maxvalue = 27
    else:
        maxvalue = 81
    finalis = " + " + str(maxvalue) + finalis
    extra = " "
    
    while(value != maxvalue):
        valuedifference = maxvalue - value
        if(valuedifference < 0):
            if(valuedifference <= -41):
                takechekGL = checkGL(valuedifference, 41)
                maxvalue = maxvalue + (takechekGL *81)
                if(takechekGL < 0):
                    extra = " "
                else:
                    extra = " + "
                finalis = extra + str(takechekGL*81) + finalis
            elif(valuedifference <= -14):
                takechekGL = checkGL(valuedifference, 27)
                maxvalue = maxvalue + (takechekGL *27)
                if(takechekGL < 0):
                    extra = " "
                else:
                    extra = " + "
                finalis = extra + str(takechekGL*27) + finalis
            elif(valuedifference <= -5):
                takechekGL = checkGL(valuedifference, 9)
                maxvalue = maxvalue + (takechekGL *9)
                if(takechekGL < 0):
                    extra = " "
                else:
                    extra = " + "
                finalis = extra + str(takechekGL*9) + finalis
            elif(valuedifference <= -2):
                takechekGL = checkGL(valuedifference, 3)
                maxvalue = maxvalue + (takechekGL *3)
                if(takechekGL < 0):
                    extra = " "
                else:
                    extra = " + "
                finalis = extra + str(takechekGL*3) + finalis
            elif(valuedifference <= -1):
                takechekGL = checkGL(valuedifference, 1)
                maxvalue = maxvalue + (takechekGL *1)
                if(takechekGL < 0):
                    extra = " "
                else:
                    extra = " + "
                finalis = extra + str(takechekGL*1) + finalis
        else:
            if(valuedifference <= 1):
                takechekGL = checkGL(valuedifference, 1)
                maxvalue = maxvalue + (takechekGL *1)
                if(takechekGL < 0):
                    extra = " "
                else:
                    extra = " + "
                finalis = extra + str(takechekGL*1) + finalis
            elif(valuedifference <= 4):
                takechekGL = checkGL(valuedifference, 3)
                maxvalue = maxvalue + (takechekGL *3)
                if(takechekGL < 0):
                    extra = " "
                else:
                    extra = " + "
                finalis = extra + str(takechekGL*3) + finalis
            elif(valuedifference <= 13):
                takechekGL = checkGL(valuedifference, 9)
                maxvalue = maxvalue + (takechekGL *9)
                if(takechekGL < 0):
                    extra = " "
                else:
                    extra = " + "
                finalis = extra + str(takechekGL*9) + finalis
            elif(valuedifference <= 40):
                takechekGL = checkGL(valuedifference, 27)
                maxvalue = maxvalue + (takechekGL *27)
                if(takechekGL < 0):
                    extra = " "
                else:
                    extra = " + "
                finalis = extra + str(takechekGL*27) + finalis
            elif(valuedifference <= 121):
                takechekGL = checkGL(valuedifference, 81)
                maxvalue = maxvalue + (takechekGL *81)
                if(takechekGL < 0):
                    extra = " "
                else:
                    extra = " + "
                finalis = extra + str(takechekGL*81) + finalis
    
    stb = list(finalis)
    if(islessthanzero == 1):
        for i in range (0, len(stb)):
            if(stb[i] == '+'):
                stb[i] = "-"
        value = -value
    if(stb[0] == '+'):
        stb[0] = ' '
    elif(stb[1]== '+'):
        stb[1] = ' '
    "".join(stb)
    print(str(stb))
            
abc(value)

    