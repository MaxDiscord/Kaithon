import sys
import random
import time
import win32create as w32
class NoEqEq(Exception):
    pass
class NoEnd(Exception):
    pass
class NoParens(Exception):
    pass
global prev
varName = []
varCont = []
lsts = []
mth = False
line=0
br = False
f = open ("ky.kyt","r")
log = open ("kycache.kyc","w")
a = f.read()
ad = a.split("\n")
while br == False:
    link = line + 1
    lin = str(link)
    rage = "Parsed " + lin
    log.write(rage)
    log.write("\n")
    mth = False
    il = ad[line].split()
    if "var" == il[0]:
        vName = il[1]
        vVal = il[3]
        eqeq = il[2]
        if "="  != eqeq:
            noek = "No Equals LINE " + lin
            log.write (noek)
            log.close()
            raise NoEqEq("No Equals",line)
        else:
            if "*" in il or "/" in il or "+" in il or "-" in il:
                if il[3] not in varName:
                    il[3] = float(il[3])
                else:
                    xdf = varName.index(il[3])
                    xaf = varCont[xdf]
                if il[5] not in varName:
                    il[5] = float(il[5])
                else:
                    cdf = varName.index(il[5])
                    caf = varCont[cdf]
                    xaf = float(xaf)
                    caf = float(caf)
                    answd = xaf + caf
                    varName.append(il[1])
                    varCont.append(answd)

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
            if parnn[0] in varName:
                rob = varName.index(parnn[0])
                bst = varCont[rob]
                bst = str(bst)
                print (bst)
            else:
                #strippedofparens = il[2].split(")")
                #strippedofparenss = "'" + strippedofparens[0] + "'"
                #print (strippedofparenss)
                bart = lsts.index(il[2])
                bart = bart + 1
                print (lsts[bart])
    elif "if" == il[0]:
        eckeck = il[2]
        if eckeck != "=":
            noeq = "No Equals ",lin
            log.write(noeq)
            log.close()
            raise NoEqEq("No equals",line)
        else:
            v1 = il[1]
            rock = varName.index(v1)
            v1 = varCont[rock]
            v2 = il[3]
            if v2 not in varName:
                v2 = int(v2)
                if v1 == v2:
                    global intulhere
                    intulhere = 0
                    for x in range(line+1,len(ad)):
                        if ad[x] =="}":
                            intulhere=x
                    if intulhere ==0:
                        noendo = "No End To If Statement "+lin
                        log.write(noendo)
                        log.close()
                        raise NoEnd("No end to IF")
            else:
                stick = varName.index(v2)
                v2 = varCont[stick]
                if v1 != v2:
                    global untilhere
                    untilhere=0
                    for x in range(line+1,len(ad)):
                        if ad[x]=="}":
                            untilhere=x
                    if untilhere==0:
                        noendof = "No End To If Statement "+lin
                        log.write(noendof)
                        log.close()
                        raise NoEnd("No end to IF",line)
                    line=line+(untilhere-line)
    elif "input" == il[0]:
        nameovar = il[1]
        ract = ad[line].split('"')
        response = input(ract[1])
        varName.append(nameovar)
        varCont.append(response)
        response = ""
    elif "integ" == il[0]:
        integify = varName.index(il[1])
        varCont[integify] = int(varCont[integify])
    elif "strin" == il[0]:
        strinify = varName.index(il[1])
        varCont[strinify] = str(varCont[strinify])
    elif "bool" == il[0]:
        boolify = varName.index(il[1])
        varCont[boolify] = bool(varCont[boolify])
    elif "flt" == il[0]:
        floatify = varName.index(il[1])
        varCont[floatify] = float(varCont[floatify])
    elif "type" == il[0]:
        tip = varName.index(il[2])
        asgn = il[1]
        varName.append(asgn)
        if type(varCont[tip]) == str:
            varCont.append("strin")
        elif type(varCont[tip]) == int:
            varCont.append("integ")
        elif type(varCont[tip]) == float:
            varCont.append("flt")
        elif type(varCont[tip]) == bool:
            varCont.append("bool")
    elif "lst" == il[0]:
        lsts.append(il[1])
        lsts.append([])
    elif "append" == il[0]:
        listToAppendOn = il[1]
        varToAppend = il[2]
        listAppendIndex = lsts.index(listToAppendOn)
        varToAppendIndex = varName.index(varToAppend)
        lsts[listAppendIndex+ 1].append(varCont[varToAppendIndex])



    if ad[line + 1] == "":
        log.close()
        sys.exit()
    line=line+1
    if line == len(ad):
        br = True
        #wait
