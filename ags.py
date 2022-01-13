#Sourc: https://www.xrepository.de/ api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:ags_2011-04-01/download/AGS_2011-04-01.json
import requests, json
from flask import jsonify


AGSSource  = "https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:ags_2011-04-01/download/AGS_2011-04-01.json"

def herausgeber():
    try:
        AGSLoad = requests.get(AGSSource)
    except:
        info = {'info':'Service temporarly unaivalable, please try later.'}
        return (info)
    AGSJSON = AGSLoad.json()
    AGSLoad.close()
    for data in AGSJSON['metadaten']:
        if ('herausgebernameLang') in data:
            Herausgeber = (AGSJSON['metadaten']['herausgebernameLang'])
    return (Herausgeber)

def makeDict(Liste): #Fassst den Ort und den AGS Key mit weiteren Infos in ein Dictionary zusammen
    AGS_Dict = {}
    AGS_Dict['Data'] = Liste
    AGS_Dict['Source'] = ('Statistisches Bundesamt Wiesbaden')
    AGS_Dict['info'] = ('gerhard.posch@outlook.com')
    return AGS_Dict

def beschreibung():
    try:
        AGSLoad = requests.get(AGSSource)
    except:
        info = {'info':'Service temporarly unaivalable, please try later.'}
        return (info)
    AGSJSON = AGSLoad.json()
    AGSLoad.close()
    for data in AGSJSON['metadaten']:
        if ('beschreibung') in data:
            beschreibung = (AGSJSON['metadaten']['beschreibung'])
    return (beschreibung)


def byplace(place):
    if place == ('Bremen') or place == ('Hamburg') or place==('Berlin'):
        info = ['00000000','Nicht moeglich Die Stadtstaaten Hamburg, Bremen und Berlin suchen sie via Stadt-/Ortsteile bzw. Stadtbezirke.']
        info = (makeDict(info))
        info = (info)
       
        return(info)
    
    try:
        AGSLoad = requests.get(AGSSource, timeout=5)
    except:
        info = {'info':'Service temporarly unaivalable, please try later.'}
        return (info)
    AGSJSON = AGSLoad.json()
    AGSLoad.close()
    for data in AGSJSON['daten']:
        if place in data[1]:
            AGS_Dict = makeDict(data)
            #data = json.dumps(AGS_Dict, ensure_ascii=False)
            data = AGS_Dict
            
            return(data)
    else:
        info = ('Your Request '+ place +' does not exist or is wrong written. Please try again :-)')
        infos = ['00000000',info]
        infos = (makeDict(infos))
        return (infos)



def bykey(key):
    try:
        AGSLoad = requests.get(AGSSource, timeout=5)
    except:
        #info = {'info':'Service temporarly unaivalable, please try later.'}
        info = {}
        info['info'] = ('Service temporarly unavailable, pleayse try later')
        return (info)
    AGSJSON = AGSLoad.json()
    AGSLoad.close()
    for data in AGSJSON['daten']:
        if key in data[0]:
           AGS_Dict = makeDict(data)
          
           return(AGS_Dict)
    else:
        info =('Your Request ' + key + ' does not exists or is not numeric. Please try again :-)')
        infos = ['00000000',info]
    
        return infos

if __name__ == ('__main__'):
    print(byplace('Zehlendorf'))
    print (type(byplace('Zehlendorf')))
    #print(byplace('kinigard'))
    #print(bykey('07138041'))
    #print(byplace('Hamburg'))

   


