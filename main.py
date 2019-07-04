import sys
import random
import time
class NoEqEq(Exception):
    pass
class NoEnd(Exception):
    pass
global prev
varName = []
varCont = []
mth = False
line=0
br = False
f = open ("ky.kyt","r")
a = f.read()
ad = a.split("\n")
while br == False:
    mth = False
    #remember to del line at end of funcs
    il = ad[line].split()
    if "var" == il[0]:
        vName = il[1]
        vVal = il[3]
        eqeq = il[2]
        if "="  != eqeq:
            raise NoEqEq("No Equals",line)
        else:
            if "*" in il or "/" in il or "+" in il or "-" in il:
                il[3] = int(il[3])
                il[5] = int(il[5])
                op = il[4]
                if op == "+":
                    answ = il[3] + il[5]
                    varName.append(il[1])
                    varCont.append(answ)
                    mth = True
                elif op == "-": 
                    answ = il[3] - il[5]
                    varName.append(il[1])
                    varCont.append(answ)
                    mth = True
                elif op == "*":
                    answ = il[3] * il[5]
                    varName.append(il[1])
                    varCont.append(answ)
                    mth = True
                elif op == "/":
                    answ = il[3] / il[5]
                    varName.append(il[1])
                    varCont.append(answ)
                    mth = True
            if il[1] in varName and mth == False:
                dvar = varName.index(vName)
                dcont = varCont.index(prev)
                del varName[dvar]
                del varCont[dcont]
                global vValue
                vValue = vVal.split('"')
                varName.append(vName)
                varCont.append(vValue[1])
            vValue = vVal.split('"')
            varName.append(vName)
            if len(vValue) == 1:
                varCont.append(vValue[0])
            else:
                varCont.append(vValue[1])
            prev = vVal
    elif "delvar" == il[0]:
        varToDel = il[1]
        varToDel = int(varToDel)
        del varName[varToDel]
        del varCont[varToDel]
    elif "p" == il[0]:
        if '"' in il[1]:
            content=""
            for x in range(1,len(il)):
                content=content+il[x]+" "
            cat = content.split('"')
            print (cat[1])
        else:
            parens = ad[line].split("(")
            parens = str(parens)
            paren = parens.split(")")
            paren = str(paren)
            parn = paren.split("'")
            parnn = parn[3].split('"')
            rob = varName.index(parnn[0])
            bst = varCont[rob]
            bst = str(bst)
            print (bst)
    elif "if" == il[0]:
        eckeck = il[2]
        if eckeck != "=":
            raise NoEqEq("No equals",line)
        else:
            v1 = il[1]
            rock = varName.index(v1)
            v1 = varCont[rock]
            v2 = il[3]
            #peen = v2.split('"')
            stick = varName.index(v2)
            v2 = varCont[stick]
            if v1 != v2:
                global untilhere
                untilhere=0
                for x in range(line+1,len(ad)):
                    if ad[x]=="}":
                        untilhere=x
                if untilhere==0:
                    raise NoEnd("No end to IF",line)
                line=line+(untilhere-line)
    elif "input" == il[0]:
        nameovar = il[1]
        ract = ad[line].split('"')
        response = input(ract[1])
        varName.append(nameovar)
        varCont.append(response)
        response = ""
    
        
    line=line+1
    if line == len(ad):
        br = True
        #wait
