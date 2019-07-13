import sys
import random
import time
class NoEqEq(Exception):
    pass
class NoEnd(Exception):
    pass
class NoParens(Exception):
    pass
class CannotChangeConstant(Exception):
    pass
global prev
varName = []
varCont = []
constName=[]
constCont=[]
constanted = False
lsts = []
mth = False
line=0
br = False
f = open ("ky.kyt","r")
log = open ("kycache.kyc","w")
a = f.read()
ad = a.split("\n")
il = ad[0].split()
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
        printinglog = "Variable created " + vName + "=" + vVal + "\n"
        log.write(printinglog)
        if "="  != eqeq:
            noek = "No Equals LINE " + lin + "\n"
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
                    answdd = str(answd)
                    mathlog = "Variable created (math)" + il[1] + "=" + answdd + "\n"
                    log.write(mathlog)
                    varName.append(il[1])
                    varCont.append(answd)

                op = il[4]
                if op == "+":
                    answ = il[3] + il[5]
                    varName.append(il[1])
                    varCont.append(answ)
                    answ = str (answ)
                    mathlog = "Variable created (math)" + il[1] + "=" + answ + "\n"
                    log.write(mathlog)
                    mth = True
                elif op == "-":
                    answ = il[3] - il[5]
                    varName.append(il[1])
                    varCont.append(answ)
                    answ = str (answ)
                    mathlog = "Variable created (math)" + il[1] + "=" + answ + "\n"
                    log.write(mathlog)
                    mth = True
                elif op == "*":
                    answ = il[3] * il[5]
                    varName.append(il[1])
                    varCont.append(answ)
                    answ = str (answ)
                    mathlog = "Variable created (math)" + il[1] + "=" + answ + "\n"
                    log.write(mathlog)
                    mth = True
                elif op == "/":
                    answ = il[3] / il[5]
                    varName.append(il[1])
                    varCont.append(answ)
                    answ = str (answ)
                    mathlog = "Variable created (math)" + il[1] + "=" + answ + "\n"
                    log.write(mathlog)
                    mth = True
            if il[1] in varName and mth == False:
                dvar = varName.index(vName)
                dcont = varCont.index(prev)
                del varName[dvar]
                del varCont[dcont]
                global vValue
                vValue = vVal.split('"')
                varName.append(vName)
                if len (vValue) == 1:
                    varCont.append(vValue[0])
                else:
                    varCont.append(vValue[1])
            vValue = vVal.split('"')
            varName.append(vName)
            if len(vValue) == 1:
                varCont.append(vValue[0])
                repls = "Variable " + il[1] + " Replaced\n"
                log.write(repls)
            else:
                varCont.append(vValue[1])
                repls = "Variable " + il[1] + " Replaced\n"
                log.write(repls)
            prev = vVal
    elif "delvar" == il[0]:
        varToDel = varName.index(il[1])
        varToDel = int(varToDel)
        deletvar = "Variable Deleted " + il[1] + "\n"
        log.write(deletvar)
        del varName[varToDel]
        del varCont[varToDel]
    elif "console.println" == il[0]:
        num = il[1].split("(")
        numba = num[1].split(")")
        if numba[0] in constName:
            printConst = constName.index(numba[0])
            print (constCont[printConst])
            constanted = True
        if '"' in il[1] and constanted == False:
            content=""
            for x in range(1,len(il)):
                content=content+il[x]+" "
            cat = content.split('"')
            printlog = "Printed " + cat[1] + "\n"
            log.write (printlog)
            print (cat[1])
        if '"' not in il[1] and constanted == False:
            parens = ad[line].split("(")
            parens = str(parens)
            paren = parens.split(")")
            paren = str(paren)
            parn = paren.split("'")
            parnn = parn[3].split('"')
            if parnn[0] in varName and constanted == False:
                rob = varName.index(parnn[0])
                bst = varCont[rob]
                bst = str(bst)
                varprint = "Printed Var " + bst
                log.write(varprint)
                print (bst)
            if parnn[0] not in varName:
                if constanted == False:
                    print ("insli")
                    nopanren = il[1].split(")")
                    noopen = nopanren[0].split("(")
                    bart = lsts.index(noopen[1])
                    bart = bart + 1
                    listprint = "Printed List Entry" + lsts[bart] + "\n"
                    print (lsts[bart])
                else:
                    pass
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
                    correctif = "If statement success " + v1 + " = " + v2 + "\n"
                    log.write(correctif)
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
                    incorrectif = "If statement failed " + v1 + " != " + v2 + "\n"
                    log.write(incorrectif)
                    global untilhere
                    untilhere=0
                    for x in range(line+1,len(ad)):
                        if ad[x]=="}":
                            untilhere=x
                    if untilhere==0:
                        noendof = "No End To If Statement "+lin + "\n"
                        log.write(noendof)
                        log.close()
                        raise NoEnd("No end to IF",line)
                    line=line+(untilhere-line)
    elif "console.req_input" == il[0]:
        nameovar = il[1]
        ract = ad[line].split('"')
        response = input(ract[1])
        loginput = "Input asked, Response: " + response + "\n"
        log.write (loginput)
        varName.append(nameovar)
        varCont.append(response)
        response = ""
    elif "integ" == il[0]:
        integify = varName.index(il[1])
        varCont[integify] = int(varCont[integify])
        integlog = "var " + il[1] + " changed type to integ\n"
    elif "strin" == il[0]:
        strinify = varName.index(il[1])
        varCont[strinify] = str(varCont[strinify])
        strinlog = 0
    elif "bool" == il[0]:
        boolify = varName.index(il[1])
        varCont[boolify] = bool(varCont[boolify])
        boolog = 0
    elif "flt" == il[0]:
        floatify = varName.index(il[1])
        varCont[floatify] = float(varCont[floatify])
        floatlog = 0
    elif "type" == il[0]:
        tip = varName.index(il[2])
        asgn = il[1]
        varName.append(asgn)
        if type(varCont[tip]) == str:
            varCont.append("strin")
            typestrin
        elif type(varCont[tip]) == int:
            varCont.append("integ")
            typeinteg
        elif type(varCont[tip]) == float:
            varCont.append("flt")
            typeflt
        elif type(varCont[tip]) == bool:
            varCont.append("bool")
            typebool
    elif "lst" == il[0]:
        lsts.append(il[1])
        lsts.append([])
    elif "append" == il[0]:
        listToAppendOn = il[1]
        varToAppend = il[2]
        listAppendIndex = lsts.index(listToAppendOn)
        varToAppendIndex = varName.index(varToAppend)
        lsts[listAppendIndex+ 1].append(varCont[varToAppendIndex])
    elif "dlt" == il[0]:
        fatman = varName.index(il[2])
        vDel = lsts.index(il[1])
        vDel = vDel+1
        del lsts[vDel][fatman]
    elif "uppr" == il[0]:
        uVar = varName.index(il[1])
        upperedVar = varCont[uVar].upper()
        beforing = varName[uVar]
        del varName[uVar]
        del varCont[uVar]
        varName.append(beforing)
        varCont.append(upperedVar)
    elif "lowr" == il[0]:
        if il[1] in varName:
            lVar = varName.index(il[1])
            print (varCont[lVar])
            loweredVar = varCont[lVar].lower()
            beforring = varName[lVar]
            del varName[lVar]
            del varCont[lVar]
            varName.append(beforring)
            varCont.append(loweredVar)
    elif "using" == il[0]:
        if il[1] == "time":
            import timea
        elif il[1] == "w32":
            import win32create as w32
        elif il[1] == "random":
            from rndm import *
    elif "time.delay"==il[0]:
        il[1] = int(il[1])
        timea.sleep(il[1])
    elif "time.cTime"==il[0]:
        timea.currentTime()
    elif "random.randnum"== il[0]:
        import random
        il[1] = int (il[2])
        il[2] = int (il[3])
        z=random.randint(il[2],il[3])
        varName.append(il[1])
        varCont.append(z)
    elif "len" == il[0]:
        ListForLen = il[3]
        ListPlacementForLen = ListForLen.index(ListForLen)
        equals = il[2]
        varToAssign = il[1]
        lenny = len(lsts[ListPlacementForLen + 1])
        if equals != "=":
            raise NoEqEq ("No Equals for Len")
        else:
            varName.append(varToAssign)
            varCont.append(lenny)
    elif "const" == il[0]:
        if il[1] in constName:
            raise CannotChangeConstant ("Cannot change value of constant")
        else:
            constAddName = il[1]
            constAddContent = il[3]
            equalss = il[2]
            if equalss != '=':
                log.write("No Equals for Constant")
                raise NoEqEq ("No Equals for Constant")
            else:
                constName.append(constAddName)
                constCont.append(constAddContent)
    elif "index" == il[0]:
        varToCreate = il[1]
        equalz = il[2]
        otherindexzone = il[3]
        otherindezone = otherindexzone.split(",")
        ListToIndex = lsts.index(otherindezone[0])
        ListToIndex = ListToIndex + 1
        varToIndex = varName.index(otherindezone[1])
        varToInde = varCont[varToIndex]
        indexReturn = lsts[ListToIndex].index(varToInde)
        varName.append(varToCreate)
        varCont.append(indexReturn)


    if line + 1 == len(ad):
        br = True
        #wait
        log.close()
        sys.exit()
    if ad[line+1] == "":
        log.close()
        sys.exit()
    line=line+1
