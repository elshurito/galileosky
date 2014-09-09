# -*- coding: utf-8 -*-
from protokol import ParseTitleBoolen, IMEI, ClearPackage, ID, DT, Coordinates, SpeedDirection
HeadPack="011780010A024603333536383936303333393332373930048100BBEA"
MainPack1="01D883043200109D1B20BD7ADF52300BAC4F5E0340B610053300004604500000510000520000530000580000043200109C1B20957ADF523008DC4F5E0360B51005339B004E04500000510000520000530000580000043200109B1B20937ADF523009DC4F5E03A0B51005333C004D0B500000510000520000530000580000043200109A1B20457ADF52300E744F5E0318B61005330000000050000051000052000053000058000004320010991B20CC79DF52300E744F5E0318B61005330000000050000051000052000053000058000004320010981B205279DF52300E744F5E0318B61005330000000050000051000052000053000058000004320010971B20D978DF52300D744F5E0318B61005330000000050000051000052000053000058000004320010961B206078DF52300D744F5E0318B61005330000000050000051000052000053000058000004320010951B20E677DF52300D744F5E0318B61005330000000050000051000052000053000058000004320010941B206D77DF52300D744F5E0318B61005330000000050000051000052000053000058000004320010931B200977DF52300D744F5E0318B61005330000000050000051000052000053000058000004320010921B20F476DF52300D744F5E0318B6100533000000005000005100005200005300005800000432001091"
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
    IMEIValue='null'
    IDValue='null'
    DTValue='null'
    correct='null'
    NumOfSattelite='null'
    Latitude='null'
    Longitude='null'
    speed='null'
    direction='null'
    ReturnMP=AnswerHeadPack(MP)
    #package
    package=MP[6:(ReturnMP[0]+3)*2]
    ReturnMP.append(package)
    while len(package) > 0:
        code=ParseTitleBoolen(package)
        if str(code).isdigit():
            package=package[2+2*(int(code)):]
        else:
            if code == 'a0001':
                #IMEI 0x03
                IMEIValue=IMEI(package)
                package=ClearPackage(package, 15)
            elif code == 'a0002':
                #ID 0x04
                IDValue=ID(package)
                package=ClearPackage(package, 2)
            elif code == 'a0003':
                #DataTime 0x20
                DTValue=DT(package)
                package=ClearPackage(package,4)
            elif code == 'a0004':
                #coordinates
                coordData=Coordinates(package)
                package=ClearPackage(package,9)
                correct=coordData[0]
                NumOfSattelite=coordData[1]
                Latitude=coordData[2]
                Longitude=coordData[3]
            elif code == 'a0005':
                #speed and direction
                speeddirect=SpeedDirection(package)
                package=ClearPackage(package, 4)
                speed=speeddirect[0]
                direction=speeddirect[1]


    ReturnMP.append(IMEIValue)
    ReturnMP.append(IDValue)
    ReturnMP.append(DTValue)
    ReturnMP.append(correct)
    ReturnMP.append(NumOfSattelite)
    ReturnMP.append(Latitude)
    ReturnMP.append(Longitude)
    ReturnMP.append(speed)
    ReturnMP.append(direction)

    return ReturnMP

#AnswerHeadPack
#0-Длина пакета
#1-Контрольная сумма
#2-Ответ, необходимый для отправки
print(AnswerHeadPack(HeadPack))
#
#
#AnswerMainPack
#0-Длина пакета
#1-Контрольная сумма
#2-Ответ
#3-Пакет с нужными данными
#4-IMEI
#5-ID
#6-Дата и время
#7-Верны ли данные True-верны
#8-Количество спутников
#9-Широта
#10-Долгота
#11-Скорость движения (КМ/ч)
#12-Направление в градусах
#                ######

print(AnswerMainPack(MainPack1))
