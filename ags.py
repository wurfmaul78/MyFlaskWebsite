#Sourc: https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:ags_2011-04-01/download/AGS_2011-04-01.json
import requests, json

AGSSource  = "https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:ags_2011-04-01/download/AGS_2011-04-01.json"

def herausgeber():
    AGSLoad = requests.get(AGSSource)
    AGSJSON = AGSLoad.json()
    AGSLoad.close()
    for data in AGSJSON['metadaten']:
        if ('herausgebernameLang') in data:
            Herausgeber = (AGSJSON['metadaten']['herausgebernameLang'])
    return (Herausgeber)


def byplace(place):
    AGSLoad = requests.get(AGSSource, timeout=5)
    AGSJSON = AGSLoad.json()
    AGSLoad.close()
    for data in AGSJSON['daten']:
        if place in data[1]:
            print (data)
            data = json.dumps(data, ensure_ascii=False)
            
            return(data)
    else:
        return(f'Your Request {place} does not exist or is wrong written. Please try again :-)')

def bykey(key):
    AGSLoad = requests.get(AGSSource, timeout=5)
    #AGSLoad.encoding='utf-8'
    AGSJSON = AGSLoad.json()
    AGSLoad.close()
    for data in AGSJSON['daten']:
        if key in data[0]:
            data = json.dumps(data, ensure_ascii=False)
            return(data)
    else:
        return(f'Your Request {key} does not exists or is not numeric. Please try again :-)')

if __name__ == ('__main__'):
    print(byplace('Lentföhrden'))
    print(type(byplace('Linz am Rhein')))
    #print(bykey('07138041'))
    #print (herausgeber())
   

   #Dictionary aus Liste bauen
