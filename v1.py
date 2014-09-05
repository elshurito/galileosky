# -*- coding: utf-8 -*-
from protokol import ParseTitleStr
HeadPack="011780010A024603333536383936303333393332373930048100BBEA"
MainPack1="01178004320020E17ADF52300EAC4F5E0340B610053300004604A2FE"
MainPack2="01178004320020E17ADF52300EAC4F5E0340B610053300004604A2FE"

def AnswerHeadPack(HP):
    #title
    headPackTitle = HP[0:2]
    #length
    headPackLength=int((HP[4:6]+HP[2:4])[1:4], 16)
    #checksum
    checksum=HP[(headPackLength+3)*2:(headPackLength+3)*2+4]
    #answer
    answer='02'+str(checksum)

    returnHP=[headPackLength, headPackLength, checksum, answer]
    return returnHP

def AnswerMainPack(MP):
    ReturnMP=AnswerHeadPack(MP)
    #package
    package=MP[6:(ReturnMP[1]+3)*2]
    ReturnMP.append(package)
    TagData={}
    while len(package) > 0:
        package=ParseTitleStr(package)


    return ReturnMP


print(AnswerHeadPack(HeadPack))
print(AnswerMainPack(MainPack1))
