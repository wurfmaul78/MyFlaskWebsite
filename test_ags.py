import sources.ags
import pytest

def test_source():
    assert sources.ags.AGSSource == "https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:ags_2024-02-29/download/AGS_2024-02-29.json"
 
def test_place():
    assert sources.ags.byplace('München') == {'Data': ['09162000', 'München, Landeshauptstadt'], 'Source': 'Statistisches Bundesamt Wiesbaden', 'info': 'gerhard.posch@outlook.com'}
    assert sources.ags.byplace('Linz am Rhein, Stadt') == {'Data': ['07138041', 'Linz am Rhein, Stadt'], 'Source': 'Statistisches Bundesamt Wiesbaden', 'info': 'gerhard.posch@outlook.com'}
if (__name__) == ('__main__'):
    print (sources.ags.byplace("Linz am Rhein")) 
