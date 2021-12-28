#Sourc: https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:ags_2011-04-01/download/AGS_2011-04-01.json
import requests, json

AGSSource  = "https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:ags_2011-04-01/download/AGS_2011-04-01.json"
AGSLoad = requests.get(AGSSource)
AGSJSON = AGSLoad.json()
AGSLoad.close()

for data in AGSJSON['metadaten']:
    if ('herausgebernameLang') in data:
        Herausgeber = (AGSJSON['metadaten']['herausgebernameLang'])


def byplace(place):
    AGSLoad = requests.get(AGSSource, timeout=5)
    AGSLoad.encoding='utf-8'
    AGSJSON = AGSLoad.json()
    AGSLoad.close()
    for data in AGSJSON['daten']:
        if place in data[1]:
            return(data)

def bykey(place):
    AGSLoad = requests.get(AGSSource, timeout=5)
    AGSLoad.encoding='utf-8'
    AGSJSON = AGSLoad.json()
    AGSLoad.close()
    for data in AGSJSON['daten']:
        if place in data[0]:
            return(data)

if __name__ == ('__main__'):
    print(byplace('Linz am Rhein'))
    print(bykey('07138041'))
   

   #Dictionary aus Liste bauen
