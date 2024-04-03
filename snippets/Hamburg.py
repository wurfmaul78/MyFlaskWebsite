Ort = ('Hamburg')
Auschluss = ('Hamburg','Berlin','Bremen')
Gesamtliste = ('Kematen','Innsbruck','Zirl')

def search(Ort):
    for a in Auschluss:
        if Ort in a:
            return ('Ausschluss')
    for a in Gesamtliste:
        if Ort in a:
            return ('Ort ist in der Gesamtliste')
    return ('nicht vorhanden')

print (search(Ort))


    