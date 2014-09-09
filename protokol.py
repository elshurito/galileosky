import datetime
import time

heshHex={
    0x01:1, 0x02:1, 0x03:15, 0x04:2, 0x10:2,
    0x20:4, 0x30:9, 0x33:4, 0x34:2, 0x35:1,
    0x40:2, 0x41:2, 0x42:2, 0x43:1, 0x44:4,
    0x45:2, 0x46:2, 0x50:2, 0x51:2, 0x52:2,
    0x53:2, 0x58:2, 0x59:2, 0x70:2, 0x71:2,
    0x72:2, 0x73:2, 0x74:2, 0x75:2, 0x76:2,
    0x77:2, 0x90:4, 0xc0:4, 0xc1:4, 0xc2:4,
    0xc3:4, 0xc4:1, 0xc5:1, 0xc6:1, 0xc7:1,
    0xc8:1, 0xc9:1, 0xca:1, 0xcb:1, 0xcc:1,
    0xcd:1, 0xce:1, 0xcf:1, 0xd0:1, 0xd1:1,
    0xd2:1, 0xd3:4, 0xd4:4, 0xd5:1, 0xd6:2,
    0xd7:2, 0xd8:2, 0xd9:2, 0xda:2, 0xdb:4,
    0xdc:4, 0xdd:4, 0xde:4, 0xdf:4, 0x80:3,
    0x81:3, 0x82:3, 0x83:3, 0x84:3, 0x85:3,
    0x86:3, 0x87:3, 0x60:2, 0x61:2, 0x62:2,
    0x88:1, 0x89:1, 0x8A:1, 0x8B:1, 0x8C:1,
    0xA0:1, 0xA1:1, 0xA2:1, 0xA3:1, 0xA4:1,
    0xA5:1, 0xA6:1, 0xA7:1, 0xA8:1, 0xA9:1,
    0xAA:1, 0xAB:1, 0xAC:1, 0xAD:1, 0xAE:1,
    0xAF:1, 0xB0:2, 0xB1:2, 0xB2:2, 0xB3:2,
    0xB4:2, 0xB5:2, 0xB6:2, 0xB7:2, 0xB8:2,
    0xB9:2, 0xF0:4, 0xF1:4, 0xF2:4, 0xF3:4,
    0xF4:4, 0xF5:4, 0xF6:4, 0xF7:4, 0xF8:4,
    0xF9:4, 0x5A:4, 0x5B:4, 0x47:4, 0x5C:68,
}
heshStr={
    '01':1, '02':1, '03':'a0001', '04':'a0002', '10':2,
    '20':'a0003', '30':'a0004', '33':4, '34':'a0005', '35':1,
    '40':2, '41':2, '42':2, '43':1, '44':4,
    '45':2, '46':2, '50':2, '51':2, '52':2,
    '53':2, '58':2, '59':2, '70':2, '71':2,
    '72':2, '73':2, '74':2, '75':2, '76':2,
    '77':2, '90':4, 'c0':4, 'c1':4, 'c2':4,
    'c3':4, 'c4':1, 'c5':1, 'c6':1, 'c7':1,
    'c8':1, 'c9':1, 'ca':1, 'cb':1, 'cc':1,
    'cd':1, 'ce':1, 'cf':1, 'd0':1, 'd1':1,
    'd2':1, 'd3':4, 'd4':4, 'd5':1, 'd6':2,
    'd7':2, 'd8':2, 'd9':2, 'da':2, 'db':4,
    'dc':4, 'dd':4, 'de':4, 'df':4, '80':3,
    '81':3, '82':3, '83':3, '84':3, '85':3,
    '86':3, '87':3, '60':2, '61':2, '62':2,
    '88':1, '89':1, '8A':1, '8B':1, '8C':1,
    'A0':1, 'A1':1, 'A2':1, 'A3':1, 'A4':1,
    'A5':1, 'A6':1, 'A7':1, 'A8':1, 'A9':1,
    'AA':1, 'AB':1, 'AC':1, 'AD':1, 'AE':1,
    'AF':1, 'B0':2, 'B1':2, 'B2':2, 'B3':2,
    'B4':2, 'B5':2, 'B6':2, 'B7':2, 'B8':2,
    'B9':2, 'F0':4, 'F1':4, 'F2':4, 'F3':4,
    'F4':4, 'F5':4, 'F6':4, 'F7':4, 'F8':4,
    'F9':4, '5A':4, '5B':4, '47':4, '5C':68,
}
def ParseTitleStr(package):
    str(package).upper()
    title=package[0:2]
    lengthPackage=heshStr.get(title)
    print(package)
    package=package[2+2*(int(lengthPackage)):]
    return package

def ClearPackage(x,lenx):
    return x[2+2*lenx:]

def ParseTitleBoolen(package):
    str(package).upper()
    title=package[0:2]
    lengthPackage=heshStr.get(title)
    if lengthPackage == 'a0001':
        code='a0001'
    elif lengthPackage == 'a0002':
        code='a0002'
    elif lengthPackage == 'a0003':
        code='a0003'
    elif lengthPackage == 'a0004':
        code='a0004'
    else:
        code = lengthPackage
    return code

def IMEI(package):
    #codeHex=0x03
    #codeStr='03'
    packageLength=15
    return package[2:packageLength*2+2].decode("hex")

def ID(package):
    #codeHex=0x04
    #codeStr='04'
    #packageLength=2
    return int(package[4:6]+package[2:4], 16)

def DT(package):
    #codeHex=0x20
    #codeStr='20'
    #packageLength=4
    return datetime.datetime.fromtimestamp(int(package[8:10]+package[6:8]+package[4:6]+package[2:4] ,16))

def Coordinates(package):
    #codeHex=0x30
    #codeStr='30'
    #packageLength=9
    if package[2]=='0':
        correct=True
    else:
        correct=False

    NumOfSattelite = int(package[3], 16)
    Latitude=(int(package[10:12]+package[8:10]+package[6:8]+package[4:6], 16))/1000000.0
    Longitude=(int(package[18:20]+package[16:18]+package[14:16]+package[12:14], 16)/1000000.0)
    return correct,NumOfSattelite,Latitude,Longitude

def SpeedDirection(package):
    #codeHex=0x34
    #packageLength=4
    speed=(int(package[4:6]+package[2:4], 16))/10.0
    direction=(int(package[8:10]+package[6:8], 16))/10.0
    return speed, direction