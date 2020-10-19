'''
UBX Protocol payload definitions

THESE ARE THE PAYLOAD DEFINITIONS FOR _GET_ MESSAGES _FROM_ THE RECEIVER
(i.e. Periodic Navigation Data, Poll Responses, Info messages)

NB: Attribute names must be unique within each message class/id

NB: Repeating groups must be defined as a tuple thus: 
    'group': ('numr', {dict})
    where 
    - 'numr' is the name of the preceding attribute containing the number
       of repeats, or 'None' if there isn't one
    - {dict} is the nested dictionary containing the repeating attributes

Created on 27 Sep 2020

@author: semuadmin
'''
# pylint: disable=unused-import, too-many-lines

from pyubx2.ubxtypes_core import U1, I1, X1, U2, I2, X2, U3, U4, I4, U5, \
                                X4, R4, U6, X6, R8, U8, U12, U40, U64, C06, \
                                C10, C30, C32, CH

UBX_PAYLOADS_GET = {
'ACK-ACK': {
'clsID': U1,
'msgID': U1
},
'ACK-NAK': {
'clsID': U1,
'msgID': U1
},
# ********************************************************************
'AID-ALM': {
'svid': U4,
'week': U4,
'optBlock': {
'dwrd': U4
}},
'AID-AOP' : {
'gnssId': U1,
'svId': U1,
'reserved1': U2,
'data': U64
},
'AID-EPH' : {
'svid': U1,
'how': U4,
'optBlock': {
'sf1d1': U4,
'sf1d2': U4,
'sf1d3': U4,
'sf1d4': U4,
'sf1d5': U4,
'sf1d6': U4,
'sf1d7': U4,
'sf1d8': U4,
'sf2d1': U4,
'sf2d2': U4,
'sf2d3': U4,
'sf2d4': U4,
'sf2d5': U4,
'sf2d6': U4,
'sf2d7': U4,
'sf2d8': U4,
'sf3d1': U4,
'sf3d2': U4,
'sf3d3': U4,
'sf3d4': U4,
'sf3d5': U4,
'sf3d6': U4,
'sf3d7': U4,
'sf3d8': U4,
}},
'AID-HUI': {
'health': X4,
'utcA0': R8,
'utcA1': R8,
'utcTOW': I4,
'utcWNT': I2,
'utcLS': I2,
'utcWNF': I2,
'utcDNs': I2,
'utcLSF': I2,
'utcSpare': I2,
'klobA0': R4,
'klobA1': R4,
'klobA2': R4,
'klobA3': R4,
'klobB0': R4,
'klobB1': R4,
'klobB2': R4,
'klobB3': R4,
'flags': X4
},
'AID-INI': {
'ecefXOrLat': I4,
'ecefYOrLon': I4,
'ecefZOrAlt': I4,
'posAcc': U4,
'tmCfg': X2,
'wn': U2,
'tow': U4,
'towNs': I4,
'tAccMs': U4,
'tAccNs': U4,
'clkDOrFreq': I4,
'clkDAccOrFreqAcc': U4,
'flags': X4
},
# ********************************************************************
'CFG-ANT': {
'flags': X2,
'pins': X2
},
'CFG-CFG': {
'clearMask': X4,
'saveMask' : X4,
'loadMask': X4,
'deviceMask': X1
},
'CFG-DAT':{
'datumNum': U2,
'datumName': C06,
'majA': R8,
'flat': R8,
'dX': R4,
'dY': R4,
'dZ': R4,
'rotX': R4,
'rotY': R4,
'rotZ': R4,
'scale': R4
},
'CFG-DOSC': {
'version': U1,
'numOsc': U1,
'reserved1': U2,
'group': ('numOsc',{  # repeating group * numOsc
'oscId': U1,
'reserved2': U1,
'flags': X2,
'freq': U4,
'phaseOffset': I4,
'withTemp': U4,
'withAge': U4,
'timeToTemp': U2,
'reserved3': U1[2],
'gainVco': I4,
'gainUncertainty': U1,
'reserved4': U3
})},
'CFG-DYNSEED': {
'version': U1,
'reserved1': U3,
'seedHi': U4,
'seedLo': U4
},
'CFG-ESRC': {
'version': U1,
'numSources': U1,
'reserved1': U2,
'group': ('numSources',{  # repeating group * numSources
'extInt': U1,
'flags': X2,
'freq': U4,
'reserved2': U4,
'withTemp': U4,
'withAge': U4,
'timeToTemp': U2,
'maxDevLifeTim': U2,
'offset': I4,
'offsetUncertainty': U4,
'jitter': U4
})},
'CFG-FIXSEED': {
'version': U1,
'length': U1,
'reserved1': U2,
'seedHi': U4,
'seedLo': U4,
'group': ('length',{  # repeating group * length
'classId': U1,
'msgId': U1
})},
'CFG-GEOFENCE': {
'version': U1,
'numFences': U1,
'confLvl': U1,
'reserved1': U1[1],
'pioEnabled': U1,
'pinPolarity': U1,
'pin': U1,
'reserved2': U1[1],
'group': ('numFences',{  # repeating group * numFences
'lat': I4,
'lon': I4,
'radius': U4
})},
'CFG-GNSS': {
'msgVer': U1,
'numTrkChHw': U1,
'numTrkChUse': U1,
'numConfigBlocks': U1,
'group': ('numConfigBlocks', {  # repeating group * numConfigBlocks
'gnssId': U1,
'resTrkCh': U1,
'maxTrkCh': U1,
'reserved1': U1,
'flags': X4
})},
'CFG-INF': {
'protocolID': U1,
'reserved1': U3,
'infMsgMaskDDC': X1,
'infMsgMaskUART1': X1,
'infMsgMaskUART2': X1,
'infMsgMaskUSB': X1,
'infMsgMaskSPI': X1,
'reserved2': X1
},
'CFG-ITFM': {
'config': X4,
'config2': X4
},
'CFG-LOGFILTER': {
'version': U1,
'flags': X1,
'minInterval': U2,
'timeThreshold': U2,
'speedThreshold': U2,
'positionThreshold': U4
},
'CFG-MSG': {
'msgClass': U1,
'msgID': U1,
'rateDDC': U1,
'rateUART1': U1,
'rateUART2': U1,
'rateUSB': U1,
'rateSPI': U1,
'reserved': U1
},
'CFG-NAV5': {
'mask': X2,
'dynModel': U1,
'fixMode': U1,
'fixedAlt': I4,
'fixedAltVar': U4,
'minElev': I1,
'drLimit': U1,
'pDop': U2,
'tDop': U2,
'pAcc': U2,
'tAcc': U2,
'staticHoldThresh': U1,
'dgpsTimeOut': U1,
'reserved2': U4,
'reserved3': U4,
'reserved4': U4
},
'CFG-NAVX5': {
'mask1': X2,
'reserved0': U4,
'reserved1': U1,
'reserved2': U1,
'minSVs': U1,
'maxSVs': U1,
'minCNO': U1,
'reserved5': U1,
'iniFix3D': U1,
'reserved6': U1,
'reserved7': U1,
'reserved8': U1,
'wknRollover': U2,
'reserved9': U1,
'reserved10': U1,
'reserved11': U1,
'usePPP': U1,
'useAOP': U1,
'reserved12': U1,
'reserved13': U1,
'aopOrbMaxErr': U2,
'reserved3': U4,
'reserved4': U4
},
'CFG-NMEA': {
'filter': X1,
'version': U1,
'numSV': U1,
'flags': X1
},
'CFG-ODO': {
'version': U1,
'reserved1': U3,
'flags': U1,
'odoCfg': X1,
'reserved2': U6,
'cogMaxSpeed': U1,
'cogMaxPosAcc': U1,
'reserved3': U2,
'velLpGain': U1,
'cogLpGain': U1,
'reserved4': U2
},
# 'CFG-EKF': {
# 'disableEkf': U1,
# 'actionFlags': X1,
# 'configFlags': U1,
# 'inverseFlags': X1,
# 'reserved2': U4,
# 'nomPPDist': U2,
# 'nomZero': U2,
# 'nomSens': U1,
# 'rmsTemp': U1,
# 'tempUpdate': U2
# },
# 'CFG-ESFGWT': {
# 'flags':X2,
# 'id': U2,
# 'wtFactor': U4,
# 'reserved1': U4,
# 'wtQuantError': U4,
# 'timeTagFactor': U4,
# 'wtCountMax': U4,
# 'timeTagMax': U4,
# 'wtLatency': U2,
# 'reserved2': U2,
# 'wtFrequency': U1,
# 'reserved3': U1,
# 'speedDeadBand': U2,
# 'reserved4': U4,
# 'reserved5': U4
# },
'CFG-PM2': {
'version': U1,
'reserved1': U1,
'reserved2': U1,
'reserved3': U1,
'flags': X4,
'updatePeriod': U4,
'searchPeriod': U4,
'gridOffset': U4,
'onTime': U2,
'minAcqTime': U2,
'reserved4': U2,
'reserved5': U2,
'reserved6': U4,
'reserved7': U4,
'reserved8': U1,
'reserved9': U1,
'reserved10': U2,
'reserved11': U4
},
# 'CFG-PM':{
# 'version': U1,
# 'reserved1': U1,
# 'reserved2': U1,
# 'reserved3': U1,
# 'flags': X4,
# 'updatePeriod': U4,
# 'searchPeriod': U4,
# 'gridOffset': U4,
# 'onTime': U2,
# 'minAcqTime': U2
# },
'CFG-PMS': {
'version': U1,
'powerSetupValue': U1,
'period': U2,
'onTime': U2,
'reserved1': U2
},
'CFG-PRT': {
'portID': U1,
'reserved0': U1,
'txReady': X2,
'mode': X4,
'baudRate': U4,
'inProtoMask': X2,
'outProtoMask': X2,
'reserved4': U2,
'reserved5': U2
},
'CFG-PWR': {
'version': U1,
'reserved1': U3,
'state': U4
},
'CFG-RATE': {
'measRate': U2,
'navRate': U2,
'timeRef': U2
},
'CFG-RINV': {
'flags': X1,
'group': ('None',{  # repeating group
'data': U1
})},
'CFG-RST': {
'navBbrMask': X2,
'resetMode': U1,
'reserved1': U1
},
'CFG-RXM': {
'reserved1': U1,
'lpMode': U1
},
'CFG-SBAS': {
'mode': X1,
'usage': X1,
'maxSBAS': U1,
'scanmode2': X1,
'scanmode1': X4
},
'CFG-SMGR': {
'minGNSSFix' : U1,
'maxFreqChange': U2,
'maxPhaseCorrRate': U2,
'reserved1': U2,
'freqTolerance' : U2,
'timeTolerance': U2,
'messageCfg': X2,
'maxSlewRate': U2,
'flags': X4
},
'CFG-TMODE2': {
'timeMode': U1,
'reserved1': U1,
'flags': X2,
'ecefXOrLat': I4,
'ecefYOrLon': I4,
'ecefZOrAlt': I4,
'fixedPosAcc': U4,
'svinMinDur': U4,
'svinAccLimit': U4
},
# 'CFG-TMODE': {
# 'timeMode': U4,
# 'fixedPosX': I4,
# 'fixedPosY': I4,
# 'fixedPosZ': I4,
# 'fixedPosVar': U4,
# 'svinMinDur': U4,
# 'svinAccLimit': U4
# },
'CFG-TP5': {
'tpIdx': U1,
'reserved0': U1,
'reserved1': U2,
'antCableDelay': I2,
'rfGroupDelay': I2,
'freqPeriod': U4,
'freqPeriodLock': U4,
'pulseLenRatio': U4,
'pulseLenRatioLock': U4,
'userConfigDelay': I4,
'flags': X4
},
# 'CFG-TP': {
# 'internal': U4,
# 'length': U4,
# 'status': I1,
# 'timeRef': U1,
# 'flags': U1,
# 'reserved1': U1,
# 'antCableDelay': I2,
# 'rfGroupDelay': I2,
# 'userDelay': I4
# },
'CFG-TXSLOT': {
'version': U1,
'enable': X1,
'refTp': U1,
'reserved1': U1,
'end1': U4,
'end2': U4,
'end3': U4
},
'CFG-USB': {
'vendorID': U2,
'productID': U2,
'reserved1': U2,
'reserved2': U2,
'powerConsumpt': U2,
'flags': X2,
'vendorString': C32,
'productString': C32,
'serialNumber': C32
},
# ********************************************************************
# 'ESF-MEAS': {
# 'timeTag': U4,
# 'flags': X2,
# 'id': U2,
# 'datagroup': ('None',{  # repeating group
# 'data': X4
# }),
# 'calibgroup': ('None',{  # repeating group
# 'calibtTag': U4
# })},
'ESF-STATUS': {
'iTOW': U4,
'version': U1,
'reserved1': U1,
'reserved2': U2,
'reserved3': U4,
'status': U1,
'reserved4': U1,
'reserved5': U1,
'numCh': U1,
'group': ('numCh',{  # repeating group * numCh
'sensStatus1': X1,
'sensStatus2': X2,
'freq': U1,
'faults': X1,
})},
# ********************************************************************
'INF-DEBUG': {
'message': CH
},
'INF-ERROR': {
'message': CH
},
'INF-NOTICE': {
'message': CH
},
'INF-TEST': {
'message': CH
},
'INF-WARNING': {
'message': CH
},
# ********************************************************************
'LOG-BATCH': {
'version': U1,
'contentValid': X1,
'msgCnt': U2,
'iTOW': U4,
'year': U2,
'month': U1,
'day': U1,
'hour': U1,
'min': U1,
'sec': U1,
'valid': X1,
'tAcc': U4,
'fracSec': I4,
'fixType': U1,
'flags': X1,
'flags2': X1,
'numSV': U1,
'lon': I4,
'lat': I4,
'height': I4,
'hMSL': I4,
'hAcc': U4,
'vAcc': U4,
'velN': I4,
'velE': I4,
'velD': I4,
'gSpeed': I4,
'headMot': I4,
'sAcc': U4,
'headAcc': U4,
'pDOP': U2,
'reserved1': U2,
'distance': U4,
'totalDistance': U4,
'distanceStd': U4,
'reserved2': U4
},
'LOG-CREATE': {
'version': U1,
'logCfg': X1,
'reserved1': U1,
'logSize': U1,
'userDefinedSize': U4
},
'LOG-FINDTIME': {
'version': U1,
'type': U1,
'reserved1': U2,
'entryNumber': U4
},
'LOG-INFO': {
'version': U1,
'reserved1': U3,
'filestoreCapacity': U4,
'reserved2': U8,
'currentMaxLogSize': U4,
'currentLogSize': U4,
'entryCount': U4,
'oldestYear': U2,
'oldestMonth': U1,
'oldestDay': U1,
'oldestHour': U1,
'oldestMinute': U1,
'oldestSecond': U1,
'reserved3': U1,
'newestYear': U2,
'newestMonth': U1,
'newestDay': U1,
'newestHour': U1,
'newestMinute': U1,
'newestSecond': U1,
'reserved4': U1,
'status': X1,
'reserved5': U3
},
'LOG-RETRIEVEPOSEXTRA': {
'entryIndex': U4,
'version': U1,
'reserved1': U1,
'year': U2,
'month': U1,
'day': U1,
'hour': U1,
'minute': U1,
'second': U1,
'reserved2': U3,
'distance': U4,
'reserved3': U12
},
'LOG-RETRIEVEPOS': {
'entryIndex': U4,
'lon': I4,
'lat': I4,
'hMSL': I4,
'hAcc': U4,
'gSpeed': U4,
'heading': U4,
'version': U1,
'fixType': U1,
'year': U2,
'month': U1,
'day': U1,
'hour': U1,
'minute': U1,
'second': U1,
'reserved1': U1,
'numSV': U1,
'reserved2': U1
},
'LOG-RETRIEVESTRING': {
'entryIndex': U4,
'version': U1,
'reserved1': U1,
'year': U2,
'month': U1,
'day': U1,
'hour': U1,
'minute': U1,
'second': U1,
'reserved2': U1,
'byteCount': U2,
'group': ('byteCount',{  # repeating group * byteCount
'data': U1
})},
# ********************************************************************
'MGA-ACK-DATA0': {
'type': U1,
'version': U1,
'infoCode': U1,
'msgId': U1,
'msgPayloadStart': U4
},
'MGA-NAK-DATA0': {
'type': U1,
'version': U1,
'infoCode': U1,
'msgId': U1,
'msgPayloadStart': U4
},
'MGA-ANO': {
'type': U1,
'version': U1,
'svId': U1,
'gnssId': U1,
'year': U1,
'month': U1,
'day': U1,
'reserved1': U1,
'data': U64,
'reserved2': U4,
},
'MGA-BDS-EPH': {
'type': U1,
'version': U1,
'svId': U1,
'reserved1': U1,
'SatH1': U1,
'IODC': U1,
'a2': I2,
'a1': I4,
'a0': I4,
'toc': U4,
'TGD1': I2,
'URAI': U1,
'IODE': U1,
'toe': U4,
'sqrtA': U4,
'e': U4,
'omega': I4,
'Deltan': I2,
'IDOT': I2,
'M0': I4,
'Omega0': I4,
'OmegaDot': I4,
'i0': I4,
'Cuc': I4,
'Cus': I4,
'Crc': I4,
'Crs': I4,
'Cic': I4,
'Cis': I4,
'reserved2': U4
},
'MGA-BDS-ALM': {
'type': U1,
'version': U1,
'svId': U1,
'reserved1': U1,
'Wna': U1,
'toa': U1,
'deltaI': I2,
'sqrtA': U4,
'e': U4,
'omega': I4,
'M0': I4,
'Omega0': I4,
'omegaDot': I4,
'a0': I2,
'a1': I2,
'reserved2': U4
},
'MGA-BDS-HEALTH': {
'type': U1,  # 0x04
'version': U1,
'reserved1': U2,
'healthCode01': U2,
'healthCode02': U2,
'healthCode03': U2,
'healthCode04': U2,
'healthCode05': U2,
'healthCode06': U2,
'healthCode07': U2,
'healthCode08': U2,
'healthCode09': U2,
'healthCode10': U2,
'healthCode11': U2,
'healthCode12': U2,
'healthCode13': U2,
'healthCode14': U2,
'healthCode15': U2,
'healthCode16': U2,
'healthCode17': U2,
'healthCode18': U2,
'healthCode19': U2,
'healthCode20': U2,
'healthCode21': U2,
'healthCode22': U2,
'healthCode23': U2,
'healthCode24': U2,
'healthCode25': U2,
'healthCode26': U2,
'healthCode27': U2,
'healthCode28': U2,
'healthCode29': U2,
'healthCode30': U2,
'reserved2': U4
},
'MGA-BDS-UTC': {
'type': U1,
'version': U1,
'reserved1': U2,
'a0UTC': I4,
'a1UTC': I4,
'dtLS': I1,
'reserved2': U1,
'wnRec': U1,
'wnLSF': U1,
'dN': U1,
'dtLSF': I1,
'reserved3': U2
},
'MGA-BDS-IONO': {
'type': U1,
'version': U1,
'reserved1': U2,
'alpha0': I1,
'alpha1': I1,
'alpha2': I1,
'alpha3': I1,
'beta0': I1,
'beta1': I1,
'beta2': I1,
'beta3': I1,
'reserved2': U4
},
'MGA-DBD': {
'reserved1': U12,
'group': ('None',{  # repeating group
'data': U1
})},
'MGA-FLASH-DATA': {
'type': U1,
'version': U1,
'sequence': U2,
'size': U2,
'group': ('size',{  # repeating group * size
'data': U1
})},
'MGA-FLASH-STOP': {
'type': U1,
'version': U1
},
'MGA-FLASH-ACK': {
'type': U1,
'version': U1,
'ack': U1,
'reserved1': U1,
'sequence': U2
},
'MGA-GAL-EPH': {
'type': U1,
'version': U1,
'svId': U1,
'reserved1': U1,
'iodNav': U2,
'deltaN': I2,
'm0': I4,
'e': U4,
'sqrtA': U4,
'omega0': I4,
'i0': I4,
'omega': I4,
'omegaDot': I4,
'iDot': I2,
'cuc': I2,
'cus': I2,
'crc': I2,
'crs': I2,
'cic': I2,
'cis': I2,
'toe': U2,
'af0': I4,
'af1': I4,
'af2': I1,
'sisaIndexE1E5b': U1,
'toc': U2,
'bgdE1E5b': I2,
'reserved2': U2,
'healthE1B': U1,
'dataValidityE1B': U1,
'healthE5b': U1,
'dataValidityE5b': U1,
'reserved3': U4
},
'MGA-GAL-ALM': {
'type': U1,
'version': U1,
'svId': U1,
'reserved1': U1,
'ioda': U1,
'almWNa': U1,
'toa': U2,
'deltaSqrtA': I2,
'e': U2,
'deltaI': I2,
'omega0': I2,
'omegaDot': I2,
'omega': I2,
'm0': I2,
'af0': I2,
'af1': I2,
'healthE1B': U1,
'healthE5b': U1,
'reserved2': U4
},
'MGA-GAL-TIMEOFFSET': {
'type': U1,
'version': U1,
'reserved1': U1[2],
'a0G': I2,
'a1G': I2,
't0G': U1,
'wn0G': U1,
'reserved2': U2
},
'MGA-GAL-UTC': {
'type': U1,
'version': U1,
'reserved1': U2,
'a0': I4,
'a1': I4,
'dtLS': I1,
'tot': U1,
'wnt': U1,
'wnLSF': U1,
'dN': U1,
'dTLSF': I1,
'reserved2': U2
},
'MGA-GLO-EPH': {
'type': U1,
'version': U1,
'svId': U1,
'reserved1': U1,
'FT': U1,
'B': U1,
'M': U1,
'H': I1,
'x': I4,
'y': I4,
'z': I4,
'dx': I4,
'dy': I4,
'dz': I4,
'ddx': I1,
'ddy': I1,
'ddz': I1,
'tb': U1,
'gamma': I2,
'E': U1,
'deltaTau': I1,
'tau': I4,
'reserved2': U4
},
'MGA-GLO-ALM': {
'type': U1,
'version': U1,
'svId': U1,
'reserved1': U1,
'N': U2,
'M': U1,
'C': U1,
'tau': I2,
'epsilon': U2,
'lambda': I4,
'deltaI': I4,
'tLambda': U4,
'deltaT': I4,
'deltaDT': I1,
'H': I1,
'omega': I2,
'reserved2': U4
},
'MGA-GLO-TIMEOFFSET': {
'type': U1,
'version': U1,
'N': U2,
'tauC': I4,
'tauGps': I4,
'B1': I2,
'B2': I2,
'reserved1': U4
},
'MGA-GPS-EPH': {
'type': U1,
'version': U1,
'svId': U1,
'reserved1': U1,
'fitInterval': U1,
'uraIndex': U1,
'svHealth': U1,
'tgd': I1,
'iodc': U2,
'toc': U2,
'reserved2': U1,
'af2': I1,
'af1': I2,
'af0': I4,
'crs': I2,
'deltaN': I2,
'm0': I4,
'cuc': I2,
'cus': I2,
'e': U4,
'sqrtA': U4,
'toe': U2,
'cic': I2,
'omega0': I4,
'cis': I2,
'crc': I2,
'i0': I4,
'omega': I4,
'omegaDot': I4,
'idot': I2,
'reserved3': U4
},
'MGA-GPS-ALM': {
'type': U1,
'version': U1,
'svId': U1,
'svHealth': U1,
'e': U2,
'almWNa': U1,
'toa': U1,
'deltaI': I2,
'omegaDot': I2,
'sqrtA': U4,
'omega0': I4,
'omega': I4,
'm0': I4,
'af0': I2,
'af1': I2,
'reserved1': U4
},
'MGA-GPS-HEALTH': {
'type': U1,
'version': U1,
'reserved1': U2,
'healthCode01': U1,
'healthCode02': U1,
'healthCode03': U1,
'healthCode04': U1,
'healthCode05': U1,
'healthCode06': U1,
'healthCode07': U1,
'healthCode08': U1,
'healthCode09': U1,
'healthCode10': U1,
'healthCode11': U1,
'healthCode12': U1,
'healthCode13': U1,
'healthCode14': U1,
'healthCode15': U1,
'healthCode16': U1,
'healthCode17': U1,
'healthCode18': U1,
'healthCode19': U1,
'healthCode20': U1,
'healthCode21': U1,
'healthCode22': U1,
'healthCode23': U1,
'healthCode24': U1,
'healthCode25': U1,
'healthCode26': U1,
'healthCode27': U1,
'healthCode28': U1,
'healthCode29': U1,
'healthCode30': U1,
'healthCode31': U1,
'healthCode32': U1,
'reserved': U4,
},
'MGA-GPS-UTC': {
'type': U1,
'version': U1,
'reserved1': U2,
'utcA0': I4,
'utcA1': I4,
'utcDtLS': I1,
'utcTot': U1,
'utcWNt': U1,
'utcWNlsf': U1,
'utcDn': U1,
'utcDtLSF': I1,
'reserved2': U2
},
'MGA-GPS-IONO': {
'type': U1,
'version': U1,
'reserved1': U2,
'ionoAlpha0': I1,
'ionoAlpha1': I1,
'ionoAlpha2': I1,
'ionoAlpha3': I1,
'ionoBeta0': I1,
'ionoBeta1': I1,
'ionoBeta2': I1,
'ionoBeta3': I1,
'reserved2': U4
},
'MGA-INI-POS_XYZ': {
'type': U1,
'version': U1,
'reserved1': U2,
'ecefX': I4,
'ecefY': I4,
'ecefZ': I4,
'posAcc': U4
},
'MGA-INI-POS_LLH': {
'type': U1,
'version': U1,
'reserved1': U2,
'lat': I4,
'lon': I4,
'alt': I4,
'posAcc': U4
},
'MGA-INI-TIME_UTC': {
'type': U1,
'version': U1,
'ref': X1,
'leapSecs': I1,
'year': U2,
'month': U1,
'day': U1,
'hour': U1,
'minute': U1,
'second': U1,
'reserved1': U1,
'ns': U4,
'tAccS': U2,
'reserved2': U2,
'tAccNs': U4
},
'MGA-INI-TIME_GNSS': {
'type': U1,
'version': U1,
'ref': X1,
'gnssId': U1,
'reserved1': U2,
'week': U2,
'tow': U4,
'ns': U4,
'tAccS': U2,
'reserved2': U2,
'tAccNs': U4
},
'MGA-INI-CLKD': {
'type': U1,
'version': U1,
'reserved1': U2,
'clkD': I4,
'clkDAcc': U4
},
'MGA-INI-FREQ': {
'type': U1,
'version': U1,
'reserved1': U1,
'flags': X1,
'freq': I4,
'freqAcc': U4
},
'MGA-INI-EOP': {
'type': U1,
'version': U1,
'reserved1': U2,
'd2kRef': U2,
'd2kMax': U2,
'xpP0': I4,
'xpP1': I4,
'ypP0': I4,
'ypP1': I4,
'dUT1': I4,
'ddUT1': I4,
'reserved2': U40
},
'MGA-QZSS-EPH': {
'type': U1,
'version': U1,
'svId': U1,
'reserved1': U1,
'fitInterval': U1,
'uraIndex': U1,
'svHealth': U1,
'tgd': I1,
'iodc': U2,
'toc': U2,
'reserved2': U1,
'af2': I1,
'af1': I2,
'af0': I4,
'crs': I2,
'deltaN': I2,
'm0': I4,
'cuc': I2,
'cus': I2,
'e': U4,
'sqrtA': U4,
'toe': U2,
'cic': I2,
'omega0': I4,
'cis': I2,
'crc': I2,
'i0': I4,
'omega': I4,
'omegaDot': I4,
'idot': I2,
'reserved3': U2
},
'MGA-QZSS-ALM': {
'type': U1,
'version': U1,
'svId': U1,
'svHealth': U1,
'e': U2,
'almWNa': U1,
'toa': U1,
'deltaI': I2,
'omegaDot': I2,
'sqrtA': U4,
'omega0': I4,
'omega': I4,
'm0': I4,
'af0': I2,
'af1': I2,
'reserved1': U4
},
'MGA-QZSS-HEALTH': {
'type': U1,
'version': U1,
'reserved1': U2,
'healthCode1': U1,
'healthCode2': U1,
'healthCode3': U1,
'healthCode4': U1,
'healthCode5': U1,
'reserved2': U3
},
# ********************************************************************
'MON-GNSS': {
'version': U1,
'supported': X1,
'default': X1,
'enabled': X1,
'simultaneous': U1,
'reserved1': U3,
},
'MON-HW2': {
'ofsI': I1,
'magI': U1,
'ofsQ': I1,
'magQ': U1,
'cfgSource': U1,
'reserved0': U3,
'lowLevCfg': X4,
'reserved11': U4,
'reserved12': U4,
'postStatus': X4,
'reserved2': U4
},
'MON-HW': {
'pinSel': X4,
'pinBank': X4,
'pinDir': X4,
'pinVal': X4,
'noisePerMS': U2,
'agcCnt': U2,
'aStatus': U1,
'aPower': U1,
'flags': X1,
'reserved1': U1,
'usedMask': X4,
'VP01': X1,
'VP02': X1,
'VP03': X1,
'VP04': X1,
'VP05': X1,
'VP06': X1,
'VP07': X1,
'VP08': X1,
'VP09': X1,
'VP10': X1,
'VP11': X1,
'VP12': X1,
'VP13': X1,
'VP14': X1,
'VP15': X1,
'VP16': X1,
'VP17': X1,
'VP18': X1,
'VP19': X1,
'VP20': X1,
'VP21': X1,
'VP22': X1,
'VP23': X1,
'VP24': X1,
'VP25': X1,
'jamInd': U1,
'reserved3': U2,
'pinIrq': X4,
'pullH': X4,
'pullL': X4
},
'MON-IO': {
'rxBytes': U4,
'txBytes': U4,
'parityErrs': U2,
'framingErrs': U2,
'overrunErrs': U2,
'breakCond': U2,
'rxBusy': U1,
'txBusy': U1,
'reserved1': U2
},
'MON-MSGPP': {
'msg10': U2,
'msg11': U2,
'msg12': U2,
'msg13': U2,
'msg14': U2,
'msg15': U2,
'msg16': U2,
'msg17': U2,
'msg20': U2,
'msg21': U2,
'msg22': U2,
'msg23': U2,
'msg24': U2,
'msg25': U2,
'msg26': U2,
'msg27': U2,
'msg30': U2,
'msg31': U2,
'msg32': U2,
'msg33': U2,
'msg34': U2,
'msg35': U2,
'msg36': U2,
'msg37': U2,
'msg40': U2,
'msg41': U2,
'msg42': U2,
'msg43': U2,
'msg44': U2,
'msg45': U2,
'msg46': U2,
'msg47': U2,
'msg50': U2,
'msg51': U2,
'msg52': U2,
'msg53': U2,
'msg54': U2,
'msg55': U2,
'msg56': U2,
'msg57': U2,
'msg60': U2,
'msg61': U2,
'msg62': U2,
'msg63': U2,
'msg64': U2,
'msg65': U2,
'msg66': U2,
'msg67': U2,
'skipped1': U4,
'skipped2': U4,
'skipped3': U4,
'skipped4': U4,
'skipped5': U4,
'skipped6': U4
},
'MON-PATCH': {
'version': U2,
'nEntries': U2,
'group': ('nEntries',{  # repeating group * nEntries
'patchInfo': X4,
'comparatorNumber': U4,
'patchAddress': U4,
'patchData': U4,
})},
'MON-RXBUF': {
'pending0': U2,
'pending1': U2,
'pending2': U2,
'pending3': U2,
'pending4': U2,
'pending5': U2,
'usage0': U1,
'usage1': U1,
'usage2': U1,
'usage3': U1,
'usage4': U1,
'usage5': U1,
'peakUsage0': U1,
'peakUsage1': U1,
'peakUsage2': U1,
'peakUsage3': U1,
'peakUsage4': U1,
'peakUsage5': U1
},
'MON-RXR': {
'flags': U1
},
'MON-SMGR': {
'version': U1,
'reserved1': U3,
'iTOW': U4,
'intOsc': X2,
'extOsc': X2,
'discSrc': U1,
'gnss': X1,
'extInt0': X1,
'extInt1': X1
},
'MON-TXBUF': {
'pending0': U2,
'pending1': U2,
'pending2': U2,
'pending3': U2,
'pending4': U2,
'pending5': U2,
'usage0': U1,
'usage1': U1,
'usage2': U1,
'usage3': U1,
'usage4': U1,
'usage5': U1,
'peakUsage0': U1,
'peakUsage1': U1,
'peakUsage2': U1,
'peakUsage3': U1,
'peakUsage4': U1,
'peakUsage5': U1,
'tUsage': U1,
'tPeakUsage': U1,
'errors': X1,
'reserved1': U1
},
'MON-VER': {
'swVersion': C30,
'hwVersion': C30,
'romVersion': C30,
'group': ('None',{  # repeating group
'extension': C30
})},
# ********************************************************************
'NAV-AOPSTATUS': {
'iTOW': U4,
'config': U1,
'status': U1,
'reserved0': U1,
'reserved1': U1,
'avail': U4,
'reserved2': U4,
'reserved3': U4
},
'NAV-CLOCK': {
'iTOW': U4,
'clkB': I4,
'clkD': I4,
'tAcc': U4,
'fAcc': U4
},
'NAV-DGPS': {
'iTOW': U4,
'age': I4,
'baseId': I2,
'baseHealth': I2,
'numCh': U1,
'status': U1,
'reserved1': U2,
'channels' : ('numCh',{  # repeating group * numCh
'svid' : U1,
'flags': U1,
'ageC' : U2,
'prc': R4,
'prrc': R4
})},
'NAV-DOP': {
'iTOW': U4,
'gDOP': U2,
'pDOP': U2,
'tDOP': U2,
'vDOP': U2,
'hDOP': U2,
'nDOP': U2,
'eDOP': U2
},
'NAV-EKFSTATUS': {
'pulses': I4,
'period': I4,
'gyroMean': U4,
'temperature': I2,
'direction': I1
},
'NAV-EOE': {
'iTOW': U4
},
'NAV-GEOFENCE': {
'iTOW': U4,
'version' : U1,
'status' : U1,
'numFences': U1,
'combState': U1,
'group': ('numFences', {  # repeating group * numFences
'state': U1,
'reserved1': U1
})},
'NAV-ODO' : {
'version' : U1,
'reserved13': U1,
'iTOW': U4,
'distance' : U4,
'totalDistance' : U4,
'distanceStd' : U4
},
'NAV-ORB' : {
'iTOW': U4,
'version' : U1,
'numCh' : U1,
'reserved1': U2,
'group' : ('numCh', {  # repeating group * numCh
'gnssId': U1,
'svId': U1,
'svFlag': X1,
'eph': X1,
'alm': X1,
'otherOrb': X1
})},
'NAV-POSECEF': {
'iTOW': U4,
'ecefX': I4,
'ecefY': I4,
'ecefZ': I4,
'pAcc': U4
},
'NAV-POSLLH': {
'iTOW': U4,
'lon': I4,
'lat': I4,
'height': I4,
'hMSL': I4,
'hAcc': U4,
'vAcc': U4
},
'NAV-PVT': {
'iTOW': U4,
'year': U2,
'month': U1,
'day': U1,
'hour': U1,
'min': U1,
'second': U1,
'valid': X1,
'tAcc': U4,
'nano': I4,
'fixType': U1,
'flags': X1,
'flags2': X1,
'numSV': U1,
'lon': I4,
'lat': I4,
'height': I4,
'hMSL': I4,
'hAcc': U4,
'vAcc': U4,
'velN': I4,
'velE': I4,
'velD': I4,
'gSpeed': I4,
'headMot': I4,
'sAcc': U4,
'headAcc': U4,
'pDOP': U2,
'reserved1': U6,
'headVeh': I4,
'magDec': I2,
'magAcc': U2
},
'NAV-SAT': {
'iTOW': U4,
'version' : U1,
'numCh' : U1,
'reserved11': I1,
'reserved12': I1,
'group': ('numCh',{  # repeating group * numCh
'gnssId': U1,
'svId': U1,
'cno': U1,
'elev': I1,
'azim': I2,
'prRes': I2,
'flags': X4
})},
'NAV-SBAS': {
'iTOW': U4,
'geo' : U1,
'mode:' : U1,
'sys': I1,
'service': X1,
'numCh': U1,
'reserved0': U3,
'channels': ('numCh',{  # repeating group * numCh
'svid': U1,
'flags': U1,
'udre': U1,
'svSys': U1,
'svService': U1,
'reserved1': U1,
'prc': I2,
'reserved2': U2,
'ic': I2
})},
'NAV-SOL': {
'iTOW': U4,
'fTOW': I4,
'week': I2,
'gpsFix': U1,
'flags': X1,
'ecefX': I4,
'ecefY': I4,
'ecefZ': I4,
'pAcc': U4,
'ecefVX': I4,
'ecefVY': I4,
'ecefVZ': I4,
'sAcc': U4,
'pDOP': U2,
'reserved1': U1,
'numSV': U1,
'reserved2': U4
},
'NAV-STATUS': {
'iTOW': U4,
'gpsFix': U1,
'flags': X1,
'fixStat': X1,
'flags2': X1,
'ttff': U4,
'msss': U4
},
'NAV-SVINFO': {
'iTOW': U4,
'numCh': U1,
'globalFlags': X1,
'reserved2': U2,
'channels': ('numCh',{  # repeating group * numCh
'chn': U1,
'svid': U1,
'flags': X1,
'quality': X1,
'cno': U1,
'elev': I1,
'azim': I2,
'prRes': I4
})},
'NAV-TIMEBDS': {
'iTOW': U4,
'SOW': U4,
'fSOW': I4,
'week': I2,
'leapS': I1,
'valid': X1,
'tAcc': U4
},
'NAV-TIMEGAL': {
'iTOW': U4,
'galTow': U4,
'fGalTow': I4,
'galWno': I2,
'leapS': I1,
'valid': X1,
'tAcc': U4
},
'NAV-TIMEGLO': {
'iTOW': U4,
'TOD': U4,
'fTOD': I4,
'Nt': U2,
'N4': U1,
'valid': X1,
'tAcc': U4
},
'NAV-TIMEGPS': {
'iTOW': U4,
'fTOW': I4,
'week': I2,
'leapS': I1,
'valid': X1,
'tAcc': U4
},
'NAV-TIMELS': {
'iTOW': U4,
'version': U1,
'reserved1': U3,
'srcOfCurrLs': U1,
'currLs': I1,
'srcOfLsChange': U1,
'lsChange': I1,
'timeToLsEvent': I4,
'dateOfLsGpsWn': U2,
'dateOfLsGpsDn': U2,
'reserved2': U3,
'valid': X1
},
'NAV-TIMEUTC': {
'iTOW': U4,
'tAcc': U1,
'nano': I4,
'year': U2,
'month': U1,
'day': U1,
'hour': U1,
'min': U1,
'sec': U1,
'validflags': X1
},
'NAV-VELECEF': {
'iTOW': U4,
'ecefVX': I4,
'ecefVY': I4,
'ecefVZ': I4,
'sAcc': U4
},
'NAV-VELNED': {
'iTOW': U4,
'velN': I4,
'velE': I4,
'velD': I4,
'speed': U4,
'gSpeed': U4,
'heading': I4,
'sAcc': U4,
'cAcc': U4
},
# ********************************************************************
'RXM-IMES': {
'numTx': U1,
'version': U1,
'reserved1': U2,
'group': ('numTx',{  # repeating group * numTx
'reserved2': U1,
'txId': U1,
'reserved3': U3,
'cno': U1,
'reserved4': U2,
'doppler': I4,
'position1_1': X4,
'position1_2': X4,
'position2_1': X4,
'lat': I4,
'lon': I4,
'shortIdFrame': X4,
'mediumIdLSB': U4,
'mediumId_2': X4,
})},
'RXM-MEASX': {
'version': U1,
'reserved1': U3,
'gpsTOW': U4,
'gloTOW': U4,
'bdsTOW': U4,
'reserved2': U4,
'qzssTOW': U4,
'gpsTOWacc': U2,
'gloTOWacc': U2,
'bdsTOWacc': U2,
'reserved3': U2,
'qzssTOWacc': U2,
'numCh': U1,
'flags': U1,
'reserved4': U8,
'group': ('numCh',{  # repeating group * numCh
'gnssId': U1,
'svId': U1,
'cNo': U1,
'mpathIndic': U1,
'dopplerMS': I4,
'dopplerHz': I4,
'wholeChips': U2,
'fracChips': U2,
'codePhase': U4,
'intCodePhase': U1,
'pseuRangeRMSErr': U1,
'reserved5': U2
})},
'RXM-RAWX': {
'rcvTow': R8,
'week': U2,
'leapS': I1,
'numMeas': U1,
'recStat': X1,
'reserved1': U3,
'prMes': R8,
'cpMes': R8,
'doMes': R4,
'gnssId': U1,
'svId': U1,
'reserved2': U1,
'freqId': U1,
'locktime': U2,
'cno': U1,
'prStdev': X1,
'cpStdev': X1,
'doStdev': X1,
'trkStat': X1,
'reserved3': U1
},
'RXM-RLM': {
'version': U1,
'type': U1,
'svId': U1,
'reserved1': U1,
'beacon': U8,
'beacon2': U1,
'beacon3': U1,
'beacon4': U1,
'beacon5': U1,
'beacon6': U1,
'beacon7': U1,
'beacon8': U1,
'message': U1,
'params1': U1,
'params2': U1
},
'RXM-RTCM': {
'version': U1,
'flags': X1,
'subType': U2,
'refStation': U2,
'msgType': U2
},
'RXM-SFRBX': {
'gnssId': U1,
'svId': U1,
'reserved1': U1,
'freqId': U1,
'numWords': U1,
'chn': U1,
'version': U1,
'reserved2': U1,
'group' : ('numWords',{  # repeating group * numWords
'dwrd': U4
})},
'RXM-SVSI': {
'iTOW': U4,
'week': I2,
'numVis': U1,
'numSV': U1,
'svid': U1,
'svFlag': X1,
'azim': I2,
'elev': I1,
'age': X1
},
# ********************************************************************
'SEC-UNIQID': {
'version': U1,
'reserved1': U3,
'uniqueId': U5
},
# ********************************************************************
'TIM-DOSC': {
'version': U1,
'reserved1': U3,
'value': U4
},
'TIM-FCHG': {
'version': U1,
'reserved1': U3,
'iTOW': U4,
'intDeltaFreq': I4,
'intDeltaFreqU': U4,
'intRaw': U4,
'extDeltaFreq': I4,
'extDeltaFreqU': U4,
'extRaw': U4,
},
'TIM-SMEAS': {
'version': U1,
'numMeas': U1,
'reserved1': U2,
'iTOW': U4,
'reserved2': U4,
'group': ('numMeas',{  # repeating group * numMeas
'sourceId': U1,
'flags': X1,
'phaseOffsetFr': I1,
'phaseUncFrac': U1,
'phaseOffset': I4,
'phaseUnc': U4,
'reserved3': U4,
'freqOffset': I4,
'freqUnc': U4,
})},
'TIM-SVIN': {
'dur': U4,
'meanX': I4,
'meanY': I4,
'meanZ': I4,
'meanV': U4,
'obs': U4,
'valid': U1,
'active': U1,
'reserved1': U2
},
'TIM-TM2': {
'ch': U1,
'flags': X1,
'count': U2,
'wnR': U2,
'wnF': U2,
'towMsR': U4,
'towSubMsR': U4,
'towMsF': U4,
'towSubMsF': U4,
'accEst': U4
},
'TIM-TOS': {
'version': U1,
'gnssId': U1,
'reserved11': U2,
'flags': X4,
'year': U2,
'month': U1,
'day': U1,
'hour': U1,
'minute': U1,
'second': U1,
'utcStandard': U1,
'utcOffset': I4,
'utcUncertaint': U4,
'week': U4,
'TOW': U4,
'gnssOffset': I4,
'gnssUncertainty': U4,
'intOscOffset': I4,
'intOscUncertainty': U4,
'extOscOffset': I4,
'extOscUncertainty': U4
},
'TIM-TP': {
'towMS': U4,
'towSubMS': U4,
'qErr': I4,
'week': U2,
'flags': X1,
'reserved1': U1
},
'TIM-VCOCAL': {
'type': U1,
'version': U1,
'oscId': U1,
'reserved1': U3,
'gainUncertainty': U2,
'gainVco': I4,
},
'TIM-VRFY': {
'itow': I4,
'frac': I4,
'deltaMs': I4,
'deltaNs': I4,
'wno': U2,
'flags': X1,
'reserved1': U1
},
# ********************************************************************
'UPD-SOS': {  # System restored from backup
'cmd': U1,
'reserved1': U3,
'response': U1,
'reserved2': U3
}
}
