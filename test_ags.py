import ags
import pytest

def test_source():
    assert ags.AGSSource == "https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:ags_2011-04-01/download/AGS_2011-04-01.json"
 
def test_place():
    assert ags.byplace('München') == {'Data': ['09162000', 'München, Landeshauptstadt'], 'Source': 'Statistisches Bundesamt Wiesbaden', 'info': 'gerhard.posch@outlook.com'}
    assert ags.byplace('Linz am Rhein, Stadt') == {'Data': ['07138041', 'Linz am Rhein, Stadt'], 'Source': 'Statistisches Bundesamt Wiesbaden', 'info': 'gerhard.posch@outlook.com'}
if (__name__) == ('__main__'):
    print (ags.byplace("Linz am Rhein")) 
