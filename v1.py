# -*- coding: utf-8 -*-
from protokol import ParseTitleBoolen, IMEI, ClearPackage, ID
HeadPack="011780010A024603333536383936303333393332373930048100BBEA"
MainPack1="011780010A024603333536383936303333393332373930048100BBEA"
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

    returnHP=[headPackLength, checksum, answer]
    return returnHP

def AnswerMainPack(MP):
    ReturnMP=AnswerHeadPack(MP)
    #package
    package=MP[6:(ReturnMP[0]+3)*2]
    ReturnMP.append(package)
    TagData={}
    while len(package) > 0:
        code=ParseTitleBoolen(package)
        if str(code).isdigit():
            package=package[2+2*(int(code)):]
        else:
            if code == 'a0001':
                #IMEI 0x03
                IMEIValue=IMEI(package)
                package=ClearPackage(package, 15)
                print(IMEIValue)
                print(package)
            elif code == 'a0002':
                #ID 0x04
                IDValue=ID(package)
                package=ClearPackage(package, 2)
                print IDValue
            elif code == 'a0003':
                #DataTime
                pass
            elif code == 'a0004':
                #coordinates
                pass
            elif code == 'a0005':
                #speed
                pass

    return ReturnMP


print(AnswerHeadPack(HeadPack))
print(AnswerMainPack(MainPack1))
