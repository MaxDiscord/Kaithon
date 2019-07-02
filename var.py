#variable creation section of Kaithon
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
