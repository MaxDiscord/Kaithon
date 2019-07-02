#kaithon
import sys
import random
import time
counts = 0
import turtle
#ALL TURTLE
#MAKE SENDFALSE
#MAKE SENDTRUE
def makePen():
    global t
    t = turtle.Turtle()
def makeWindow():
    global wn
    wn = turtle.Screen()
    wn.title("KaithonGraphics")
def pColor(color):
    t.pencolor(color)
def pSize(px):
    t.pensize(px)
def fwd(px):
    t.forward(px)
def lft(dgs):
    t.left(dgs)
def rgt(dgs):
    t.right(dgs)
def bak(px):
    t.backward(px)
def wnTitle(title):
    wn.title(title)
def pnup():
    t.penup()
def pdn():
    t.pendown()
def hdePn():
    t.hideturtle()
def shwPn():
    t.showturtle()
def pSeen():
    if t.isvisible == False:
        sndFalse()
    else:
        sndTrue()

im = ["wd","time","misc"]
class NoEqEq(Exception):
    pass
class ModuleNotFound(Exception):
    pass
global prev
varName = []
varCont = []
mth = False
inpaca = False
line=0
br = False
f = open ("ky.kyt","r")
a = f.read()
ad = a.split("\n")
if a == "":
    br = True
while br == False:
    mth = False
    #remember to del line at end of funcs
    il = ad[line].split()
    if "var" == il[0]:
        if il[2] == "input":
            question = il[4]
            varName.append(il[1])
            ekek = il[3]
            if "=" != ekek:
                raise NoEqEq("No equals")
            else:
                response = input (question)
                varCont.append(response)
                inpaca = True
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
        if inpaca == False:
            ct = ""
            ick = str(il)
            nammen = ick.split('"')
            for x in range(1,len(il)):
                ct=ct+il[x]+" "
            d = ct.split('"')
            varCont.append(d[1])
            varName.append(il[1])
            eqeq = il[2]
            if "="  != eqeq:
                raise NoEqEq("No Equals")
            
    elif "delvar" == il[0]:
        varToDel = il[1]
        racksack = varName.index(varToDel)
        del varName[racksack]
        del varCont[racksack]
    elif "p" == il[0]:               
        if '"' in il[1]:
            content =""
            for x in range(1,len(il)):
                content=content+il[x]+" "
            c = content.split('"')
            print (c[1])
        else:
            ill = str(il)
            STR = ill.split('"')
            char = "'"
            r = STR[0].split("'")
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
    elif "var.list" == il[0]:
        print (varName)
        print (varCont)
 
        
    line=line+1
    if line == len(ad):
        br = True
if br == True:
    print ("Thanks for using Kaithon")
