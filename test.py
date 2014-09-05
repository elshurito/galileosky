# -*- coding: utf-8 -*-
inputStr='011780010A024603333536383936303333393332373930048100BBEA'
#headPack
headPackStr=inputStr;
#title
headPackTitle=headPackStr[0:2]
lengthPack=headPackStr[4:6]+headPackStr[2:4]
#Неотправленные данные
unsendData=True;
if lengthPack[0]=='0':
    unsendData=False
else:
    unsendData=True
print(unsendData)

#mainPack
#mainPack2
