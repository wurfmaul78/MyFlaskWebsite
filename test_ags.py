from ags import AGSSource, bykey,byplace, herausgeber

def test_herausgeber():
    assert herausgeber()== 'Statistisches Bundesamt, Wiesbaden'

def test_source():
    assert AGSSource == "https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:ags_2011-04-01/download/AGS_2011-04-01.json"
 
def test_place():
    assert byplace('Linz am Rhein') == (["07138041", "Linz am Rhein, Stadt"]) 

if (__name__) == ('__main__'):
    print (byplace('Linz am Rhein'))