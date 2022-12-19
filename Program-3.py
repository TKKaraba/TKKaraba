vek = input ("Kolko ,mas rokov?") 
# Musime spravit casting. Premennu moj_vek, ktora je kvoli prikazu input stale str musit zmenit na typ premenej float, 
# ak by sme zadali desatinne cislo a nasledne vsetko zabalime do int, aby sme mali pekny cely vysledok a nie vysledok desatinne cislo
moj_vek = int(float(vek)*2)
print ("Ja ma  2 krat viac rokov ako ty ", moj_vek)
