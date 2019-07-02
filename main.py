import sys
import random
import time
class NoEqEq(Exception):
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
            raise NoEqEq("No Equals")
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
                varName.append(vName)
                varCont.append(vVal)                                     
            varName.append(vName)
            varCont.append(vVal)
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
            print (content)
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
            if '"' in bst:
                b = bst.split('"')
                print (b[1])
            else:
                print (bst)
        
    line=line+1
    if line == len(ad):
        br = True
