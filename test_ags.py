import ags
import pytest

def test_herausgeber():
    assert ags.herausgeber()== 'Statistisches Bundesamt, Wiesbaden'

def test_source():
    assert ags.AGSSource == "https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:ags_2011-04-01/download/AGS_2011-04-01.json"
 
def test_agsplace():
    assert ags.byplace("Linz am Rhein") == ["07138041", "Linz am Rhein, Stadt"]

if (__name__) == ('__main__'):
    print (ags.byplace('Linz am Rhein'))