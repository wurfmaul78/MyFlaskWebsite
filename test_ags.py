#import pytest
import ags

def test_agskey(): #Testet die Requests per APS-Key auf Richtigkeit
    assert ags.bykey('07138041')  == ['07138041', 'Linz am Rhein, Stadt']
    assert ags.bykey ('01051089') == ["01051089","Quickborn"]
    assert ags.bykey ('01053058') == ["01053058","Juliusburg"]
    assert ags.bykey ('01054070') == ["01054070","Koldenbüttel"]
    assert ags.bykey ('01060020') == ["01060020","Fahrenkrug"]

def test_agsplace(): # Testet die Requests per Place auf Richtigkeit
    assert ags.byplace('Linz am Rhein') == ["07138041","Linz am Rhein, Stadt"]
    assert ags.byplace('Bonn') == ['05314000', 'Bonn, Stadt']
    assert ags.byplace('Bilshausen') == ["03152002","Bilshausen"]

def test_meta(): #Testet ob der richtige Herausgeber aus den Metadaten gezogen wird
    assert ags.herausgeber() == ("Statistisches Bundesamt, Wiesbaden")

def test_source(): #Prüft die Datengrundlage für die AGS Search
    assert ags.AGSSource  == ("https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:ags_2011-04-01/download/AGS_2011-04-01.json")

if (__name__) == ('__main__'): #Wenn die Datei direkt aufgerufen wird, Durchführung der Tests
    test_source()
    test_meta()
    test_agskey()
    test_agsplace()